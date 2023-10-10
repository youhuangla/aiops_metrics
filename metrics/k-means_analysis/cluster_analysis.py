

import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# NOTE: Update the path to point to your files location
files_path = 'E:/github/aiops_metrics/metrics/kpi_name_files'
files = os.listdir(files_path)

# Get the total number of files for progress indication
total_files = len(files)

# Loop through all files
for i, file in enumerate(files):
    # Print progress
    print(f"Processing file {i+1}/{total_files}: {file}")
    
    # Load data
    data = pd.read_excel(os.path.join(files_path, file))
    
    # Data preprocessing (e.g., handle missing values, standardization)
    # ...
    
    # Extract the 'value' column and standardize it
    X = data[['value']]
    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)
    
    # K-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X_std)
    
    # Add clustering results back to the original data
    data['cluster'] = kmeans.labels_
    
    # Save results or generate visualizations
    # ...
    # For instance, save the dataframe with clusters to a new csv file
    data.to_csv(f"E:/github/aiops_metrics/metrics/k-means_analysis/cluster/clustered_{file}", index=False)
