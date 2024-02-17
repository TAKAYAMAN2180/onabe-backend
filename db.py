import sqlite3
import json

def newdata():
    # データベースに接続する
    conn = sqlite3.connect('example.sqlite')
    # カーソルオブジェクトを作成
    c = conn.cursor()
    # テーブルの作成
    # idがオートインクリメントされるように設定
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, question TEXT)''')
    # 変更をコミット（保存）する
    conn.commit()
    conn.close()

def adddata(questiondict):
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()
    for category, questions in questiondict.items():
        for question in questions:
            c.execute("INSERT INTO questions (category, question) VALUES (?, ?)", (category, question))
    conn.commit()
    conn.close()


def getalldata():
    # データベースに接続
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()

    # 全てのデータを選択
    c.execute("SELECT * FROM questions")
    rows = c.fetchall()

    # データベース接続を閉じる
    conn.close()

    data_list = [{"category": row[1], "question": row[2]} for row in rows]

    return data_list

def deletedata():
    # 削除したいレコードのIDを設定
    your_id_variable = 8  # ここに実際のIDを設定

    # データベースに接続
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()

    # 指定したIDのデータを削除
    c.execute("DELETE FROM questions WHERE id = ?", (your_id_variable,))

    # 変更をコミット
    conn.commit()

    # データベース接続を閉じる
    conn.close()

deletedata()