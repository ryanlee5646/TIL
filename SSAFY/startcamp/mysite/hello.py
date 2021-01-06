from flask import Flask, render_template, request
import random, requests, os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ping')  
def ping():
    return render_template('ping.htm')  

@app.route('/pong')
def pong():
    name = request.args['name']
    result = random.choice(['캡처.PNG', '2.PNG', '3.PNG', '5.PNG', '6.PNG'])
    # result = random.choice(["유머", "다혈질", "긍정", "배고픔"])
    return render_template('pong.htm', name_in_htm=name, result=result)

@app.route('/lotto/<int:num>')
def lotto(num):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    response = requests.get(url) 
    lotto = response.json()   
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])  #=> 30           
    
    bonus = lotto['bnusNo'] #=> 6
    return render_template('lotto.htm', w=winner, b=bonus, n=num)    
    
@app.route('/write')
def write():
    return render_template('write.htm')

@app.route('/send')
def send():
    token = os.getenv('TELEGRAM_BOT_TOKEN') #=> 
    chat_id = os.getenv('CHAT_ID')
    #하고싶은 것을 작성할 수 있음
    text = request.args['message']
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return render_template('send.htm')

