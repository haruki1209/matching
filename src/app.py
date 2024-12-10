from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask_cors import CORS

# .envファイルから環境変数を読み込む
load_dotenv()

# APIキーの確認
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEYが設定されていません。.envファイルを確認してください。")

# Gemini APIの設定
genai.configure(api_key=api_key)

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)
CORS(app)

def generate_response(prompt, gender):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # 応答が有効か確認
        if not response or not response.text:
            return "申し訳ありませんが、適切な応答を生成できませんでした。"

        return response.text
    
    except Exception as e:
        print(f"Error in generate_response: {str(e)}")
        return "エラーが発生しました。もう一度お試しください。"

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get('message')
        gender = data.get('gender', 'female')  # デフォルトは女性モード
        
        if not user_input:
            return jsonify({'error': 'メッセージが空です'}), 400
        
        bot_response = generate_response(user_input, gender)
        return jsonify({'response': bot_response})
    
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)