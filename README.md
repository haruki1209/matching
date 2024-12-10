# プロジェクトのセットアップ

## 仮想環境のセットアップ

1. **仮想環境の作成**:
   ```bash
   python -m venv myenv
   ```

2. **仮想環境のアクティベート**:
   - Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

3. **必要なパッケージのインストール**:
   ```bash
   pip install -r requirements.txt
   ```

## アプリケーションの実行

1. **Flaskアプリケーションの起動**:
   ```bash
   python src/app.py
   ```

2. **ブラウザでアプリケーションにアクセス**:
   - URL: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## テンプレートの実装

- `templates/chat.html`は、ユーザーがメッセージを入力し、AIと対話するためのインターフェースを提供します。以下のコードを使用して、`chat.html`を実装します。
