import os
import xarray as xr
import json


mydir_tmp = os.getcwd()
combined_filepath = os.path.join(mydir_tmp, "combined_data.nc")

master = {}

# Loop through all .nc files in the directory
for filename in os.listdir(mydir_tmp):
    if filename.endswith(".nc"):
        # Construct the full path to the file
        filepath = os.path.join(mydir_tmp, filename)
        
        # Open the dataset
        ds = xr.open_dataset(filepath)
        
        # Extract the values of 't2m'
        t2m_values = ds['t2m'].values.tolist()  # Convert numpy array to list
        
        # Store the filename (without extension) as a key in master
        key_name = os.path.splitext(filename)[0]
        master[key_name] = t2m_values

# Save the master dictionary as a JSON file
with open('combined_data.json', 'w') as f:
    json.dump(master, f)
