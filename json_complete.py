import json
import os
from pathlib import Path

def update_coco_json_paths(json_path, output_path=None):
    """
    更新COCO格式JSON文件中images的file_name路径
    :param json_path: 原始JSON文件路径
    :param output_path: 输出文件路径（默认覆盖原文件）
    """
    # 定义新旧路径前缀
    old_base = "/home/hjh/crackBase/crackD/images/val/"
    new_base = "/home/hjh/crackBase/crackD_all/val"
    
    # 读取原始JSON文件
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # 处理每个image条目
    for img in data['images']:
        original_path = img['file_name']
        
        # 验证路径格式是否符合预期
        if not original_path.startswith(old_base):
            print(f"警告：路径 {original_path} 不符合旧基础路径，已跳过")
            continue
        
        # 提取相对路径部分（如 "data1/0.jpg"）
        relative_part = original_path[len(old_base):]
        
        # 分割子文件夹和文件名（处理多层目录情况）
        parts = relative_part.split('/')
        if len(parts) < 2:
            print(f"警告：路径 {relative_part} 结构不符合预期，已跳过")
            continue
            
        # 合并子文件夹和文件名（如 data1-0.jpg）
        new_filename = '-'.join(parts)
        
        # 构建新路径
        new_path = os.path.join(new_base, new_filename)
        img['file_name'] = new_path

    # 设置默认输出路径（覆盖原文件）
    if output_path is None:
        output_path = json_path
    
    # 确保输出目录存在
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    # 写回更新后的JSON文件
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"处理完成！已保存至：{output_path}")

if __name__ == "__main__":
    # 输入文件路径
    input_json = "/home/hjh/crackBase/annotations/D/val/coco.json"
    
    # 输出路径（设置为None则覆盖原文件，建议先测试时可指定新路径）
    output_json = "/home/hjh/crackBase/crackD_all/coco_val.json"
    
    # 执行处理
    update_coco_json_paths(input_json, output_json)