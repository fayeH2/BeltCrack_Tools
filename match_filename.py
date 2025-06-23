import os

def find_extra_files(folder1, folder2):
    # 获取文件夹1中所有文件的文件名（去除后缀）
    files1 = set([os.path.splitext(file)[0] for file in os.listdir(folder1)])
    # 获取文件夹2中所有文件的文件名（去除后缀）
    files2 = set([os.path.splitext(file)[0] for file in os.listdir(folder2)])

    # 找出在文件夹1中存在但在文件夹2中不存在的文件名
    extra_in_folder1 = [file + '.json' for file in files1 - files2]
    # 找出在文件夹2中存在但在文件夹1中不存在的文件名
    extra_in_folder2 = [file + '.txt' for file in files2 - files1]

    return extra_in_folder1, extra_in_folder2

# 定义两个文件夹的路径
folder2 = r'G:\desktop\电子科技大学\4.课题组项目资料\2024.7《苏州瑞斯特-鞍山安泰红盾—工业传送带裂缝检测》\代码-备份\datasets  迭代\2024-10-24 裂缝数据集\实际使用\json'
folder1 = r'G:\desktop\电子科技大学\4.课题组项目资料\2024.7《苏州瑞斯特-鞍山安泰红盾—工业传送带裂缝检测》\代码-备份\datasets  迭代\2024-10-24 裂缝数据集\pictures'

# 调用函数找出多余的文件
extra_json, extra_txt = find_extra_files(folder1, folder2)

# 输出结果
print("JSON文件夹中多余的文件:")
for file in extra_json:
    print(file)

print("\nTXT文件夹中多余的文件:")
for file in extra_txt:
    print(file)