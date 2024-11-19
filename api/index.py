from flask import Flask, jsonify
from app.routes.api import api_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API"})

# 这个变量会被 Vercel 使用
application = app

if __name__ == '__main__':
    app.run(debug=True)