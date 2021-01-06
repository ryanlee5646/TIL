# TIL

## Day 01

### 웹 브라우저(Webbrowser)

---

```python
import webbrowser
keywords = ['날씨', '박보영', '구미맛집']
for k in keywords:
	webbrowser.open('https://search.daum.net/search?q='+k)
```

###### method

* `open`
* `open_new`
* `open_new_tab`

### 정보요청(Request)

---

###### method

* `pip install requests`
* `request.get(주소).text`: HTML 내용 출력
* `request.get(주소).status_code`:  상태 코드

```python
import requests
import bs4
 
response = requests.get('https://finance.naver.com/sise/').text
print(response)

# ctrl + `: 터미널창 toggle
```

### 정보조작

---

* `pip install bs4`

* `select(selector)`: 문서 안의 내용 선택
* `select_one(selector)`: 문서 안에 있는 특정 내용 하나 선택

```python
import requests
import bs4
 
response = requests.get('https://finance.naver.com/marketindex/').text
#print(response)
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").text
print('지금 원/달러 환율은' + result +'입니다')
print(f'지금 원/달러 환율은 {result} 입니다')
```

### VSCode 기본 terminal 변경

---

* `ctr + shift +p`

* shell 검색
* select Default Shell
* Git Bash

### VS 단축키

---

* `ctrl + backtick`: 터미널 보기

* `ctrl + L`: 터미널 clear

* `ctrl + /`: 주석 toggle



## Day 02

### Git 설정

---

* `git config --global user.name 'Minsu Seo'`

* `git config --global user.email 'tjalstn10@gmail.com'`
* `git config --global --list`: 유저 설정

* `git init`: git 초기화, git으로 관리하겠다!
* `git remote add origin 주소` : 원격 저장소 등록
  * `git remote set-url origin 주소`: 원격 저장소 수정

### Git commit & Push

---

* `git add .`: 현재 폴더의 변경사항들을 commit하기 위해서 준비

* `git commit -m 'day 02 입니다.'`: commit, 변경 사항 저장, ' '안에 commit 설명
* `git push -u origin master`: remote로 등록된 원격저장소(remote repository)
  - 이후에는 `git push`만 입력해도 동작합니다.

* `git status`: 현재 폴더의 git의 상태
* `git log`: 커밋 기록
* Markdown 기록할 것입니다.
  * typora or VSCode
* GitHub Student Developer Pack

###  Git bash 명령어

---

* `$ touch test.txt`: 파일 생성 

* `$ mkdir`: 디렉토리 생성
* `$ cd`: 디렉토리 변경
* `$ ls:`: 현재 디렉토리의 파일 보기
* `$ pwd`: 현재 디렉토리 위치
* `$ clear`: 화면 정리 
  * `ctrl + /`  동일한 기능
* ` $ ctrl + c`: 현재 실행프로그램 종료
* `$ exit()`: 종료?? (수정중)

### 파일명 변경

---

* `import os`: 파일 조작해주는 module

* `os.chdir(r'폴더 주소')`
* `os.listdir('.')`: 현재 working directory의 파일 목록 리스트
* `os.rename('바꾸고자 하는 파일 이름', '바꿀 이름')`
* `os.getcwd()`: 이동해온 디렉토리

```python
# 이름.txt를 지원자_누구누구.txt로 변경


os.chdir(r'C:\Users\student\minsu\day02\dummy') #디렉토리를 해당 경로로 이동
for filename in os.listdir('.'): #.은 현재폴더를 의미
    os.rename(filename, f'지원자_{filename}') #os.rename(src, dst)
```



###  Python 문자열 변경

---

* `replace(원래 이름, 바꾸려는 이름)`: 문자열의 일부/전체 변경

```python
# 지원자_0_누구누구.txt를 합격자_0_누구누구.txt로 변경
import os

for filename in os.listdir('.'):
    new_filename = filename.replace('지원자','합격자')
    os.rename(filename, new_filename)
