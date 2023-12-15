'''
THE GOAL OF THIS PYTHON SCRIPT IS TO PERFORM A MAXIMUM LIKELIHOOD CLASSIFICATION GIVEN (i) AN INPUT SATELLITE RASTER
IMAGERY AND (ii) TRAINING DATASET IN SHAPEFILE FORMAT
'''

# Import essential libraries
import numpy as np
from scipy.stats import multivariate_normal
from collections import defaultdict
import rasterio
from rasterio.features import rasterize
import geopandas as gpd

# File paths
raster_path = '0000070656-0000047104.tif'
shapefile_path = 'TRAINING.shp'
output_path = 'MLC_CLASS.tif'

# Load the training data from shapefile
shapefile = gpd.read_file(shapefile_path)

# Load the satellite raster data
with rasterio.open(raster_path) as src:
    raster_data = src.read()
    raster_meta = src.meta

# Initialize an array for training data
training_data = []
labels = []

# Iterate over the features in the shapefile and extract the corresponding raster values
for i, feature in enumerate(shapefile.geometry):
    # Rasterize the geometry to create a mask
    mask = rasterize([(feature, 1)],
                     out_shape = (raster_meta['height'], raster_meta['width']),
                     transform = raster_meta['transform'],
                     fill = 0,
                     dtype = rasterio.uint8)
    mask = mask.astype(bool)

    # Apply the mask to the raster data and flatten it to a 1D array
    masked_data = raster_data[:, mask]
    training_data.append(np.mean(masked_data, axis = 1))
    labels.append(shapefile['id'][i])

# Convert to numpy array for further manipulation
training_data = np.array(training_data)
labels = np.array(labels)

# Calculate mean and covariance for each class
classes_info = defaultdict(dict)
for class_id in np.unique(labels):
    class_data = training_data[labels == class_id]
    if len(class_data) > 1:
        classes_info[class_id]['mean'] = np.mean(class_data, axis = 0)
        classes_info[class_id]['cov'] = np.cov(class_data.T) + np.eye(class_data.shape[1]) * 1e-6
    else:
        continue  # Skip classes with only one training sample

# Prepare the raster data for classification
raster_data_2d = raster_data.reshape(raster_data.shape[0], -1).T

# Initialize an empty array for storing classification probabilities
probabilities = np.zeros((raster_data_2d.shape[0], len(classes_info)))

# Calculate Maximum Likelihood Estimate (MLC) probabilities for each class
for i, (class_id, class_info) in enumerate(classes_info.items()):
    probabilities[:, i] = multivariate_normal.pdf(raster_data_2d, mean = class_info['mean'], cov = class_info['cov'])

# Classify each pixel to the class with the highest probability
classification = np.argmax(probabilities, axis = 1)

# Map classification back to class ids
class_ids = list(classes_info.keys())
classification = np.array(class_ids)[classification]

# Reshape classification to original raster shape
classification = classification.reshape(raster_meta['height'], raster_meta['width'])

# Save the classification to a new raster file
raster_meta.update(count = 1, dtype = rasterio.uint8, nodata = 0)
with rasterio.open(output_path, 'w', **raster_meta) as dst:
    dst.write(classification.astype(rasterio.uint8), 1)

# End of the Python Script
print("TASK COMPLETED SUCCESSFULLY")