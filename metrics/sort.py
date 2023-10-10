import os
import pandas as pd

# Load the data
data_path = "./Linux_metric_0918.csv"  # Update the path to your file
data = pd.read_csv(data_path)

# Get unique kpi_names
unique_kpi_names = data['kpi_name'].unique()

# Create a directory to store the Excel files
output_dir = "kpi_name_files"
os.makedirs(output_dir, exist_ok=True)

# Save each subset of the data as an Excel file
for kpi in unique_kpi_names:
    # Get the subset of the data
    subset_data = data[data['kpi_name'] == kpi]
    
    # Replace "/" in kpi name to avoid issues with file paths
    filename = kpi.replace("/", "_")
    
    # Save the subset data as an Excel file
    subset_data.to_excel(os.path.join(output_dir, f"{filename}.xlsx"), index=False)

print("Files have been saved.")
