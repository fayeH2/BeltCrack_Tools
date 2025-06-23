import os
import random
import shutil

def collect_leaf_jpg_files(root_dir):
    """收集所有叶子目录中的JPG文件"""
    leaf_jpg_files = []
    for current_dir, subdirs, files in os.walk(root_dir):
        if not subdirs:  # 叶子目录判断
            for file in files:
                if file.lower().endswith('.jpg'):
                    leaf_jpg_files.append(os.path.join(current_dir, file))
    return leaf_jpg_files

def copy_random_files(src_files, dest_dir, num_files=1000):
    """随机复制文件到目标目录（扁平结构+新文件名）"""
    if not src_files:
        print("没有找到任何JPG文件。")
        return 0
    
    os.makedirs(dest_dir, exist_ok=True)  # 创建目标目录
    selected = random.sample(src_files, min(num_files, len(src_files)))
    
    duplicate_counter = {}  # 处理重复文件名
    copied_count = 0
    
    for src_path in selected:
        # 获取父目录名和原始文件名
        parent_name = os.path.basename(os.path.dirname(src_path))
        original_name = os.path.basename(src_path)
        
        # 生成新文件名
        new_name = f"{parent_name}_{original_name}"
        
        # 处理重复文件名
        if new_name in duplicate_counter:
            duplicate_counter[new_name] += 1
            base, ext = os.path.splitext(new_name)
            new_name = f"{base}_{duplicate_counter[new_name]}{ext}"
        else:
            duplicate_counter[new_name] = 0
        
        # 执行复制
        dest_path = os.path.join(dest_dir, new_name)
        shutil.copy2(src_path, dest_path)
        copied_count += 1
    
    return copied_count

if __name__ == "__main__":
    PIC_ROOT = r'G:\desktop\crackD\images'
    TMP_ROOT = r'G:\desktop\crackD\tmp'
    
    jpg_files = collect_leaf_jpg_files(PIC_ROOT)
    copied = copy_random_files(jpg_files, TMP_ROOT)
    
    print(f"操作完成！成功复制 {copied} 个文件到 {TMP_ROOT} 目录。")
    if len(jpg_files) < 1000:
        print(f"警告：仅找到 {len(jpg_files)} 个JPG文件，不足1000个。")