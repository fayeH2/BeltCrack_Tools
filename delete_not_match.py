import os

# 删除多余的jpg文件


def remove_unmatched_jpgs(jpg_dir, txt_dir):
    # 获取txt文件夹中所有文件的名称（不含扩展名）
    txt_files = set()
    for file in os.listdir(txt_dir):
        if file.endswith('.json'):
            # 添加文件名（不含扩展名）到集合中
            txt_files.add(os.path.splitext(file)[0])

    # 遍历jpg文件夹中的所有文件
    for file in os.listdir(jpg_dir):
        if file.endswith('.jpg'):
            # 获取文件名（不含扩展名）
            file_name_without_ext = os.path.splitext(file)[0]
            # 检查文件名是否存在于txt_files集合中
            if file_name_without_ext not in txt_files:
                # 如果不存在，删除该JPG文件
                file_path = os.path.join(jpg_dir, file)
                print(f"Deleting {file_path}...")
                os.remove(file_path)

if __name__ == "__main__":
    jpg_dir = r'G:\desktop\crack_d\images\data20'  # JPG文件文件夹路径
    txt_dir = r'G:\desktop\crack_d\json\data20'  # TXT文件文件夹路径

    # 调用函数
    remove_unmatched_jpgs(jpg_dir, txt_dir)