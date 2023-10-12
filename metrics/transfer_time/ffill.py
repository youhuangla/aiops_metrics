# ffill and backfill
import os
import pandas as pd

# 定义文件路径
input_path = 'E:/github/aiops_metrics/metrics/transfer_time/cleaned_data'

# 获取所有的excel文件
files = [f for f in os.listdir(input_path) if f.endswith('.xlsx')]

# 遍历所有文件
for file in files:
    # 读取Excel文件
    df = pd.read_excel(os.path.join(input_path, file))
    
    # 使用前向填充，然后使用后向填充
    df = df.fillna(method='ffill').fillna(method='bfill')
    
    # 保存处理过的数据到原文件
    df.to_excel(os.path.join(input_path, file), index=False)

    print(f"Processed {file}")
