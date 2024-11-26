import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the NetCDF file
file_path = r"C:\Users\ldias\Downloads\goa-full\combined.nc"
data = xr.open_dataset(file_path)

# Define Goa region bounding box
goa_lat_min, goa_lat_max = 14.898333, 15.666667
goa_lon_min, goa_lon_max = 73.675833, 74.336944

# Subset the data for the Goa region
goa_data = data.sel(
    latitude=slice(goa_lat_min, goa_lat_max),
    longitude=slice(goa_lon_min, goa_lon_max)
)

# Convert time to a datetime format
goa_data['time'] = pd.to_datetime(goa_data['time'].values, unit='s', origin='unix')

# Filter for the month of August (8)
goa_data = goa_data.where(goa_data['time.month'].isin(range(5,11)), drop=True)

# Calculate total precipitation for the Goa region (spatially averaged)
goa_precip = goa_data['APCP_sfc'].mean(dim=['latitude', 'longitude'])

# Group by year and sum precipitation for each year
annual_precip = goa_precip.groupby('time.year').sum()
annual_precip_series = annual_precip.to_series()

# Convert the series to a DataFrame for easier display and printing
annual_precip_df = annual_precip_series.reset_index()
annual_precip_df.columns = ['Year', 'Total Precipitation (kg/m²)']

# Print the data table
print("Annual Total Precipitation in Goa Region (August):")
print(annual_precip_df)

# Plot the total precipitation for each year
plt.figure(figsize=(10, 6))
annual_precip_series.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Total Precipitation (August) in Goa Region (per Year)")
plt.xlabel("Year")
plt.ylabel("Total Precipitation (kg/m²)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
