# Maximum Likelihood Classification (MLC) with Python 
<p align="center">
  <img src="https://github.com/akhilchibber/Maximum-Likelihood-Classification/blob/main/MLC.jpg?raw=true" alt="earthml Logo">
</p>

Welcome to this repository where we explore satellite imagery processing using Python! Our primary tool is a script designed to perform Maximum Likelihood Classification (MLC), a statistical method used in remote sensing for classifying satellite imagery.

## What is Maximum Likelihood Classification?

Maximum Likelihood Classification is a probabilistic classification method in remote sensing. It's used for classifying satellite imagery data by assigning each pixel to a class based on statistical characteristics, aiming to accurately categorize land cover or other features in satellite images.

## About This Python Script

This script is perfect for those looking to apply MLC on satellite raster imagery. It's user-friendly, requiring only two inputs:
1. A satellite raster image file.
2. A training dataset in Shapefile format.

### How It Works

- **Data Loading:** Load the satellite raster data and training data from a Shapefile.
- **Data Preparation:** Process these inputs to create a model based on the training data.
- **MLC Processing:** Apply the Maximum Likelihood Classification algorithm to classify each pixel in the raster image.
- **Output Generation:** Produce a new raster file with the classified data.

### Key Features

- **User-Friendly:** Simple inputs for ease of use.
- **Versatile:** Suitable for various types of satellite imagery.
- **Efficient:** Optimized for quick processing times.

## Getting Started

Clone this repository to your local machine and ensure you have the required libraries (`numpy`, `scipy`, `rasterio`, and `geopandas`) installed.

### Prerequisites

- Python 3.x
- Libraries: `numpy`, `scipy`, `rasterio`, `geopandas`

### Running the Script

1. Place your satellite raster image and Shapefile in the designated file paths.
2. Run the script using Python.
3. Find the output as a classified raster image based on your input data.

## Benefits of Using This Script

- **Accessibility:** Makes MLC techniques available to a wider audience.
- **Customization:** Easily modifiable for different project needs.
- **Educational Value:** Ideal for learning about MLC in remote sensing.

## Contributing

We welcome contributions, and your involvement is what makes the community amazing. To contribute:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request against the `main` branch.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name: Akhil Chhibber

LinkedIn: https://www.linkedin.com/in/akhilchhibber/

Medium Blogs: https://medium.com/@akhil.chibber
