import os
import pandas as pd

# Directory where your Excel files are stored
files_dir = "kpi_name_files"

# Create an empty DataFrame to store the descriptive statistics
desc_stats = pd.DataFrame()

# Get the list of files
files = [f for f in os.listdir(files_dir) if f.endswith(".xlsx")]

# Loop through all Excel files in the directory
for i, filename in enumerate(files, start=1):
    # Load the data
    file_path = os.path.join(files_dir, filename)
    data = pd.read_excel(file_path)
        
    # Calculate descriptive statistics
    stats = data['value'].describe()
        
    # Add the kpi_name to the stats
    stats['kpi_name'] = filename.replace(".xlsx", "")
        
    # Append the stats to the desc_stats DataFrame
    desc_stats = desc_stats.append(stats, ignore_index=True)
    
    # Print the progress
    print(f"Processing file {i} of {len(files)}: {filename}")

# Save the descriptive statistics as a new Excel file
desc_stats.to_excel("descriptive_statistics_by_kpi_name.xlsx", index=False)

print("Descriptive statistics have been saved.")
