# 非序列文件夹，严格coco格式
import os
import shutil

def reformat_images(src_root, dst_root):
    """
    将源目录下所有子文件夹中的图片重新命名并复制到目标目录
    :param src_root: 源图片根目录（包含data1,data2等子文件夹）
    :param dst_root: 目标目录（所有图片直接存放在此）
    """
    # 确保目标目录存在
    os.makedirs(dst_root, exist_ok=True)
    
    # 遍历所有子文件夹
    for folder_name in os.listdir(src_root):
        data_folder = os.path.join(src_root, folder_name)
        
        # 只处理目录且符合data前缀格式
        if os.path.isdir(data_folder) and folder_name.startswith("data"):
            print(f"Processing folder: {folder_name}")
            
            # 遍历子文件夹中的文件
            for filename in os.listdir(data_folder):
                src_path = os.path.join(data_folder, filename)
                
                if os.path.isfile(src_path):
                    # 分割文件名和扩展名
                    name_part, ext = os.path.splitext(filename)
                    
                    try:
                        # 生成新文件名（保留原始编号格式）
                        new_name = f"{folder_name}-{name_part}{ext}"
                        dst_path = os.path.join(dst_root, new_name)
                        
                        # 复制并保留元数据
                        shutil.copy2(src_path, dst_path)
                        
                    except Exception as e:
                        print(f"Error processing {src_path}: {str(e)}")

if __name__ == "__main__":
    # 配置路径（根据实际情况修改）
    SOURCE_DIR = "/home/hjh/crackBase/crackS/images/train"
    DEST_DIR = "/home/hjh/crackBase/crackS_all/train"
    
    # 执行转换
    reformat_images(SOURCE_DIR, DEST_DIR)
    print("All images reformatted successfully!")