import cv2
import os

video_path = 'test111.mp4'
output_folder = 'frame'

if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 打开视频文件
cap = cv2.VideoCapture(video_path)
# 用于存储帧的序号
frame_count = 0
while True:
    # 读取视频的下一帧
    ret, frame = cap.read()
    if ret:
        # 构建保存帧的文件名
        frame_name = os.path.join(output_folder, f"{frame_count + 1}.jpg")
        # 保存帧为图片
        cv2.imwrite(frame_name, frame)
        frame_count += 1
    else:
        break
# 释放视频对象
cap.release()
