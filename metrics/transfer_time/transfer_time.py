

import os
import pandas as pd
import datetime

# 指定文件目录的路径
directory_path = 'E:/github/aiops_metrics/metrics/kpi_name_files'

# 列出目录中的所有文件
files = os.listdir(directory_path)

# 循环处理目录中的每一个文件
for file_name in files:
    # 创建完整的文件路径
    file_path = os.path.join(directory_path, file_name)
    
    # 读取文件内容
    data = pd.read_excel(file_path)  # 如果文件格式不是Excel，请使用适当的读取函数
    
    # 将时间戳列转换为pandas datetime类型
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')  # 将单位设置为秒
    
    # 从时间戳中提取新的时间特征
    data['year'] = data['timestamp'].dt.year
    data['month'] = data['timestamp'].dt.month
    data['day'] = data['timestamp'].dt.day
    data['hour'] = data['timestamp'].dt.hour
    data['minute'] = data['timestamp'].dt.minute
    data['second'] = data['timestamp'].dt.second
    data['day_of_week'] = data['timestamp'].dt.dayofweek
    data['day_of_year'] = data['timestamp'].dt.dayofyear
    
    # 保存包含新特征的数据到新的文件
    output_file_path = os.path.join('E:/github/aiops_metrics/metrics/transfer_time/after_transfer_time', file_name)
    data.to_excel(output_file_path, index=False)  # 如果你希望保存为其他格式，请使用适当的保存函数
