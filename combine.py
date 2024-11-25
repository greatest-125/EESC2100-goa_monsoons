import xarray as xr
import os

# Step 1: Define the path to the folder containing the .nc files
data_folder = r"C:\Users\ldias\Downloads\goa-full"

# Step 2: Create a list of all .nc files in the folder
file_list = [os.path.join(data_folder, file) for file in os.listdir(data_folder) if file.endswith('.nc')]

# Step 3: Combine the NetCDF files using open_mfdataset
# 'combine='by_coords'' merges files along their shared coordinates
# 'concat_dim' specifies the dimension along which to concatenate if needed
combined_ds = xr.open_mfdataset(file_list, combine='by_coords')

# Step 4: Save the combined dataset to a new NetCDF file
output_file = r"C:\Users\ldias\Downloads\goa-full\combined_dataset.nc"
combined_ds.to_netcdf(output_file)

# Optional: Print confirmation
print(f"Combined dataset saved to {output_file}")