```



### Python 파일

---

#### 파일 쓰기

1. `open(파일명, w)`: 파일명으로 파일  생성
2. `write(파일내용)`:  파일에 내용 쓰기
3. `close()`: 파일 종료

```python
f = open('ssafy.txt','w') # w: write, r: read, a: append
f.write('This is SSAFY!') #파일 내부에 문자열 기록
f.close()
```

* with open(파일명, 모드, encoding) as

  * `모드 w: write, r: read, a: append`

  * ```python
    with open('ssafy.txt','w', encoding='utf8') as f:
      	f.write('This is SSAFY!, with 이용했다')#문자열
    	f.writelines(['1\n' '2\n' '3\n'])	   #List
    ```

  * open(), write(), close()  묶은 기능

#### 파일 읽기

```python
with open('ssafy.txt', 'r', encoding = 'utf8') as f:
    lines = f.readlines()
    for line in lines:
        #print(line)        #줄바꿈을 포함한 라인의 문자를 보여줌
        print(line.strip()) #줄바꿈을 제외한 라인의 문자를 보여줌
```

#### 파일 조작

* ssafy.txt의 문자열의 뒤집어서 ssafy_reverse.txt에 쓰기

```python
# 1. 한번에 처리
with open('ssafy.txt', 'r', encoding = 'utf8') as f:
	lines = reversed(f.readlines())
    with open('ssafy_reversed.txt', 'r', encoding = 'utf8') as ff:
        ff.writelines(lines)
```

```python
# 2. read / write
with open('ssafy.txt', 'r', encoding = 'utf8') as f:
    lines = f.readlines()
   
lines.reverse()

with open('ssafy_reverse.txt','w', encoding='utf8') as f:
    f.writelines(lines)
```

### CSV 쓰기

---

```python
lunch = {  "매콤돈까스"   : "053-555-1234",
           "한마리삼계탕" : "053-666-8888",
           "화로소고기"   : "053-777-9977",
           "별난짬뽕"     : "053-675-4422",
           "용성비빔밥"   : "053-987-6543"
        }
with open('lunch.csv','w',encoding = 'utf8',newline = '') as f:
    for item in lunch.items():  # 리스트 [(key, value), ...]
        f.write(f'{item[0]},{item[1]}\n')
```

```python
# csv 사용
lunch = {  "매콤돈까스"   : "053-555-1234",
           "한마리삼계탕" : "053-666-8888",
           "화로소고기"   : "053-777-9977",
           "별난짬뽕"     : "053-675-4422",
           "용성비빔밥"   : "053-987-6543"
        }

import csv
with open('lunch.csv','w',encoding = 'utf8',newline = '') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():  # 리스트 [(key, value), ...]
        csv_writer.writerow(item)   
        
    #writerow도 개행문자를 만들고 f도 개행문자를 
    #만들어서 2줄이 개행된다.
    #newline=''로 f의 개행문자 제거
```

### CSV 읽기

---

```python
with open('lunch.csv','r',encoding = 'utf8') as f:
    # 1. 단순 문자열 읽기
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))    
```

```python
import csv
with open('lunch.csv','r',encoding = 'utf8') as f:
    # 2. csv 사용
    items = csv.reader(f)
    print(items)
    for item in items:
        print(item)
    
```

### 웹 크롤링(crawling)

---

* class 명으로 select

* class는 space 공백으로 구분해서 작성
* `.text`: 텍스트만 추출

```python
# naver 인기검색어 검색어 크롤링
import requests
import bs4
 
response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('div.ah_list.PM_CL_realtimeKeyword_list_base span.ah_k') #class로 검색
for item  in result:
    print(item.text)

```

```python
# naver.py
# naver 인기검색어 검색어 크롤링
import requests
import bs4
 
response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('div.ah_list.PM_CL_realtimeKeyword_list_base a.ah_a') #class로 검색
# ~~_list_base와 a.ah_a 사이 공백으로 구분

for item  in result:
    rank = item.select_one('.ah_r').text
    keyword = item.select_one('.ah_k').text
    print(f'{rank} / {keyword}')
