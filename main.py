import os
import sys
import argparse
from utils import load_document, generate_code
# from test_utils import load_document, generate_code

def main():
    parser = argparse.ArgumentParser(description="開発文書にもとづいてpythonのソースコードを生成する")
    parser.add_argument('--r', required=False, help="要件定義書のパス")
    parser.add_argument('--b', required=False, help="基本設計書のパス")
    parser.add_argument('--d', required=False, help="詳細設計書のパス")
    parser.add_argument('--O', required=True, help="ソースコードを保存するディレクトリのパス")
    parser.add_argument('--C', type=int, default=1,required=True, help="ソースコードを生成する回数")
    args = parser.parse_args()

    # 開発文書の読み込み
    requirements_doc = load_document(args.r)
    basic_doc = load_document(args.b)
    detail_doc = load_document(args.d)

    # 出力ディレクトリの作成
    os.makedirs(args.O, exist_ok=True)

    # APIキーの読み込み
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY がない。.env書け。")
        sys.exit(1)

    # 指定回数分生成
    for i in range(1, args.C + 1):
        prompt = {
            'requirements': requirements_doc,
            'basic': basic_doc, 
            'detail': detail_doc
        }
        code = generate_code(prompt, api_key)

        # 生成したコードを保存
        if code:
            file_name = os.path.join(args.O, f"cli{i}.py")
            with open(file_name, "w", encoding='utf-8') as file:
                file.write(code)
            print(f" {file_name}として保存しました。")
        else:
            print(f"生成に失敗 {i}回目")

if __name__ == "__main__":
    main()