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

def addscrapdata(questiondict,date):
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()
    for category, question in questiondict.items():
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

    data_list = [{"id":row[0], "keyword": row[1], "question": row[2],"answer": row[3],"createdAt": row[4],"answeredAt": row[5]} for row in rows]

    return data_list

def getiddata(question_id):
    # データベースに接続
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()

    # idでデータを選択
    c.execute("SELECT * FROM questions WHERE id=?", (question_id,))  # パラメータはタプルとして渡す
    row = c.fetchone()  # idはユニークなので、一致するのは最大で1行のみ

    # データベース接続を閉じる
    conn.close()

    # 結果が存在すれば、その行のデータで辞書を作成
    if row:
        data = {
            "id": row[0],
            "keyword": row[1],  
            "question": row[2],
            "answer": row[3],
            "createdAt": row[4],
            "answeredAt": row[5]
        }
        return data
    else:
        return None  # 結果がなければ、Noneを返す


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
    c.execute("ALTER TABLE questions ADD COLUMN answer_at DATETIME")

    # 変更をコミット
    conn.commit()

    # データベース接続を閉じる
    conn.close()

def addanswer(question_id,answer_text,date):
    # データベースに接続
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()

    c.execute("UPDATE questions SET answer = ?, answer_at = ? WHERE id = ?", (answer_text,date,question_id))

    # 変更をコミット
    conn.commit()

    # データベース接続を閉じる#
    conn.close()

def make_question_column_unique():
    # データベースに接続
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()

    # 新しいテーブルを作成し、`question`カラムに`UNIQUE`制約を設定
    c.execute('''
    CREATE TABLE IF NOT EXISTS new_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        question TEXT UNIQUE,
        answer TEXT,
        created_at DATETIME,
        answer_at DATETIME
    )
    ''')

    # 既存のデータを新しいテーブルに移行（重複する`question`のデータは除外）
    c.execute('''
    INSERT INTO new_questions (id, category, question, answer, created_at, answer_at)
    SELECT id, category, question, answer, created_at, answer_at FROM questions
    GROUP BY question
    ''')

    # 既存のテーブルを削除
    c.execute('DROP TABLE questions')

    # 新しいテーブルの名前を変更
    c.execute('ALTER TABLE new_questions RENAME TO questions')

    # 変更をコミット
    conn.commit()

    # データベース接続を閉じる
    conn.close()

#make_question_column_unique()