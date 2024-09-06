import csv
import random


# Generate synthetic complex data for Lake Chilka
# Latitude and Longitude ranges are approximate for Lake Chilka
def generate_complex_bathymetry_data(num_points=1000):
    # Latitudes between 19.650 and 19.850 (approx range for Lake Chilka)
    latitudes = [round(random.uniform(19.650, 19.850), 6) for _ in range(num_points)]

    # Longitudes between 85.280 and 85.600 (approx range for Lake Chilka)
    longitudes = [round(random.uniform(85.280, 85.600), 6) for _ in range(num_points)]

    # Depth values in meters, with values ranging from -2m to -35m
    # (Negative depths represent underwater bathymetry)
    depths = [round(random.uniform(-35, -2), 2) for _ in range(num_points)]

    return zip(latitudes, longitudes, depths)


# Function to create the complex bathymetry CSV file
def create_bathymetry_csv(file_path, num_points=1000):
    # Generate bathymetry data
    bathymetry_data = generate_complex_bathymetry_data(num_points)

    # Write to CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['latitude', 'longitude', 'depth'])
        # Write data rows
        writer.writerows(bathymetry_data)

    print(f"CSV file '{file_path}' created successfully with {num_points} data points!")


# Specify the output file path
csv_file_path = 'lake_chilka_bathymetry_data.csv'

# Call the function to create the CSV with complex data
create_bathymetry_csv(csv_file_path, num_points=1000)  # Create 1000 data points
