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
def adddata(questiondict):
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()
    for category, questions in questiondict.items():
        for question in questions:
            c.execute("INSERT INTO questions (category, question) VALUES (?, ?)", (category, question))
    conn.commit()


def getalldata():
    pass


newdata()
