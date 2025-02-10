# Todo App

シンプルな To-Do リストアプリです。  
タスクの追加・削除・編集、完了/未完了の切り替えができます。  
Flask を使用してバックエンドを構築し、HTML/CSS/JavaScript でフロントエンドを作成しています。

## 機能

✅ タスクの追加・削除・編集  
✅ タスクの完了/未完了の切り替え  
✅ 期限・タグを設定してタスク管理  
✅ データは JSON ファイルに保存  

## 使用技術

- **フロントエンド**: HTML, CSS, JavaScript  
- **バックエンド**: Python (Flask)  
- **データ保存**: JSON ファイル  

## ファイル構成

todo-app/ │── static/ # 静的ファイル (CSS, JS) │ ├── styles.css # スタイルシート │ ├── script.js # クライアント側の処理 │── templates/ # HTML テンプレート │ ├── index.html # メイン画面 │── data/ # タスクデータ保存用 │ ├── tasks.json # タスクデータ (初回実行時に作成) │── app.py # Flask アプリケーション │── requirements.txt # 必要なパッケージ一覧 │── README.md # このファイル


## セットアップ & 実行方法

1. **リポジトリをクローン**
   ```sh
   git clone https://github.com/あなたのユーザー名/todo-app.git
   cd todo-app

2. 仮想環境を構築（推奨）

python -m venv venv
source venv/Scripts/activate  # Windows の場合
source venv/bin/activate      # Mac/Linux の場合

3. 依存パッケージをインストール

pip install -r requirements.txt

4. アプリを実行

python app.py

5. ブラウザで開く

http://127.0.0.1:5000/ にアクセス


## 開発者
[Kazuki-Takayama777]

## ライセンス
MIT License
