from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask_cors import CORS

# .envファイルから環境変数を読み込む
load_dotenv()

# Gemini APIの設定
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__, template_folder='templates')  # テンプレートフォルダを指定
CORS(app)  # CORSを有効にする

def generate_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    bot_response = generate_response(user_input)
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)