import cv2


def process_video(video_path):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    # 获取原始视频的帧率、宽度和高度
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 定义输出视频的编解码器
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    # 创建输出视频对象，设置输出路径、编解码器、帧率、分辨率
    # out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))
    processed_video_path = video_path.replace(".mp4", "_output.mp4")
    out = cv2.VideoWriter(processed_video_path, fourcc, fps, (width, height))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # 在每一帧的右上角添加数字 1
        cv2.putText(frame, '1', (width - 50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        # 写入处理后的帧到输出视频
        out.write(frame)
    # 释放视频对象
    cap.release()
    out.release()

    return processed_video_path


