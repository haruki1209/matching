import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルから環境変数を読み込む
load_dotenv()

# Gemini APIの設定
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response_with_gemini(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')  # モデル名をGeminiに設定
        response = model.generate_content(prompt)  # プロンプトを使用してコンテンツを生成
        return response.text
    except Exception as e:
        print(f"Error in generate_response_with_gemini: {str(e)}")
        return "エラーが発生しました。もう一度お試しください。"