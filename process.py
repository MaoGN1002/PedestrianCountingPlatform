import cv2
import os

def turn_video_to_frames(video_path,output_folder):
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



def process_frames_with_modle(RGB_folder,T_folder, output_folder):
    #  暂时按照给RGB图片每一帧右上角添加一个1做替代，实际后期是调用模型进行处理

    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 获取文件夹中的所有文件
    file_list = os.listdir(RGB_folder)
    label='1'
    for file_name in file_list:
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            # 读取图片
            image_path = os.path.join(RGB_folder, file_name)
            image = cv2.imread(image_path)
            # 获取图片的高度和宽度
            height, width, _ = image.shape
            # 设置字体
            font = cv2.FONT_HERSHEY_SIMPLEX
            # 字体大小
            font_scale = 1
            # 字体颜色（白色）
            color = (255, 255, 255)
            # 字体厚度
            thickness = 2
            # 在图片右上角添加标签
            cv2.putText(image, label, (width - 100, 50), font, font_scale, color, thickness, cv2.LINE_AA)
            # 构建新的保存路径
            new_image_path = os.path.join(output_folder, file_name)
            # 保存修改后的图片
            cv2.imwrite(new_image_path, image)
            
# if __name__ == "__main__":
#     process_frames_with_modle("RGB_frame", "label", 'processed_frame')

def turn_frames_to_video(image_folder, video_name, fps):
    # 存储图片的列表
    images = []
    index = 1
    while True:
        img_name = str(index) + ".jpg"  # 假设图片都是以数字命名，且后缀为.jpg
        img_path = os.path.join(image_folder, img_name)
        if os.path.exists(img_path):
            images.append(img_name)
            index += 1
        else:
            break
    # 获取第一张图片的尺寸信息
    if len(images) > 0:
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape
    else:
        raise ValueError("No images found in the specified folder.")

    # 创建视频对象
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'avc1'), fps, (width, height))

    for image in images:
        # 读取图片
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)
        # 将图片添加到视频中
        video.write(img)

    # 释放视频对象
    video.release()




