## 섹션 2. 파이썬 기초 스크랩핑 -1



### BeautifulSoup 사용법 및 간단 웹 파싱 기초 (1)

* 선택자(Selector)

* BeautifulSoup 설치

  : `pip install beautifulsoup4`

* BeautifulSoup 간단 파싱 학습

  ```python
  from bs4 import BeautifulSoup
  import sys
  import io
  
  sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
  sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
  
  html = """
  <html>
  <body>
  <h1>파이썬 BeautifulSoup 공부</h1>
  <p>태그 선택자</p>
  <p>CSS 선택자</p>
  </body>
  </html>
  """
  soup = BeautifulSoup(html, 'html.parser')
  print('soup', type(soup))
  print('prettify',soup.prettify()) # 들여쓰기 후 출력
  
  h1 = soup.html.body.h1
  print('h1',h1)
  p1 = soup.html.body.p
  print('p1',p1)
  p2 = p1.next_sibling.next_sibling
  # .next_sibling을 한번만 쓰면 공백이 출력 된다. (줄바꿈 기호가 생략되어있기때문)
  print('p2',p2)
  p3 = p1.previous_sibling.previous_sibling
  print('p3',p3)
  # p3 <h1>파이썬 BeautifulSoup 공부</h1>
  
  ```

* urljoin, find_all, select_one, next_sibling, previous_sibling

  ```python
  from bs4 import BeautifulSoup
  import sys
  import io
  
  sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
  sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
  
  html = """
  <html><body>
    <ul>
      <li><a href="http://www.naver.com">naver</a></li>
      <li><a href="http://www.daum.net">daum</a></li>
      <li><a href="https://www.google.com">google</a></li>
      <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
  </body></html>
  """
  
  soup = BeautifulSoup(html, 'html.parser')
  
  links = soup.find_all("a")
  # print('links',type(links))
  a = soup.find_all("a",string="daum")
  print('a',a)
  b = soup.find_all("a", limit=3)
  print('b',b)
  # limit로 원하는 만큼 불러올수 있음
  c = soup.find_all(string=["naver","google"])
  print('c',c)
  # type 은 ResultSet
  
  for a in links:
      print('a',type(a),a)
      href = a.attrs['href']
      txt = a.string
      print('txt >> ',txt,'href >> ',href)
  
  ```

* Selector

  ```python
  from bs4 import BeautifulSoup
  import sys
  import io
  
  sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
  sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
  
  html = """
  <html><body>
  <div id="main">
    <h1>강의목록</h1>
    <ul class="lecs">
      <li>Java 초고수 되기</li>
      <li>파이썬 기초 프로그래밍</li>
      <li>파이썬 머신러닝 프로그래밍</li>
      <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
  </div>
  </body></html>
  """
  
  soup = BeautifulSoup(html, 'html.parser')
  h1 = soup.select_one("div#main > h1")
  print('h1',h1.string)
  # h1의 type은 string이 아니고 list 이다.
  list_li = soup.select("div#main > ul.lecs > li")
  for li in list_li:
      print("li >>>",li.string)
  ```

* BeutifulSoup HTML파일 파싱 실습

  ```python
  html = """
  <html><body>
    <ul>
      <li><a href="http://www.naver.com">naver</a></li>
      <li><a href="http://www.daum.net">daum</a></li>
      <li><a href="https://www.google.com">google</a></li>
      <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
  </body></html>
  """
  
  soup = BeautifulSoup(html, 'html.parser')
  print(soup.find(id="naver").string) # id값을 가져올 수 있음
  
  # 정규 표현식
  import re
  soup = BeautifulSoup(html, 'html.parser')
  print(soup.find(id="naver").string)
  li = soup.find_all(href=re.compile(r"^https://"))
  # ex) r"da"일 경우 da가 포함된것들이 출력
  
  for e in li:
      print(e.attrs['href'])
  ```

  

* 더욱 다양하게 CSS 선택자 사용해 보기

