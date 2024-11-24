import xarray as xr

# Load the NetCDF file
input_file = "C:\\Users\\ldias\\Downloads\\goa-full\\combined.nc"
output_file = "C:\\Users\\ldias\\Downloads\\goa-region-expanded.nc"

# Open the dataset
dataset = xr.open_dataset(input_file)

# Define expanded bounding box for the Goa region
lat_min, lat_max = 10.0, 20.0  # Broader latitude range
lon_min, lon_max = 70.0, 76.0  # Broader longitude range

# Subset the data
subset_data = dataset.sel(
    latitude=slice(lat_min, lat_max),
    longitude=slice(lon_min, lon_max)
)

# Remove global attributes that may confuse Panoply
for attr in ["geospatial_lat_min", "geospatial_lat_max", "geospatial_lon_min", "geospatial_lon_max"]:
    if attr in subset_data.attrs:
        del subset_data.attrs[attr]

# Save the subset data to a new NetCDF file
subset_data.to_netcdf(output_file)

print(f"Subset data saved to {output_file}")
