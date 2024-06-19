# 本当に開発文書が段階的に読み込めているかテスト
# main.pyのfrom utilsをtest_utilsに変更
# 適当な文字を入れたテキストファイルを代替として読み込ませよう


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
        {"role": "system", "content": "以下の文字をつなげてください"},
    ]

    # 開発文書の有無に応じてメッセージを追加
    if prompt["requirements"]:
        messages.append({"role": "user", "content": f'1文字目 {prompt["requirements"]}'})
    
    if prompt["basic"]:
        messages.append({"role": "user", "content": f'2文字目 {prompt["basic"]}'})

    if prompt["detail"]:
        messages.append({"role": "user", "content": f'3文字目 {prompt["detail"]}'})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo", #　モデル指定
            messages=messages
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e: # エラーキャッチ
        print(f"error: {e}")
        return None