```

#### Request 거부 시 우회 방법

* Chrome - 검사 - Network - Request Headers -> User-Agent 내용 복사
  * Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
* headers 생성

```python
# melon차트 request using header
import requests
import bs4
 
h = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get('https://www.melon.com/chart/index.htm', headers =h).text
print(response)
```

##### java scrips로 구성된 웹 크롤링

* selenium 사용



## DAY03

### Python의 공백처리

---

* 0, [], (), {}: false로 처리

* if 공백: false

### Github Page 제작

---

* Github New repository 

* repository name: blossomwill.github.io  ("GithubName".github.io)
* `$ git clone https://github.com/blossomwill/blossomwill.github.io.git` student/에 git 폴더 생성
* bootstrap template - Start Bootstrap/Resume 테마 다운로드
* 압축해제 후 항목 전체를 blossomwill.github.io 폴더 내로 복사
* blossomwill.github.io 폴더에서 우클릭 - [open with code] 하면 해당 git가 VS code로 열린다.
* `git status`
* `git add .`
* `git commit -m 'Init commit'`
* `git push`
* Github - settings- GitHub Pages에서 site 활성화 확인

### html 작성 및 태그(TAG)

---

* `html5: + tap`: html 기본 틀 자동완성

* 주석: `ctrl+/`     `<!-- -->`
* `<head>`: 문서에 대한 정보를 담고있다

* `<body>`: 실제 웹에서 보이는 화면
* `<br>`: 개행
* `<h#>`
* `<p>`: 본문 paragraph
* `<ul>`: unordered list
* `<ol>`: orderd list
* `<div>`: 속성 없음 division

```html
<body><!--실제 보이는 웹화면-->
    <h1>이것은 h1 태그입니다.</h1>
    <h2>이것은 h2 태그입니다.</h2>
    <h3>이것은 h3 태그입니다.</h3>
    <h4 id="green">이것은 h4 태그입니다.</h4>
    <h5 class="yellow">이것은 h5 태그입니다.</h5>
    <h6 class="yellow">이것은 h5 태그입니다.</h6>

    <p><!-- paragraph 본문-->
        이것은 p 태그입니다. <br>
        이것은 p 태그입니다. <br>
        이것은 p 태그입니다. <br>
        이것은 p 태그입니다. <br>
    </p>

    <ul><!-- unordered list-->
        <li>리스트 1번째</li>
        <li>리스트 2번째</li>
        <li>리스트 3번째</li>
        <li>리스트 4번째</li>
    </ul>
    <ol>
        <li>리스트 1번째</li>
        <li>리스트 2번째</li>
        <li>리스트 3번째</li>
    </ol>
    <div><!-- 어떤 속성도 가지지 않은 놈-->
         <b>여기는 division입니다.</b><!-- bold -->
         <i>여기는 division입니다.</i><!-- italic -->
    </div>
</body>
```

### CSS

---

* html에서 <style>추가 또는 css 파일 생성

```html
<style>
        h1, h3 {
            color: red;
        }
        h2 {
            color: blue;
        }
        #green {
            color: green;
        }
        .yellow {
            color: yellow;
        }
    </style>
```

* semiconlon(;)을 문장의 끝에 붙여준다

* id참조: id앞에 '#'붙여준다  `#green`

* class참조: class앞에 '.'붙여준다 `.yellow`

### 이미지 추가

---

* `<img src="이미지 파일" alt = "이미지 설명">`

* `<img src="이미지 주소" alt = "이미지 설명">`

### Flask

---

* python 기반 web framework

#### Flask 설치 및 실행

* `http://flask.pocoo.org/` Flask 홈페이지

* `$ pip install Flask`: Flask 설치

