import os
import re
import shutil

# 定义路径
base_path = 'E:/GITHUB/AIOPS_METRICS/METRICS/TRANSFER_TIME/SORTED_BY_ID_DATA'

# 获取所有子目录
subdirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

# 遍历每个子目录
for subdir in subdirs:
    subdir_path = os.path.join(base_path, subdir)
    
    # 获取子目录中的所有文件
    files = os.listdir(subdir_path)
    
    # 遍历每个文件
    for file in files:
        # 使用正则表达式查找文件名中的数字
        match = re.search(r'_(\d+)', file)
        
        # 如果找到数字，使用它来创建/选择子目录
        if match:
            number = match.group(1)
            new_subdir_path = os.path.join(subdir_path, number)
            
            # 如果新子目录不存在，则创建它
            if not os.path.exists(new_subdir_path):
                os.makedirs(new_subdir_path)
            
            # 移动文件到新子目录
            shutil.move(os.path.join(subdir_path, file), os.path.join(new_subdir_path, file))
        else:
            print(f"Warning: No number found in filename {file}. File is not moved.")
