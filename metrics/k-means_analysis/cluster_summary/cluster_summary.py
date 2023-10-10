import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设定文件路径
files_path = 'E:/github/aiops_metrics/metrics/k-means_analysis/cluster'  # 请替换为您的文件路径

# 获取文件列表
files = os.listdir(files_path)

# 遍历文件进行分析
for file in files:
    # 读取数据
    data = pd.read_csv(os.path.join(files_path, file))
    
    # 计算描述性统计量
    stats = data.groupby('cluster').describe()
    print(f"Statistics for {file}:\n", stats)
    
    # 保存描述性统计量为CSV文件
    stats.to_csv(os.path.join(files_path, f"stats_{file}.csv"))
    
    # 可视化：箱型图
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data, x='cluster', y='kpi_name')  # 请替换为您的特征列名
    plt.title(f"Boxplot for {file}")
    plt.savefig(os.path.join(files_path, f"boxplot_{file}.png"))
    plt.close()
