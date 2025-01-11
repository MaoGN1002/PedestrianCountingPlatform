import cv2
import os


def images_to_video(image_folder, video_name, fps):
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


if __name__ == "__main__":
    image_folder = 'processed_frame'
    video_name = 'output_vide666o.mp4'
    fps = 30  # 帧率，可以根据需要调整
    images_to_video(image_folder, video_name, fps)




# import cv2
# import os


# def images_to_video(image_folder, video_name, fps):
#     # 获取文件夹中所有的图片文件，并按文件名排序
#     images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
#     images.sort()
#     # 读取第一张图片，获取尺寸信息
#     frame = cv2.imread(os.path.join(image_folder, images[0]))
#     height, width, layers = frame.shape

#     # 创建视频对象，使用 avc1 编码
#     video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'avc1'), fps, (width, height))

#     for image in images:
#         # 读取图片
#         img_path = os.path.join(image_folder, image)
#         img = cv2.imread(img_path)
#         # 将图片添加到视频中
#         video.write(img)

#     # 释放视频对象
#     video.release()


# if __name__ == "__main__":
#     image_folder = 'processed_frame'
#     video_name = 'output_video1.mp4'
#     fps = 30  # 帧率，可以根据需要调整
#     images_to_video(image_folder, video_name, fps)