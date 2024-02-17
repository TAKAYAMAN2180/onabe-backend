import sqlite3

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

def adddata(questiondict,date):
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()
    for category, questions in questiondict.items():
        for question in questions:
            c.execute("INSERT INTO questions (category, question,created_at) VALUES (?, ?, ?)", (category, question ,date))
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

    data_list = [{"id":row[0], "keyword": row[1], "question": row[2],"createdAt":row[3]} for row in rows]

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

def addclass():
    # データベースに接続
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()

    # `questions`テーブルに`answer`カラムを追加（TEXT型として）
    c.execute("ALTER TABLE questions ADD COLUMN created_at DATETIME")

    # 変更をコミット
    conn.commit()

    # データベース接続を閉じる
    conn.close()

def addanswer(question_id,answer_text):
    # データベースに接続
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()

    c.execute("UPDATE questions SET answer = ? WHERE id = ?", (answer_text, question_id))

    # 変更をコミット
    conn.commit()

    # データベース接続を閉じる
    conn.close()