```python
#hello.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

* `$ FLASK_APP=hello.py flask run`: 서버 실행
* `ctrl + click`  사이트 주소 들어가서 서버 동작 확인

* route: 실제 주소창에 나오는 주소값

* variable routing: 명시된 주소가 아니라 변수에 주소값이 들어가서 바뀜

  * ```python
    #hello.py
    from flask import Flask, render_template
    import random
    app = Flask(__name__)
    
    # @:데코레이터
    @app.route("/ssafy")
    def ssafy():
        return "This is SSAFY"
    
    #variable routing
    @app.route("/greeting/<string:name>")
    def greeting(name):
        return f"반갑습니다! {name}님"
    ```

  * `from 메서드 import 모듈`

  * `@app.route(" /'route명'/<string:'변수명>' ")`

  * `http://127.0.0.1:5000/greeting/민수` 

#### Flask 템플릿(Template)

* `minsu/day01/mysite/`에 'templates' 폴더 추가

* `minsu/day01/mysite/templates/` (templates라는 이름으로 써야함)에 'hi.html' 파일 추가

* `from flask import render_template`
* 수정중

```python
#hello.py
@app.route("/hi/<string:name>")
def hi(name):
    return render_template('hi.htm', name_in_htm=name)
```

```html
<!-- hi.htm -->
<style>
h1{
    color : red
}
</style>
<h1>만나서 반갑습니다! {{ name_in_htm }} 님</h1>
```

* 네이버 검색 .py

```python
#hello.py
@app.route("/fake_naver")
def fake_naver():
    return render_template('fake_naver.htm')
```

* 네이버 검색. htm

```html
<style>
    .naver{
        color : green
    }
</style>
<h1 class="naver">NAVER</h1>
<form action="https://search.naver.com/search.naver">
    <input type="text" name="query">
    <input type="submit">
</form>
<h1>DAUM</h1>
<form action="https://search.daum.net/search">
    <input type="text" name="q">
    <input type="submit">
</form>
```

## DAY 04

### JSON

* Python의 딕셔너리와 비슷하고 서로 왔다갔다 호환 가능

### Dictionary  (dict.py 실습)

---

* API를 활용하는데에 있어 가장 많이 사용되는 자료형. 웹을 하면서 계속 만나게 될 자료형.
* `key`와 `value`의 구조
* `key`는 `string`, `integer`, `float`, `boolean` 가능하다. (list, dictionary는 안된다.)
* `value`는 모든 자료형이 가능하다. `list` 또는  `dictionary`도 가능하다.



* 딕셔너리 선언 및 초기화

  * `딕셔너리 변수 = {key:value, key:value, key:value,}` 마지막 data 다음 ,(trailing commas)
  * `변수 = dict(key:value)`
    * dict() 사용 시 key가 '문자열'이라도 '' 없이 넣는다.

* 딕셔너리 내용 추가

  * `변수[key] = value`

* 딕셔너리 중첩

  - ```
    변수 = {
    	key1: {
    			key2:value2, key2:value2
           }
     }
    ```

  - ```python
    idol = {
        'bts': {
            '지민':24,
            'RM':25,
        }
    }
    ```

* 딕셔너리 내용 가져오기

  * `print(변수[key])`

  * ```python
    idol['bts'] #=> {'지민':24,'RM':25,}
    idol['bts']['RM'] #=> 25
    ```

* 딕셔너리 반복문 활용

```python
#기본활용
for key in lunch:
    print(key)  #=> key
    print(lunch[key]) #=> value

# key만 가져오기 : .keys()
for key in lunch.keys():
    print(key)

# value만 가져오기 : .values()
for value in lunch.values():
    print(value)
```

```python
# item (key, value) item 가져오기 : .items()
for key, value in lunch.items():
    print(key, value)
# => 중국집 02-123-123
# lunch.items() #=> [('중국집','02'), ...] tuple로 출력
```

```python
# item index 접근으로 item 가져오기
for item in lunch.items():
    print(item[0], item[1])
# => 중국집 02-123-123
```

* 여러 변수 정의

```python
#자료형 개수와 자료형 길이가 같으면 파이썬에서 각각 넣어준다
a, b = 1, 2
print(a)
print(b)
```

