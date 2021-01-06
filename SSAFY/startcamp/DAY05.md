### Chat Bot 만들기

* Telegram의 Chat bot인 BotFater를 이용해 시작할 수 있다.

1. Chat bot 생성

* `/newbot`: 새로운 bot 생성 시작
* botname: `blossomwll`
* username: `blossomwill_bot`

2. Token

* Bot token: API 접근하는 권한을 가진 토큰
*  Use this token to access the HTTP API:  `token`

3. Bot API 설명

* https://core.telegram.org/bots/api

4. ID 획득

* `https://api.telegram.org/bot<token>/getUpdates`
* telegram 서버에 데이터를 보내고 받아서 `from`의  id를 확인한다.
* 첫 단락에 id가 있다 

```json
"from": {
          "id": <id>,
          "is_bot": false,
          "first_name": "Minsu",
          "last_name": "Seo",
          "language_code": "ko"
        },
```

5. 메세지 보내기

* `https://api.telegram.org/bot<token>/sendMessage?chat_id=<token>&text="반갑습니다"`

6. token, id  숨기기

* `$ code ~/.bash_profile`

```python
# .bash_profile 띄어쓰기 금지
export TELEGRAM_BOT_TOKEN='token'
export CHAT_ID='id'
```

* `source ~/.bash_profile`: shell refresh
* `printenv`

```python
import requests
import os
token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

#하고 싶은 것들
text = '안녕하세요'
requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}")
```

7. 메세지 주고 받기

* 특정한 메세지가 Sever DB로 보내졌다. URL을 Server(Telegram)에 알려주어 메세지를 알아내고, 메세지를 보낸 곳(bot)에 메세지를 보낸다.
* `www.c9.io` 서비스 사용
* `ide.c9.io` 예전 c9 서비스 주소

#### C9 Server

* 서버를 빌려서 구성해본다.

1. 파이썬 버전 관리

* `pyenv`: python 버전 관리
  * `https://gist.github.com/nwith`
* `$ pyenv install 3.6.7` : 파이썬 3.6.7 설치
* `$ pyenv versions` : 파이썬 버전들 확인
*  `$ pyenv global 3.6.7`: 파이썬 기본 버전으로 설정
* `$ pyenv -V`: 파이썬 버전 확인
* `$ exec $SHELL`: Shell창 refresh (리프레쉬 해줘야 바뀐 버전이 적용됨)

2. flask 설치

* `~/workspace/telegram-bot` 경로에 app.py 추가
* `$ pip install flask`
* `$ FLASK_APP=app.py flask run`

* `FLASK_APP=app.py flask run --hosh=$IP --port=$PORT` : flask 서버 작동 명령어

  * IP는 외부에서 찾을 수 있는 IP

  * PORT는 외부에서 접속할 수 있는 통로

  * IP와 PORT(통로)를 넘겨서 외부에서 접근할 수 있게 만든다.

  * ```python
    # 아래 Code를 app.py에 추가하면 서버 작동 명령어를 포함시킨다.
    if __name__ == '__main__':
        app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
    ```
* 페이지 주소는 c9 우측상단에 Share - Application에서 확인 할 수 있다.

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

3. Token 숨기기

* bashrc 수정

* `c9 ~/.bashrc` 
* 마지막줄에 `export TELEGRAM_BOT_TOKEN=<token>` 추가
* get: 주소를 직접 얻는 방식, 주소창 입력
* post: 내부적으로 생성되야하는 데이터에 쓰인다. 주소창에서 쓸 수 없다.

4. setWebhook 사용

* server에서 url을 가져온다
* local(VS code) 에서 작업하다가 c9을 쓰는 이유는 set webhook 기능이 필요하기 때문

##### 시나리오

* user가 telegram에 메세지를 보내고 telegram이 Bot한테 메세지를 보내야 하는데 주소를 알수 없다.
* C9의 setWephook으로 
* User -> Telegram -> [Telegram Server] -> setWebhook -> C9( ( Flask(Bot) ) ) token을 이용해 받아온다 ->  

