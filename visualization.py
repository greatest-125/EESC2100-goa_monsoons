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

# Subset the data for Goa region
goa_data = data.sel(
    latitude=slice(goa_lat_min, goa_lat_max),
    longitude=slice(goa_lon_min, goa_lon_max)
)

# Convert time to a datetime format
goa_data['time'] = pd.to_datetime(goa_data['time'].values, unit='s', origin='unix')

# Filter for months May (5) to November (11)
goa_data = goa_data.where(goa_data['time.month'].isin(range(5, 11)), drop=True)
# Or select only one month
#goa_data = goa_data.where(goa_data['time.month'] == 10, drop=True)

# Calculate total precipitation for the Goa region (spatially averaged)
goa_precip = goa_data['APCP_sfc'].mean(dim=['latitude', 'longitude'])

# Group by year and sum precipitation for each year
annual_precip = goa_precip.groupby('time.year').sum()
annual_precip_series = annual_precip.to_series()

# Plot the total precipitation for each year
plt.figure(figsize=(10, 6))
annual_precip_series.plot(kind='bar', color='skyblue', edgecolor='black', figsize=(10, 6))
plt.title("Total Precipitation (May to November) in Goa Region (per Year)")
plt.xlabel("Year")
plt.ylabel("Total Precipitation (kg/m²)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
