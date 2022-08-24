from cgi import parse_multipart
from flask import Flask, request
import json
import start


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!'

# 장학금 조회
@app.route('/api/Lookup', methods=['POST'])
def Lookup():
    
    body = request.get_json()
    print(body)
    # 카카오 챗봇에서 보낸 요청값을 body에 저장
    name=body['action']['detailParams']['name']['value']
    print(name)
    # 사용자 발화값 중 입력값을 받기 위함
    df1=start.area_db(name)
    # db_select함수에 name값 입력
    name=df1['name']
    print(name)
    print(type(name))
    # df1이라는 데이터프레임의 'name'컬럼값을 series형식으로 저장
    URL=df1['url']
    # df1이라는 데이터프레임의 'url'컬럼값을 series형식으로 저장
    image=df1['image']
    # df1이라는 데이터프레임의 'image'컬럼값을 series형식으로 저장

    if len(df1) > 0:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                     {
                        "simpleText": {
                            
                            "text": "조회하신 장학금입니다"
                            },
                    },

                    {
                    "carousel": {
                    "type": "basicCard",        
                    "items": [
                        {
                        "title": name[0],
                        "description": "장학금 조회",
                        "thumbnail": {
                            "imageUrl": image[0]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "장학금 정보 보기",
                            "webLinkUrl": URL[0]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"

                            }
                        ]
                        }
                    ]      
                    }    
                }
                ]
            }  
        }
  
            

    return responseBody