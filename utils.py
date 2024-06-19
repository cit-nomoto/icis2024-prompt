import openai
import os
from dotenv import load_dotenv

load_dotenv() # .envファイルの読み込み

def load_document(file_path): 
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    return ""

def generate_code(prompt, api_key):
    openai.api_key = api_key # APIキーの読み込み
    messages=[
        {"role": "user", "content": "pythonで書籍を管理するCLIツールを作成したいです"},
        {"role": "system", "content": "以下の開発文書に基づき、機能をすべて満たすCLIツールとして動作するpythonコードを生成してください。"},
    ]

    # 開発文書の有無に応じてメッセージを追加
    if prompt["requirements"]:
        messages.append({"role": "user", "content": f'要件定義書がこちらです {prompt["requirements"]}'})
    
    if prompt["basic"]:
        messages.append({"role": "user", "content": f'基本設計書がこちらです {prompt["basic"]}'})

    if prompt["detail"]:
        messages.append({"role": "user", "content": f'詳細設計書がこちらです {prompt["detail"]}'})
    
    # 条件設定
    messages.extend([
        {"role": "system", "content": "必ず全ての機能を実装してpythonコードを生成してください。一部機能を失くしたり、関数を省略したコードは出力しないでください"},
        {"role": "system", "content": "また、ソースコードやコメントだけを出力し、pythonコードとして動作しない説明等は一切不要です。一意のソースコードのみを出力してください"},
        {"role": "system", "content": "データのやり取りには, RDBMSとして、sqlite3を用い、必要となるテーブルなども設計してください"},
    ])

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo", #　モデル指定
            messages=messages
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e: # エラーキャッチ
        print(f"error: {e}")
        return None