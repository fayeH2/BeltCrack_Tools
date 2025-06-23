import os

def rename_files(folder_path, prefix):
    # 获取文件夹中所有文件的名称，并按字典顺序排序
    file_names = sorted(os.listdir(folder_path))
    for index, file_name in enumerate(file_names):
        # 分离文件名和文件后缀
        name, extension = os.path.splitext(file_name)
        # 生成新的文件名
        new_name = f"{prefix}{index}{extension}"
        # 拼接文件的完整旧路径和新路径
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # 重命名文件
        os.rename(old_file_path, new_file_path)

# 请将此路径替换为你实际的文件夹路径
folder_path = r"G:\desktop\电子科技大学\4.课题组项目资料\2024.7《苏州瑞斯特-鞍山安泰红盾—工业传送带裂缝检测》\代码-备份\datasets  迭代\2025-02-16 裂缝数据集\crack_20000\tmp(match)"
# 重命名的前缀
prefix = "pic"
rename_files(folder_path, prefix)