* Quiz.  반 평균을 구하시오.

```python
# 반 평균을 구하시오.
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100,
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100,
    },
    'c': {
        '수학': 100,
        '국어': 100,
        '음악': 100,
    }
}
```

```python
# 방법 1 python style?
total_score = 0
cnt = 0
for person_score in scores.values():
    for subject_score in person_score.values():
        total_score += subject_score
        cnt += 1
print(total_score/cnt)

# 방법 2 C style?
total_score = 0
cnt = 0
for student in scores:
    for sub_score in scores[student]:
        total_score += scores[student][sub_score]
        cnt += 1
print(total_score/len_cnt)    
```

* Quiz. 도시별 최근 3일의 온도 평균은?

```python
# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 6],
    '대전': [-3, -6, 2],
    '광주': [-0. -2, 10],
    '구미': [2, -2, 9],
}
```

```python
# 1 반복
for city_name, temp in city.items():
    total_temp = 0
    for t in temp:
        total_temp += t
    avg_temp = total_temp/len(temp)
    print(f'{city_name} : {round(avg_temp,2)}')
```

```python
# 2 내장함수
    total_temp = sum(temp)/len(temp)
```

##### Quiz. dict_advanced

```python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "junwoo",
            "manager": "pro-gm",
            "class president": "엄윤주",
            "groups": {
                "1조": ["강대현", "권민재", "서민수", "이규진"],
                "2조": ["박재형", "서민호", "윤종원", "이지현"],
                "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}
```

```python
# 2 python standard library에 'requests'가 있나요? : 접근 및 list in
library = ssafy["language"]["python"]["python standard library"]
print('requests' in library)
```

```python
# 4 ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
for key in ssafy["language"].keys():
    print(key)
language = ssafy["language"]
for key in language.keys():
    print(key)
```

```python
# 6 framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
for name, des in ssafy["language"]["python"]["frameworks"].items():
    print(f'{name}는 {des}이다.')
```

### Github

* `$ git pull`: 수정 사항 정리

* `gitignore` : git으로 관리하지 않는 파일 설정
  * master 위치에 `gitignore` 파일 생성
  * `https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore`복사

### Flask  ping pong

---

* `ping`페이지와 `pong`페이지를 만들어 왔다갔다 할 수있게 만든다.
* `request.args`: 딕셔너리와 같다

* `print(request.args['name'])`: 'min'을 입력하면 웹페이지는* /ping?name=min
* `render_template( )`: ()안은 데이터를 넘겨줄 html
  * ex) `render_template('ping.htm')`

###### 이미지추가

* `<img src="{{ url_for('static',filename='이미지 파일명') }}" alt = "이미지 설명">`
  * `{{ }}`: jinja

````python
# hello.py
# 신이 나를 만들 때
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ping') # @app.route()웹페이지 이름
def ping():
    return render_template('ping.htm') # render_template(): 데이터를 넘겨줄 html

@app.route('/pong')
def pong():
    name = request.args['name']
    result = random.choice(['image_1.png', 'image_2.png', 'image_3.png','image_4.png'])
    return render_template('pong.htm', name_in_htm = name, result = result)
````

```html
<h1>PING! </h1>
<!-- 하이퍼링크 -->
<a href="/pong">Pong</a>
<!-- 어떠한 페이지로 이동을 할지 주소를 입력한다 -->
<form action="/pong">
    <input type="text" name="name"> <!--텍스트 입력창: text형태로 "name"을 /pong페이지로 넘긴다-->
    <input type="submit">   <!-- 버튼 -->
</form>
```

```html
<h1>PONG! </h1>
<a href="/ping">Ping</a>
<h2>신이 {{ name_in_htm }}님을 만들때</h2>
<h3>{{ result }}</h3>
<img src="{{ url_for('static',filename=result) }}" alt = "이미지 설명">
```



### 문제해결

1. 숫자 입력받기 

* `list(map(int, input('숫자를 공백으로 구분해서 쓰세요').split()))`

