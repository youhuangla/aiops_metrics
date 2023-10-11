import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# NOTE: Update the path to point to your files location
files_path = 'E:/github/aiops_metrics/metrics/transfer_time/after_transfer_time'
output_path = 'E:/github/aiops_metrics/metrics/changing_trend/trend'
files = os.listdir(files_path)

# Get the total number of files for progress indication
total_files = len(files)

# Loop through all files
for i, file in enumerate(files):
    # Print progress
    print(f"Processing file {i+1}/{total_files}: {file}")
    
    # Load data
    data = pd.read_excel(os.path.join(files_path, file))
    
    # Extract 'hour' and 'minute' from 'timestamp'
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['hour'] = data['timestamp'].dt.hour
    data['minute'] = data['timestamp'].dt.minute
    
    # Choose features for clustering
    features = ['hour', 'minute', 'value']
    
    # Standardize the features
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[features])
    
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=0).fit(data_scaled)
    
    # Add cluster labels to the original data
    data['cluster'] = kmeans.labels_
    
    # Plotting the value over time
    plt.plot(data['timestamp'], data['value'])
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title(f'Value over time for {file}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, f"time_series_plot_{file.replace('.xlsx', '.png')}"))
    plt.close()
    
    # Save the data with cluster labels
    data.to_excel(os.path.join(output_path, f"clustered_{file}"), index=False)
