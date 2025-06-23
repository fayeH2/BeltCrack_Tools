
import os
import shutil

# 定义源文件夹和目标文件夹路径
json_folder = r'G:\desktop\电子科技大学\4.课题组项目资料\2024.7《苏州瑞斯特-鞍山安泰红盾—工业传送带裂缝检测》\代码-备份\datasets  迭代\2025-02-16 裂缝数据集\crack_20000\json'  # JSON文件所在的文件夹路径
crack_s_folder = r'G:\desktop\crack_d'
 # crack_s文件夹路径

# 遍历crack_s文件夹中的images文件夹
images_folder = os.path.join(crack_s_folder, 'images')
data_folders = [d for d in os.listdir(images_folder) if d.startswith('data')]

# 遍历每个data文件夹中的jpg文件
for data_folder in data_folders:
    data_path = os.path.join(images_folder, data_folder)
    jpg_files = [f for f in os.listdir(data_path) if f.endswith('.jpg')]
    
    # 创建对应的json文件夹
    target_json_folder = os.path.join(json_folder, data_folder)
    if not os.path.exists(target_json_folder):
        os.makedirs(target_json_folder)
    
    # 匹配json文件并复制
    for jpg_file in jpg_files:
        jpg_name = os.path.splitext(jpg_file)[0]  # 获取不带后缀的文件名
        json_file = f'{jpg_name}.json'
        json_path = os.path.join(json_folder, json_file)
        
        # 如果找到匹配的json文件，则复制到目标文件夹
        if os.path.exists(json_path):
            shutil.copy(json_path, os.path.join(target_json_folder, json_file))
            print(f'复制文件：{json_file} 到 {target_json_folder}')
        else:
            print(f'未找到匹配的json文件：{json_file}')

print('批量复制完成！')