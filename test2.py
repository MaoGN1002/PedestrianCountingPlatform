import cv2
import os


def add_label_to_images(folder_path, label, output_folder):
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 获取文件夹中的所有文件
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            # 读取图片
            image_path = os.path.join(folder_path, file_name)
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


if __name__ == "__main__":
    folder_path = 'frame'
    label = '1'
    output_folder = 'processed_frame'
    add_label_to_images(folder_path, label, output_folder)