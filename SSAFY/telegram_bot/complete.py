import os
import requests
from flask import Flask, request
app = Flask(__name__)

# api_url = 'https://api.telegram.org'
api_url = 'https://api.hphk.io/telegram'
token = os.getenv('TELEGRAM_BOT_TOKEN')
naver_client_id = os.getenv('NAVER_CLIENT_ID')
naver_client_secret = os.getenv('NAVER_CLIENT_SECRET')

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 1. requset를 변수에 저장
    from_telegram = request.get_json()
    if from_telegram.get('message') is not None:
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')

        # 3. CFR
        if from_telegram.get('message').get('photo') is not None:
            file_id = from_telegram.get('message').get('photo')[-1].get('file_id')
            file_res = requests.get(f'{api_url}/bot{token}/getFile?file_id={file_id}')
            file_path = file_res.json().get('result').get('file_path')
            file_url = f'{api_url}/file/bot{token}/{file_path}'

            real_file_res = requests.get(file_url, stream=True)
            headers={'X-Naver-Client-Id':naver_client_id,'X-Naver-Client-Secret':naver_client_secret}

            clova_res = requests.post('https://openapi.naver.com/v1/vision/celebrity', headers=headers, files={'image':real_file_res.raw.read()})
            print(clova_res.json())

            if clova_res.json().get('info').get('faceCount'):
                print(clova_res.json().get('faces'))
                celebrity = clova_res.json().get('faces')[0].get('celebrity')
                text = f"{celebrity.get('value')} - {celebrity.get('confidence')*100}% 확신"
            else:
                text = "인식된 사람이 없습니다."
        else:
            # 2. keyword
            if text[0:4] == '/번역 ':
                headers = {'X-Naver-Client-Id':naver_client_id,'X-Naver-Client-Secret':naver_client_secret}
                papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers,
                                                data={
                                                    'source':'ko',
                                                    'target':'en',
                                                    'text': text[4:]
                                                })
                text = papago_res.json().get('message').get('result').get('translatedText')

        # res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
        res = requests.post(f'{api_url}/bot{token}/sendMessage', data={'chat_id':chat_id,'text':text})
    return '', 200

if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))