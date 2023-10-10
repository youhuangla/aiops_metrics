import pandas as pd

# Load the data
# NOTE: Update the path to point to your file location
data_path = "./Linux_metric_0918.csv"
data = pd.read_csv(data_path)

# Check for missing values in the data
missing_values = data.isnull().sum()

# Print the number of missing values for each column
print("Number of missing values for each column:")
print(missing_values)

# Save the missing values count to an Excel file
missing_values.to_excel("missing_values_count.xlsx", sheet_name="Missing Values", header=True)

print("The missing values count has been saved to 'missing_values_count.xlsx'")
