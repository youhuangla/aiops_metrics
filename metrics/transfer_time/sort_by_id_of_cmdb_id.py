import os
import shutil

# 定义路径
input_path = 'E:/github/aiops_metrics/metrics/transfer_time/cleaned_data'
output_path = 'E:/github/aiops_metrics/metrics/transfer_time/sorted_by_id_data'

# 获取所有文件
files = os.listdir(input_path)

# 遍历文件
for file in files:
    # 获取文件前缀，假设使用下划线"_"分割
    prefix = file.split('_')[0]
    
    # 创建对应的子目录（如果不存在）
    subdir_path = os.path.join(output_path, prefix)
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)
    
    # 移动文件
    shutil.move(os.path.join(input_path, file), os.path.join(subdir_path, file))
