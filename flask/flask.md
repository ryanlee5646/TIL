# FLASK

## C9

- [https://ide.c9.io](https://ide.c9.io/)
- workspace 생성 - name: 'flask'- template:blank

### pyenv.sh 설치

```html
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"

git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
```

- `pyenv install 3.6.7` 추가
- `pyenv global 3.6.7` : 파이썬 3.6.7을 global로 쓰겠다
- `python -V`: 파이썬 버전 확인

### 가상환경 pyenv 설치

- `pip install `명령은 컴퓨터에 전역으로 설치하게 된다.

  프로젝트마다 파이썬의 버전, 라이브러리 버전을 나눠서 사용하기 위해서

  독립적인 가상환경안에서 버전 설치를 한다.

- `pyenv virtualenv 3.6.7 first_venv`

- 가상환경으로 사용하려는 폴더내부에서 `pyenv local first_venv`

  - 현재 폴더를 가상환경으로 사용하겠다.

- `pip install -U pip`: pip 최신버전 18.1이 설치된다.

- 디렉토리를 이전으로 옮겨서 `pip freeze` `pip --version`

  18.1이 아니라 pip 10.1이 나온다

  - 가상환경 내부만 18.1 버전이 설치됨을 알 수 있다.

### Flask

- `pip install flask`

- new file - 'app.py '

- local에서 했던 flask는 자체가 호스트였지만, 여기서는 C9의 서버를 사용하기

  때문에 Host와 Port를 입력해주어야 한다

```html
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/') #어떤 주소로 접근하겠다
def index():
    return 'Hello World'
```

- `FLASK_APP=app.py flask run --host=$IP --port=$PORT`

```html
# app.py
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
    
# 밑의 구문은 항상 아래에 와야한다.
# 이 구문 밑은 실행이 안된다.
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

- `FLASK_APP=app.py flask run`

  - os의 env변수로 IP와 PORT를 넘겨준다.

- `python app.py`: Debug=True까지 인자로 들어오면 app.py를 실행해서 flask를 작동시킨다.

- debug mode: On => 변경하는 사항이 바로 반영됨

  ### Debug 모드 적용하기

  ```ㅗ싀
  $ FLASK_DEBUG=1 FLASK_APP=hello.py flask run
   * Serving Flask app "hello.py" (lazy loading)
   * Environment: production
     WARNING: Do not use the development server in a production environment.
     Use a production WSGI server instead.
   * Debug mode: on
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 166-987-344
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  127.0.0.1 - - [11/Jan/2019 17:09:22] "GET / HTTP/1.1" 200 -
  127.0.0.1 - - [11/Jan/2019 17:09:59] "GET /python HTTP/1.1" 200 -
  FLASK_DEBUG=1 FLASK_APP=hello.py flask run
  ```

  - `FLASK_DEBUG=1 FLASK_APP=hello.py flask run`
  - 기본적으로 내용 수정이 필요 한 경우,Flask를 종료한 후에 파이썬 파일의 내용 수정 => 저장 => Flask 재 실행 과 같이 번거로운 절차가 필요하였음.
  - 그러나, Debug 모드를 사용하면, 위의 절차를 거치지 않고 간편히 업데이트가 가능하다.

### Variable routing

- 웹 주소에 들어가는 값이 바뀌어서 웹에 나타나는 내용도 바뀌게 하는 형태?
- route는? : 새로운 페이지를 생성한다.

```python
# app.py
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
    
@app.route('/greeting/<string:name>') 
def greeting(name):
    return f'반갑습니다 ! {name}님!'
    
@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

- `http://flask-blossomwill.c9users.io:8080/greeting/민수`
- return은 string type만 와야하기 때문에 다른 자료형(int 등)은 str로 변환해줘야 한다.
- `http://flask-blossomwill.c9users.io:8080/cube/3`



#### 페이지 생성 - 응용 1

```python
@app.route('/dictionary/<string:word>') 
def dictionary(word):
    return f'{word}을(를) 받았습니다.'
```

- `@app.route('/dictionary/<string:word>')의 <word>` 는 `variable routing` 임. (변경될 수 있는 주소; 변수)
- `word`앞에`string`: (예:`<string:word`) 을 입력 할 경우, 변수의 자료형에 문자열만 가능하게 됨.
  - 예) `<string:word>` / `<int:word>` / `<float:word>` / `<path:word>`
