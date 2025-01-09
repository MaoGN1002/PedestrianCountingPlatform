from flask import Flask, request, render_template, jsonify, send_from_directory
import your_model_module  # 这里需要导入你已经训练好的模型模块
import logging
import os

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
        visible_image = request.files['visible_image']
        infrared_image = request.files['infrared_image']
        app.logger.debug("Files received: visible_image=%s, infrared_image=%s", visible_image.filename, infrared_image.filename)
        
        # 确保 static 目录存在
        if not os.path.exists('static'):
            os.makedirs('static')
            app.logger.debug("Created static directory")


        # 保存图像文件到服务器，假设保存到 static 目录下
        visible_image_path = f'static/{visible_image.filename}'
        infrared_image_path = f'static/{infrared_image.filename}'
        visible_image.save(visible_image_path)
        app.logger.debug("Visible image saved to %s", visible_image_path)
        infrared_image.save(infrared_image_path)
        app.logger.debug("Infrared image saved to %s", infrared_image_path)
        # 调用你的模型进行处理，这里假设 your_model 是已经训练好的模型对象，且有一个 predict 方法
        result = your_model_module.predict(visible_image_path, infrared_image_path)
        app.logger.debug("Prediction result: %s", result)
        return jsonify({'result': result})
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/static/<filename>')
def send_image(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)