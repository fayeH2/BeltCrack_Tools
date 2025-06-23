import os
import re

# 定义主文件夹路径
root_folder = r'G:\desktop\crackS\json'  # 替换为你的主文件夹路径

def windows_sort_key(filename):
    # 提取数字部分
    parts = re.split(r'(\d+)', filename)
    # 将数字部分转换为整数，其他部分保持原样
    return [int(part) if part.isdigit() else part for part in parts]

# 遍历主文件夹中的所有子文件夹
for foldername, subfolders, filenames in os.walk(root_folder):
    # 获取当前子文件夹中的所有JPG文件
    jpg_files = [f for f in filenames if f.lower().endswith('.json')]
    
    # 按照Windows的排序规则对JPG文件进行排序
    jpg_files.sort(key=lambda x: windows_sort_key(x))
    
    # 重命名JPG文件
    for index, filename in enumerate(jpg_files):
        # 构造新的文件名，格式为 "序号.jpg"
        new_filename = f"{index}.json"
        # 构造完整的旧路径和新路径
        old_file_path = os.path.join(foldername, filename)
        new_file_path = os.path.join(foldername, new_filename)
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f'文件 {filename} 已重命名为 {new_filename} 在文件夹 {foldername}')

print('所有文件已重新命名完成！')