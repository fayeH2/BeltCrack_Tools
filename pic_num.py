# 检查文件夹中 递归深入检查 其中的jpg格式文件的数量

import os

def count_jpg_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                count += 1
    return count

directory = r"G:\desktop\crackD\json\test"  # 替换为你的文件夹路径
jpg_count = count_jpg_files(directory)
print(f"文件夹中包含 {jpg_count} 个 .json 文件。")