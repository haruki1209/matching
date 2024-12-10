import pandas as pd
import re

# ツイートデータのクリーンアップ関数
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # URLを削除
    text = re.sub(r'@\w+', '', text)  # メンションを削除
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # 特殊文字を削除
    text = text.lower()  # 小文字に変換
    return text

# 生成されたデータの読み込み
df_generated_tweets = pd.read_csv('data/generated_data/generated_tweets.csv')

# クリーンアップ処理
df_generated_tweets['Cleaned_Tweet'] = df_generated_tweets['Tweet'].apply(clean_text)

# 最終的なデータセットを保存
df_generated_tweets.to_csv('data/cleaned_data/cleaned_generated_tweets.csv', index=False)

# 最初の数行を表示
df_generated_tweets.head()
