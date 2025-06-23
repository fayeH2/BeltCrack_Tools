 
from PIL import Image
import os
 
# img = Image.open('D:/torch1/unet-pytorch-main/myimgs/3.jpg')
# print(img.mode)
# # 若是四通道则将其改为三通道
# if img.mode == "RGBA":img = img.convert('RGB')
# img.save('D:/torch1/unet-pytorch-main/datasets/before/3.jpg')
 
 
 
path = r"G:\desktop\电子科技大学\4.课题组项目资料\2024.7《苏州瑞斯特-鞍山安泰红盾—工业传送带裂缝检测》\代码-备份\datasets  迭代\2024-8-14 裂缝数据集\crack_10000\pictures"  # 最后要加双斜杠，不然会报错
filelist = os.listdir(path)
 
for file in filelist:
    whole_path = os.path.join(path, file)
    img = Image.open(whole_path)  # 打开图片img = Image.open(dir)#打开图片
    if img.mode == "RGBA":img = img.convert('RGB')
    save_path = r'G:\desktop\电子科技大学\4.课题组项目资料\2024.7《苏州瑞斯特-鞍山安泰红盾—工业传送带裂缝检测》\代码-备份\datasets  迭代\2024-8-14 裂缝数据集\crack_10000\test/'
    # img.save(save_path + img1)
    img.save(save_path + file)