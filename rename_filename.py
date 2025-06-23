import os
import re

# 定义主文件夹路径
root_folder = r'G:\desktop\crackS\json'  # 替换为你的主文件夹路径

def windows_sort_key(foldername):
    # 提取数字部分
    parts = re.split(r'(\d+)', foldername)
    # 将数字部分转换为整数，其他部分保持原样
    return [int(part) if part.isdigit() else part for part in parts]

# 获取主文件夹中的所有子文件夹
subfolders = [f for f in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, f))]

# 按照Windows的排序规则对子文件夹进行排序
subfolders.sort(key=lambda x: windows_sort_key(x))

# 重命名子文件夹
for index, foldername in enumerate(subfolders):
    # 构造新的文件夹名，格式为 "data序号"
    new_foldername = f"data{index + 1}"
    # 构造完整的旧路径和新路径
    old_folder_path = os.path.join(root_folder, foldername)
    new_folder_path = os.path.join(root_folder, new_foldername)
    # 重命名文件夹
    os.rename(old_folder_path, new_folder_path)
    print(f'文件夹 {foldername} 已重命名为 {new_foldername}')

print('所有文件夹已重新命名完成！')