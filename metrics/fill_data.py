import pandas as pd

# Load the data
# NOTE: Update the path to point to your file location
data_path = "./Linux_metric_0918.csv"
data = pd.read_csv(data_path)

# Fill missing values in the 'device' column with the placeholder "Unknown"
data['device'].fillna('Unknown', inplace=True)

# Check if there are any missing values left
missing_values = data.isnull().sum()

# Print the number of missing values for each column
print("Number of missing values for each column after filling:")
print(missing_values)

# Save the filled data to a new CSV file
data.to_csv("Linux_metric_filled.csv", index=False)

print("The filled data has been saved to 'Linux_metric_filled.csv'")
