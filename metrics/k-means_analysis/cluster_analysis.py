

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

import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. 加载数据
# 指定文件目录的路径
files_path = 'E:/github/aiops_metrics/metrics/kpi_name_files'
files = os.listdir(files_path)

# 循环处理目录中的每一个文件
for file_name in files:
    # 创建完整的文件路径
    file_path = os.path.join(files_path, file_name)
    
    # 读取文件内容
    data = pd.read_excel(file_path)
    
    # 2. 特征工程: 从时间戳中提取小时和分钟
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['hour'] = data['timestamp'].dt.hour
    data['minute'] = data['timestamp'].dt.minute
    
    # 选择要用于聚类的特征
    features = ['hour', 'minute', 'value']
    
    # 3. 数据预处理: 对特征进行标准化
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[features])
    
    # 4. 聚类: 使用K-Means进行聚类
    kmeans = KMeans(n_clusters=3, random_state=0).fit(data_scaled)
    
    # 将聚类标签添加回原始数据中
    data['cluster'] = kmeans.labels_
    
    # 5. 分析结果: 可视化聚类结果
    plt.scatter(data['hour'], data['value'], c=data['cluster'], cmap='viridis')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Value')
    plt.title(f'K-Means Clustering of {file_name}')
    plt.colorbar(label='Cluster Label')
    plt.show()
