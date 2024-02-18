from flask import Flask, jsonify, request
from flask_cors import CORS
from chatgpt import cre_word,cre_question
from db import adddata,getalldata,getiddata,addanswer,addscrapdata
import datetime

app = Flask(__name__)

CORS(app)
#origins=["http://localhost:3000/"], methods=["POST","GET"]
#"https://onabe-front-front.vercel.app",
# ルートページのハンドラ
@app.route('/wordpost',methods=['POST'])
def keywordtoquestion():
    user_input = request.json.get('keyword')
    user_date = request.json.get('createdAt')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    questionlist = cre_word(user_input)
    if questionlist is None:
        return jsonify({"message": "Operation successful"}), 200
    #リストをdbに保存していく
    genequestiondict={}
    for geneword in questionlist:
        genequestiondict[geneword]=cre_question(geneword)
    
    adddata(genequestiondict,user_date)
    return jsonify({"message": "Operation successful"}), 200

    

@app.route('/getall',methods=['GET'])
def jsonalldata():
     
    data=getalldata()

    return jsonify(data)

@app.route('/delete',methods=['GET'])
def deletedata():
    deletedata()

@app.route('/addanswer',methods=['POST'])
def newanswer():
    id = request.json.get('id')
    answer = request.json.get('answer') 
    date = request.json.get('answerAt')
    addanswer(id,answer,date)
    return jsonify({"message": "Operation successful"}), 200

@app.route('/idquestion',methods=['POST'])
def getidquestion():
    id = request.json.get('id')
    data=getiddata(id)
    return  jsonify(data)
    
@app.route('/scrapquestion',methods=['POST'])
def postscrapbox():
    scrapboxdict={}
    question=request.json.get('question')
    keyword=request.json.get('pageTitle')
    scrapboxdict[keyword]=question
    addscrapdata(scrapboxdict,datetime.datetime.now())
    return jsonify({"message": "Operation successful"}), 200


if __name__ == '__main__':
    app.run(debug=True,port=8000)