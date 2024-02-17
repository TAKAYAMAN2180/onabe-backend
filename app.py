from flask import Flask, jsonify, request
from flask_cors import CORS
from chatgpt import cre_word,cre_question
from db import adddata,getalldata,addanswer

app = Flask(__name__)

CORS(app,origins=["https://onabe-front-front.vercel.app"], methods=["POST","GET"])

# ルートページのハンドラ
@app.route('/wordpost',methods=['POST'])
def keywordtoquestion():
    user_input = request.json.get('keyword')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    questionlist = cre_word(user_input)
    print(questionlist)
    print(type(questionlist))
    #リストをdbに保存していく
    genequestiondict={}
    for geneword in questionlist:
        genequestiondict[geneword]=cre_question(geneword)

    adddata(genequestiondict)
    return 
    

@app.route('/getall',methods=['GET'])
def jsonalldata():
     
    data=getalldata()

    return jsonify(data)

@app.route('/delete',methods=['GET'])
def deletedata():
    deletedata()

@app.route('/wordpost',methods=['POST'])
def newanswer():
    id = request.json.get('id')
    answer = request.json.get('answer') 
    addanswer(id,answer)

if __name__ == '__main__':
    app.run(debug=True,port=8000)