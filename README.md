icis2024-prompt
====
Overview  

This program used to generate the source code for the icis2024 summer 3 SS3-12 research experiment.  

Due to the amount of text, it would be nearly impossible to list all the prompts used in the experiment, so I'll leave them here.

Each text intended for the development documents is located in the `doc` folder, and the main content of the prompts is written in `utils.py`.

このプログラムは、icis2024 summer 3 SS3-12 における調査実験を実施するためのツールである。

文章量の観点から、実験に使用したプロンプトを詳細に記載することが困難であるためここに記す。

開発文書を想定した各テキストは `doc`フォルダに配置され、プロンプトの主な内容は `utils.py`に記載されている。

## Description
Enter a prompt requesting the generation of python source code based on the development documentation provided, into `gpt-4-turbo` using the Open AI API.  

By setting the arguments when executing main.py, you can generate source code with any combination of development documents, any number of times.

I made this program for personal use, so I haven't done any detailed refactoring.


指定した開発文書に基づくpythonソースコードの生成を要求するプロンプトを、Open AI APIを使用して `gpt-4-turbo `に入力する。 

main.py実行時に引数を設定することで、任意の開発文書の組み合わせで、任意の回数のソースコードを生成することができる。

実験の実施のみが目的であるため、本ツールのリファクタリングなどは行っていない。

## Requirements
- `Python 3.x` (3.10 tested)
- An OpenAI API key stored in the environment variable `API_KEY` in `.env`

## Usage
in bash  

- set OpenAI API key  

`touch .env && echo API_KEY=[your openai api_key] > .env`

- install package

`pip install -r requirements.txt ` 

- run

`python3 main.py [OPTIONS]`

# Options

- Required  
 
`--O`  
The path to the directory where the generated source code will be saved.  

`--C`  
The number of times to generate the source code. 


- Optional  

`--r`  
The path to the requirements definition document. 
  
`--b`  
The path to the basic design document. 
  
`--d`  
The path to the detailed design document. 

# Example

- All development documents, output=./prompt3, count=10  
`python3 main.py --r doc/requir.txt --b doc/basic.txt --d doc/detail.txt --O ./prompt3 --C 10`
  

## Reference

[1], "Analysis of Quality Improving of Source Code Generation by LLM along with More Detailing of  Development Documents", icis2024-summer, p3, 2024