- `def dictionary(word)` : 변수명(word)을 파라미터(괄호 안 내용)로 받아야지 실행이 가능함.

#### 페이지 생성 - 응용 2

```python
@app.route('/dictionary/<string:word>') 
def dictionary(word):
    dictionary = {
        'apple':'사과',
        'banana':'바나나',
        'pear':'배',
        'watermelon':'수박'
    }
     result = dictionary.get(word,'나만의 단어장에 없는 단어입니다')
    return f'{word}은(는) {result}!'   
```

> 딕셔너리의 get 메소드를 이용하면 딕셔너리 내 key에 해당하는 value값을 반환 할 수 있음.
>
> ```
> # 예시
> dictionary = {'apple':'사과','banana':'바나나','pear':'배', 'watermelon':'수박'}
> dictionary.get('apple')
> >>>'사과'
> ```

이를 이용하여, `http://127.0.0.1:5000/dictionar/apple` 을 주소창에 입력한다면,

1. `word` => `apple` 로 들어가며,
2. `dictionary.get('apple')` => `사과` 라는 결과 값이 도출 된다.
3. 따라서, `word` = `'apple'` , `result` = `'사과'` 로 입력이 됨.

최종적으로 `return` 이하를 formatting을 이용하여 `f'{word}은(는) {result}!'` 로 작성해줄 경우, 정상적으로 웹페이지가 출력 된다.

#### get 메소드를 사용한 이유?

일반적으로 딕셔너리는 get 메소드를 사용하지 않고 다음과 같은 방법으로도 key값을 통해 value 값을 접근할 수도 있다.

하지만 이 방법으로 웹페이지를 구현할 때, 딕셔너리 내에 존재하지 않는 key 값을 불러온다면 에러가 발생한다.

get 메소드의 경우, 딕셔너리 내에 존재 하지 않는 key 값을 불러올 경우 None 을 출력하기 때문에, 에러를 피할 수 있다.

```
# 예시
dictionary = {'apple':'사과','banana':'바나나','pear':'배', 'watermelon':'수박'}
dictionary.['apple']
>>>'사과'
```

또한, get 메소드는 기본값을 적용할 수 있음. 이를 활용하여, `http://127.0.0.1:5000/dictionar/kiwi` 와 같이, 딕셔너리 내에 존재 하지 않는 키 값을 불러올 때, 기본값이 웹페이지에 출력되게 할 수 있다.

```
result = dictionary.get(word,'나만의 단어장에 없는 단어입니다')
```

### Render_template을 이용한 html 파일 열기

- 정확히 `'templates'` 이름의 하위폴더를 생성한다.

```html
<!DOCTYPE html>
<!-- html_file.html -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>This is HTML file.</h1>
</body>
</html>
# app.py
"""
위의 코드
"""
@app.route('/html_file')
def html_file():
    return render_template('html_file.html')
```

- `render_template` 기능으로 'html_file.html' 파일을 페이지로 연다.

```html
<!DOCTYPE html>
<!-- hi.html -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Hi! {{ name_in_html }}</h1>
</body>
</html>
# app.py
"""
위의 코드
"""
@app.route('/hi/<name>')
def hi(name):
    return render_template('hi.html', name_in_html=name)
```

- `render_template` 기능으로 'hi.html' 파일을 페이지로 연다.
- 'hi.html'의 `<h1>Hi! {{ name_in_html }}</h1>` 에서
  - Hi!는 그대로 출력되고, 변수를 출력하고 싶으면 {{ 변수 }} 이렇게 이중 중괄호 안에 변수를 넣어야 한다.

### Jinja templates

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {% for f in fruits %}
    <li>
        {{ f }}
    </li>
    {% endfor %} 반드시 반복문을 닫아줘야함
</body>
</html>
# app.py
"""
위의 코드
"""
@app.route('/fruits')
def fruits():
    fruits = ['qpple', 'banan', 'mango', 'melon']
    return render_template('fruits.html', fruits=fruits)
```

- `{% for f in fruits %}`: 중괄호 안에 앞뒤로 %를 써주면 안에 있는 내용이 출력이 안되고, jinja 템플릿이 적용됨
- `{{ fruits }}` 로 쓴다면 글자 그대로 출력이 됨
- list로 for 문을 순회하는 요소값 f 출력
- `{% endfor %}` : for 문 끝!

### 폴더정리

- ['workspace'] - [Flask] - ['here'] - []'clone'] - 'playgroun' - create