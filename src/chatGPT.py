import openai
import settings

API_KEY = settings.API_KEY
openai.api_key = API_KEY

def getResponse(theme: str):
  command = """次のJSONのフォーマットで""" + theme + """に関するクイズを5問作れ。
  {
    "quizes": [
      {
        "question": クイズの問題文,
        "options": [
          選択肢の配列
        ],
        "answer": 正解の選択肢,
        "answerIndex": 正解の選択肢のインデックスを整数型で
      }
    ]
  }
  キーは必ず含ませる。
  JSON以外の情報は削除する。
  """

  response = openai.ChatCompletion.create(
      model='gpt-3.5-turbo',
      temperature=0.0,
      messages=[
          {
              'role': 'system',
              'content': command
          }
      ],
  )

  print(response["choices"][0]["message"]["content"])
  return response["choices"][0]["message"]["content"]