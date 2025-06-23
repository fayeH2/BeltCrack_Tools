# 拆分视频为图像帧，并保存到同名文件夹中
import os
import cv2

video_path = r'G:\desktop\电子科技大学\4.课题组项目资料\2024.7《苏州瑞斯特-鞍山安泰红盾—工业传送带裂缝检测》\代码-备份\datasets  迭代\2025-02-26 裂缝数据集\original_video_pictures-原始\video55.mp4'  # 视频路径
output_folder = r'G:\desktop\test'  # 输出文件夹路径,必须为空文件夹
print("---start")


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")


frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite(os.path.join(output_folder, f'55_{frame_count}.jpg'), frame)
    frame_count += 1

print(frame_count)
print("---end")
cap.release()
