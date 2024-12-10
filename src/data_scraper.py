import os
from dotenv import load_dotenv
import google.generativeai as genai
import pandas as pd

# .envファイルから環境変数を読み込む
load_dotenv()

# Gemini APIの設定
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_tweet(prompt):
    model = genai.GenerativeModel('gemini-pro')  # モデル名をGeminiに設定
    response = model.generate_content(prompt)  # プロンプトを使用してコンテンツを生成
    return response.text

def main():
    # ツイートを生成
    generated_tweets = []
    for i in range(100):
        tweet = generate_tweet("Gemini AIを使用して生成されたツイートです。")  # プロンプトをGeminiに適応
        generated_tweets.append(tweet)

    # 生成されたツイートをDataFrameに変換
    df = pd.DataFrame(generated_tweets, columns=['tweet'])

    # CSVファイルとして保存
    df.to_csv('data/raw_data/tweets.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    main()
