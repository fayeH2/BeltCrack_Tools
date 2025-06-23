import os
import shutil

# 定义文件夹路径
json_folder = r"G:\desktop\test\4"  # json文件夹路径
pictures_folder = r"G:\desktop\crack_d\images\data6"  # jpg文件夹路径
output_folder = r"G:\desktop\tmp(pic)\4"  # 输出的tmp文件夹路径

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取json文件夹中所有文件的文件名（不含后缀）
json_files = [os.path.splitext(file)[0] for file in os.listdir(json_folder) if file.endswith('.json')]

# 遍历jpg文件夹，筛选出对应的jpg文件并复制到tmp文件夹
for file in os.listdir(pictures_folder):
    if file.endswith('.jpg'):
        # 获取文件名（不含后缀）
        jpg_name = os.path.splitext(file)[0]
        # 如果jpg文件名在json文件名列表中，则复制到tmp文件夹
        if jpg_name in json_files:
            source_path = os.path.join(pictures_folder, file)
            target_path = os.path.join(output_folder, file)
            shutil.copy2(source_path, target_path)
            print(f"Copied: {file}")

print("Finished copying files.")