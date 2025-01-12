from flask import Flask, render_template, request, jsonify, send_from_directory
import process  # 这里需要导入你已经训练好的模型模块
import logging
import os
import mimetypes

app = Flask(__name__)

# 配置日志记录
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        app.logger.debug("Received upload request")
        video1 = request.files['video1']
        video2 = request.files['video2']
        app.logger.debug("Files received: video1=%s, video2=%s", video1.filename, video2.filename)
        
        # 确保 static 目录存在
        if not os.path.exists('static'):
            os.makedirs('static')
            app.logger.debug("Created static directory")
        
        # 保存视频文件到服务器，假设保存到 static 目录下
        video1_path = os.path.join('static', video1.filename)
        video2_path = os.path.join('static', video2.filename)
        video1.save(video1_path)
        app.logger.debug("Video1 saved to %s", video1_path)
        video2.save(video2_path)
        app.logger.debug("Video2 saved to %s", video2_path)
        
        # 调用你的模型进行处理，这里假设 your_model 是已经训练好的模型对象，且有一个 process_video 方法
        # processed_video1_path = your_model_module.process_video(video1_path)
        # app.logger.debug("Processed video1 path: %s", processed_video1_path)

        RGB_frame_folder='static/RGB_frame'
        T_frame_folder='static/T_frame'
        processed_frame_folder='static/processed_frame'
        processed_video_path='static/processed_video.mp4'

        # 首先将视频处理成一帧一帧的图片
        process.turn_video_to_frames(video1_path, RGB_frame_folder)
        process.turn_video_to_frames(video2_path, T_frame_folder)
        
        # 调用模型处理图片进行计数
        process.process_frames_with_modle(RGB_frame_folder,T_frame_folder,processed_frame_folder)

        # 将处理后的图片合成视频
        process.turn_frames_to_video(processed_frame_folder, processed_video_path, 30)

        return jsonify({'result': processed_video_path})
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/static/<filename>')
def send_video(filename):
    # return send_from_directory('static', filename, mimetype='video/mp4')
    # 动态获取文件的 MIME 类型
    mime_type, _ = mimetypes.guess_type(filename)
    return send_from_directory('static', filename, mimetype=mime_type)

if __name__ == '__main__':
    app.run(debug=True)