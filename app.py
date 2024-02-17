from flask import Flask, jsonify, request
from flask_cors import CORS
from chatgpt import cre_word,cre_question
from db import adddata

app = Flask(__name__)
CORS(app,origins=["http://localhost:3000"], methods=["POST","GET"])

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
    return jsonify(genequestiondict)
    

@app.route('/getall',methods=['GET'])
def jsonalltest():
     
    test_api = {
        'qtext': 'It is test. where is hospital?',
        'lang': 'english'
        }

    return jsonify(test_api)

@app.route('/jsontest')
def form_interface():

    testtext = request.json.get("test")

    return jsonify(testtext)

@app.route('/test')
def jsontest():

    test_api = {
        'qtext': 'It is test. where is hospital?',
        'lang': 'english'
        }

    return jsonify(test_api)



if __name__ == '__main__':
    app.run(debug=True,port=8888)