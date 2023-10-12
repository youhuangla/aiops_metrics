import os
import pandas as pd
import re
from tqdm import tqdm

def clean_filename(filename):
    """
    Ensure that the filename is valid and does not contain any special characters.
    """
    return re.sub(r'[^\w.]', '_', filename)

# Define file paths
files_path = 'E:/github/aiops_metrics/metrics/transfer_time/after_transfer_time'
output_path = 'E:/github/aiops_metrics/metrics/transfer_time/sorted_data'

# Get list of files in the directory
files = os.listdir(files_path)

# Concatenate all data with progress bar
all_data = pd.concat([pd.read_excel(os.path.join(files_path, file)) for file in tqdm(files, desc='Loading files')], ignore_index=True)

# Check for 'device' column and update 'cmdb_id' accordingly
if 'device' in all_data.columns:
    all_data['cmdb_id'] = all_data['cmdb_id'].astype(str) + '.' + all_data['device'].astype(str)

# Pivot the table
reshaped_data = all_data.pivot_table(index=['timestamp', 'cmdb_id'], columns='kpi_name', values='value').reset_index()

# Ensure the output directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Get unique cmdb_ids
cmdb_ids = reshaped_data['cmdb_id'].unique()

# Loop through unique cmdb_ids
for i, cmdb_id in enumerate(cmdb_ids):
    print(f"Processing {i+1}/{len(cmdb_ids)}: {cmdb_id}")  # Progress indicator
    
    # Filter data by cmdb_id
    cmdb_data = reshaped_data[reshaped_data['cmdb_id'] == cmdb_id].dropna(axis=1, how='all')
    
    # Save data to Excel, including 'device' in the file name if present, and ensuring it is a valid file name
    cleaned_filename = clean_filename(cmdb_id)
    cmdb_data.to_excel(os.path.join(output_path, f"{cleaned_filename}.xlsx"), index=False)
