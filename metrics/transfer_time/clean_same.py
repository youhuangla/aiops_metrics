import os
import pandas as pd

# 定义文件路径
input_path = 'E:/github/aiops_metrics/metrics/transfer_time/sorted_data'
output_path = 'E:/github/aiops_metrics/metrics/transfer_time/cleaned_data'

# 确保输出路径存在
if not os.path.exists(output_path):
    os.makedirs(output_path)

# 获取输入文件夹中的所有文件
files = os.listdir(input_path)

# 遍历文件
for file in files:
    # 读取数据
    data = pd.read_excel(os.path.join(input_path, file))
    
    # 找到所有值相同的列并删除它们
    for col in data.columns:
        if data[col].nunique() == 1:
            data = data.drop(col, axis=1)
    
    # 保存清理过的数据到新的文件夹
    data.to_excel(os.path.join(output_path, file), index=False)
    print(f"Processed and saved: {file}")

print("All files have been processed and saved in the cleaned data folder.")
