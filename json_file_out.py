# 从json文件夹中根据内容 筛选我想要的json文件
import os
import json
import shutil
import re

# 定义源文件夹路径
tmp_folder = r'G:\desktop\tmp(json)'  # 替换为你的tmp文件夹路径

# 遍历tmp文件夹中的所有文件
for filename in os.listdir(tmp_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(tmp_folder, filename)
        
        # 读取JSON文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print(f"文件 {filename} 不是有效的JSON文件，跳过。")
                continue
        
        # 检查是否存在'imagePath'键
        if 'imagePath' in data:
            image_path = data['imagePath']
            
            # 使用正则表达式匹配格式
            match = re.match(r'\.\.\\pictures\\(\d+)_(\d+)\.jpg', image_path)
            if match:
                # 提取序号1和序号2
                number1, number2 = match.groups()
                
                # 创建以序号1命名的文件夹
                target_folder = os.path.join(tmp_folder, number1)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # 生成新的文件名
                new_filename = f'{number1}_{number2}.json'
                new_file_path = os.path.join(target_folder, new_filename)
                
                # 复制文件
                shutil.copy(file_path, new_file_path)
                print(f'文件 {filename} 已复制到 {new_file_path}')
            else:
                print(f"文件 {filename} 的'imagePath'值不符合格式，跳过。")
        else:
            print(f"文件 {filename} 中没有'imagePath'键，跳过。")

print('处理完成！')