* fiond, select 실습 예제

  ```python
  from bs4 import BeautifulSoup
  import sys
  import io
  
  sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
  sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
  
  fp = open("food-list.html",encoding="utf-8")
  soup = BeautifulSoup(fp, "html.parser")
  
  # Select
  print("1", soup.select("li:nth-of-type(4)")[1].string) #각 li 태그 그룹의 4번째 요소 선택
  print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
  print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string)
  print("4", soup.select("#ac-list > li.alcohol.high")[0].string)
  # select는 리스트 이므로 인덱스 형식으로 접근해야한다.
  
  # find
  param = {"data-lo": "cn", "class": "alcohol"}
  print("5", soup.find("li", param).string)
  # 가독성이 좋다.
  print("6", soup.find(id="ac-list").find("li",param).string)
  # 위에서부터 차례대로 접근한것
  
  for ac in soup.find_all("li"):
      if ac['data-lo'] == 'us':
          print('data-lo == us', ac.string)
  
  ```

* 함수와 람다식

  ```python
  from bs4 import BeautifulSoup
  import sys
  import io
  
  sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
  sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
  
  fp = open("cars.html",encoding="utf-8")
  soup = BeautifulSoup(fp, "html.parser")
  
  # gkatntlr
  def car_func(selector):
      print("car_func", soup.select_one(selector).string)
  
  # 람다식
  car_lambda = lambda q : print("car_lambda", soup.select_one(q).string)
  
  car_func("#gr")
  car_func("li#gr")
  car_func("ul > li#gr")
  car_func("#cars #gr")
  car_func("#cars > #gr")
  car_func("li[id='gr']")
  
  car_lambda("#gr")
  car_lambda("li#gr")
  car_lambda("ul > li#gr")
  car_lambda("#cars #gr")
  car_lambda("#cars > #gr")
  car_lambda("li[id='gr']")
  
  print("car_func", soup.select("li")[3].string)
  print("car_func", soup.find_all("li")[3].string)
  ```

  

### BeutifulSoup 사용법 및 웹 파싱 실습(1)

* fake-useragent 설치

  :  `pip install fake-useragent`

* 다음(daum) 금융 시가 총액 상위 종목 가져오기

  ```python
  import io
  import json
  import sys
  import urllib.request as req
  
  from fake_useragent import UserAgent
  
  sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
  sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
  
  # Fake Header 정보
  ua = UserAgent()
  
  # 헤더 선언
  headers = {
      'User-Agent': ua.ie,
      'referer': 'https://finance.daum.net/'
  }
  
  # 다음 주식 요청 URL
  url = "https://finance.daum.net/api/search/ranks?limit=10"
  
  # print(request.get_method())   #Post or Get 확인
  # print(request.get_full_url()) #요청 Full Url 확인
  
  # 요청
  res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
  
  # 응답 데이터 확인(Json Data)
  # print('res', res)
  
  # 응답 데이터 str -> json 변환 및 data 값 저장
  rank_json = json.loads(res)['data']
  
  # 중간 확인
  print('중간 확인 : ', rank_json, '\n')
  
  for elm in rank_json:
      # print(type(elm)) #Type 확인
      print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']), )
  ```

  

* 네이버(naver) 금융 시가 Top 10 종목 가져오기

  ```python
  from bs4 import BeautifulSoup
  import urllib.request as req
  import sys
  import io
  
  sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
  sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
  
  url = "http://finance.naver.com/sise/"
  res = req.urlopen(url).read().decode('cp949')  # utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐
  
  # 중간 출력
  # print(res)
  
  soup = BeautifulSoup(res, "html.parser")
  
  top10 = soup.select("#popularItemList > li > a")
  
  # 파싱 확인
  # print(top10)
  
  print('네이버 주식 인기검색 종목 10위')
  for i, e in enumerate(top10, 1):
      print('순위 : {}, 이름 : {}'.format(i, e.string))
  ```

  

* 인프런(inflearn) 추천강좌 10개 가져오기 

```python
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

recommand = soup.select("ul.slides")[0]

for i,e in enumerate(recommand,1):
    print(i,e.select_one("h4.block_title > a").string)
```

