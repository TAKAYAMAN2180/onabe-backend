# openai, osインポート
import os
import openai
#load_dotenv()
openai.api_key = "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"
#os.environ["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"]

# ユーザーからの質問に回答する関数
def cre_word(keyword): # lang: ユーザの使用言語, user_que: 元(ユーザの)言語の質問
    response_question = openai.ChatCompletion.create(
        model = "gpt-4-1106-preview",
        messages = [
            {"role": "system", "content": "キーワードに関連する言葉を5つ出力してください。"},
            {"role": "system", "content": "例)キーワード:学校であれば教室,授業,先生,机,テスト"},
            {"role": "user", "content": "キーワード:"+keyword},
        ],
    )
    gpt_question=response_question.choices[0]["message"]["content"].strip().split(",")

    return gpt_question
   
#test1=cre_word("電気")
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