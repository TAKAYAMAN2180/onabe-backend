# openai, osインポート
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# ユーザーからの質問に回答する関数
def cre_word(keyword): # lang: ユーザの使用言語, user_que: 元(ユーザの)言語の質問
    response_question = openai.ChatCompletion.create(
        model = "gpt-4-1106-preview",
        messages = [
            {"role": "system", "content": "キーワードに関連する言葉を5つ出力してください。"},
            {"role": "system", "content": "例)キーワード:学校であれば教室,授業,先生,机,テスト"},
            {"role": "system", "content": "キーワードについて良くわからない場合は「本当に良くわからない」と出力してください"},
            {"role": "user", "content": "キーワード:"+keyword},
        ],
    )
    
    gpt_output=response_question.choices[0]["message"]["content"].strip().split(",")

    if gpt_output == ['本当に良くわからない。'] or gpt_output == ['本当に良くわからない']:
        return None
    
    return gpt_output
   
#test1=cre_word("コンセント")
#print(test1)

def cre_question(geneword):
    response_question = openai.ChatCompletion.create(
        model = "gpt-4-1106-preview",
        messages = [
            {"role": "system", "content": "あなたは%sを知らない人です。"%(geneword)},
            {"role": "system", "content": "キーワードに関連する質問を5つ生成しなさい。"},
            {"role": "system", "content": "回答を並べるときにナンバリングは必要ありません。改行だけしてください。"},
            {"role": "user", "content": "キーワード:%s"%(geneword)},
        ],
    )
    gene_question=response_question.choices[0]["message"]["content"].strip().splitlines()

    return gene_question

#test2=cre_question("コンセント")
#print(test2)