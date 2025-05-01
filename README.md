# Bathymetry SIH demo

## Project Overview
This project contains tools for analyzing bathymetry (underwater depth) data, particularly focused on Lake Chilka.

## Files
- `bathymetry_analysis.py`: Script to analyze bathymetry data and calculate water coverage percentages
- `create_bathymetry_csv.py`: Script to generate bathymetry data in CSV format
- `bathymetry_data.csv`: Small sample dataset for testing
- `lake_chilka_bathymetry_data.csv`: Larger dataset with 1000 data points of Lake Chilka bathymetry

## Usage
1. Generate bathymetry data:
```
python create_bathymetry_csv.py
```

2. Analyze water coverage:
```
python bathymetry_analysis.py
```

## Requirements
- Python 3.x
- Required libraries: (likely includes numpy, pandas, matplotlib)
