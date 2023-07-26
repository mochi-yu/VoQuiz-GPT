from flask import Flask, request
from chatGPT import getResponse
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def getData():
    data = request.get_json()
    gptResponse = getResponse(data["theme"])
    print(gptResponse)
    return json.dumps(gptResponse)

@app.route("/test", methods=["POST"])
def testData():
    data = request.get_json()
    print(data["theme"])
    gptResponse = """{
      "quizes": [
        {
          "question": "クイズの問題文",
          "options": [
            "選択肢の配列",
            "選択肢の配列",
            "選択肢の配列"
          ],
          "answer": "正解の選択肢",
          "answerIndex": 0
        }
      ]
    }"""
    print(gptResponse)
    print(type(json.dumps(gptResponse)))
    return gptResponse

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
