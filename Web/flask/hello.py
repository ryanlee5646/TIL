from flask import Flask
app = Flask(__name__)

@app.route("/") # @는 데코레이터(decorator)
def hello():
    return "Hello World!"

@app.route('/python')
def python():
    return 'Python is fun!'

@app.route('/dictionary/<string:word>')  #string 자리에는 int, pass와 같은 변수도 올 수 있다.
def dictionary(word):
    dictionary = {
        'apple' : '사과',
        'banana' : '바나나',
        'pear' : '배',
        'watermelon' : '수박'
    }
    result = dictionary.get(word,'나만의 단어장에 없는 단어입니다.') 
    return f'{word}은(는) {result}!'