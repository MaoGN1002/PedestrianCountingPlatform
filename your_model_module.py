import cv2
import os
import numpy as np

def process_video(video_path):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception("Could not open video file")

    # 获取视频的帧率和尺寸
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建一个 VideoWriter 对象，用于保存处理后的视频
    processed_video_path = video_path.replace(".mp4", "_processed.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用 mp4v 编解码器
    out = cv2.VideoWriter(processed_video_path, fourcc, fps, (width, height))

    if not out.isOpened():
        raise Exception("Could not open VideoWriter")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 在每一帧的右上角添加一个 "1"
        frame=frame.astype(np.uint8)
        cv2.putText(frame, "1", (width - 50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # 写入处理后的帧
        out.write(frame)

    # 释放资源
    cap.release()
    out.release()

    return processed_video_path