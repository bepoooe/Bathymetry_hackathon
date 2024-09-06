import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


# Load raw bathymetry data
# Assuming the input file contains columns: 'latitude', 'longitude', and 'depth'
def load_bathymetry_data(file_path):
    data = pd.read_csv(file_path)
    return data


# Interpolate bathymetry data to create a smooth grid for topography detection
def create_topography_grid(data, grid_resolution=100):
    # Create a mesh grid based on the range of latitude and longitude
    lat_range = np.linspace(data['latitude'].min(), data['latitude'].max(), grid_resolution)
    lon_range = np.linspace(data['longitude'].min(), data['longitude'].max(), grid_resolution)

    # Create the grid
    grid_lat, grid_lon = np.meshgrid(lat_range, lon_range)

    # Interpolate depth data onto the grid using cubic interpolation
    grid_depth = griddata((data['latitude'], data['longitude']), data['depth'], (grid_lat, grid_lon), method='cubic')

    return grid_lat, grid_lon, grid_depth


# Plot the topography (depth) of the waterbody
def plot_topography(grid_lat, grid_lon, grid_depth):
    plt.figure(figsize=(10, 8))
    # Create a contour plot for depth
    contour = plt.contourf(grid_lon, grid_lat, grid_depth, cmap='Blues', levels=20)
    plt.colorbar(contour, label='Depth (m)')
    plt.title('Bathymetry Topography')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()


# Analyze water levels based on depth
def analyze_water_levels(grid_depth, threshold_depth=0):
    # Water level can be assumed to be areas with depth below a certain threshold
    water_area = np.sum(grid_depth <= threshold_depth)
    total_area = grid_depth.size

    # Calculate water coverage percentage
    water_coverage_percentage = (water_area / total_area) * 100
    print(f"Water coverage: {water_coverage_percentage:.2f}% of the total area")

    return water_coverage_percentage


# Main function
def main(file_path):
    # Step 1: Load raw bathymetry data
    data = load_bathymetry_data(file_path)

    # Step 2: Create a grid and interpolate topography
    grid_lat, grid_lon, grid_depth = create_topography_grid(data)

    # Step 3: Plot the topography (depth map)
    plot_topography(grid_lat, grid_lon, grid_depth)

    # Step 4: Analyze water levels and areas of waterbodies
    analyze_water_levels(grid_depth, threshold_depth=0)

def load_bathymetry_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file: {e}")
        return None

def load_bathymetry_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file: {e}")
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                print(f"Line {i+1}: {line.strip()}")
        return None


if __name__ == "__main__":
    # Replace 'bathymetry_data.csv' with the path to your data file
    file_path = 'bathymetry_data.csv'
    main(file_path)
