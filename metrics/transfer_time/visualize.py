import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 定义文件路径
input_path = 'E:/github/aiops_metrics/metrics/transfer_time/cleaned_data'
output_path = 'E:/github/aiops_metrics/metrics/transfer_time/visualizations'

# 确保输出路径存在
Path(output_path).mkdir(parents=True, exist_ok=True)

# 获取输入文件夹中的所有文件
files = os.listdir(input_path)

# 遍历文件
for file in files:
    # 读取数据
    data = pd.read_excel(os.path.join(input_path, file))
    
    # 获取所有的指标列
    kpi_columns = [col for col in data.columns if col not in ['timestamp', 'cmdb_id']]
    
    # 检查是否有KPI列
    if len(kpi_columns) == 0:
        print(f"Warning: No KPI columns found in {file}. Skipping visualization generation for this file.")
        continue

    # 创建一个新的图像，其中包含多个子图
    fig, axs = plt.subplots(len(kpi_columns), 1, figsize=(10, 5*len(kpi_columns)))
    fig.suptitle(f"Visualizations for {file}", fontsize=16)
    
    # 遍历指标列并为每个指标创建一个子图
    for idx, kpi in enumerate(kpi_columns):
        # 检查无法转换的值
        non_numeric = data[pd.to_numeric(data[kpi], errors='coerce').isna()][kpi].unique()
        if len(non_numeric) > 0:
            print(f"Warning: Non-numeric values found in {file}, column {kpi}: {non_numeric}")

        # 将非数值数据转换为NaN
        data[kpi] = pd.to_numeric(data[kpi], errors='coerce')

        axs[idx].plot(data['timestamp'], data[kpi])
        axs[idx].set_title(kpi)
        axs[idx].set_xlabel('Timestamp')
        axs[idx].set_ylabel('Value')
    
    # 调整布局并保存图像
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(os.path.join(output_path, f"visualization_{Path(file).stem}.png"))
    plt.close(fig)
    print(f"Visualizations for {file} generated and saved.")
    
print("All files have been visualized and saved in the visualizations folder.")
