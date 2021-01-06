# Section 2  - 파이썬 기초 스크랩핑



## 크롬(Chrome) 개발자 도구

#### ● 기본개념

1. DOM 구조 분석(요소검사)

2. 선택자(Selector) 추출

   - 개발자 도구를 통해 내가 원하는 데이터의 Selector을 가져올 수 있는지

3. Console 도구

4. Source - 로딩 한 리소스 분석 및 디버깅

5. 네트워크 탭 및 기타

   

## 파이썬 urllib을 활용한 웹에서 필요한 데이터 추출하기(1)

#### ● 오늘 배울 내용 정리

1. Urlretrieve
2. urlopen
3. urlretrieve Vs urlopen 비교
4. open, write, close
5. with

https://wikidocs.net/26

https://docs.python.org/3/library/urllib.request.html



* Atom은 한글 텍스트를 콘솔창에 출력하면 글이 깨짐 그래서 아래 코드를 상단에 추가해야함

  * ```python
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
    
    ```

### 1. Urlretrieve

* Url을 통해 원하는 정보를 하드 디스크에 다운 받음

  * ```python
    imgUrl = # 이미지다운 "http://post.phinf.naver.net/MjAxODA4MDFfMjMw/MDAxNTMzMDg4NDAwMTE0.gDPRGifP9tYmNRSxOvNhKQfi1qsyR4luus9bgZdI6uIg.yzhhIvD7AWlpOb4OK1vOA5F4HLVxCEfGb57k9gndK94g.JPEG/Iq_cU6Sac798YMzN22yJSvrEU2GM.jpg"
    htmlURL = "https://google.com" # Url을 html파일로 다운
    
    savePath1 = "c:/test1.jpg"
    savePath2 = "c:/index.html"
    
    down.urlretrieve(imgUrl, savePath1)
    down.urlretrieve(htmlURL, savePath2)
    
    print("다운로드 완료!")
    ```

  * 

### 2. Urlopen

* Url을 통해 원하는 정보를 하드 디스크에 다운 받음

  ```python
  import sys
  import io
  import urllib.request as down
  
  sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
  sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
  
  imgUrl = "http://post.phinf.naver.net/MjAxODA4MDFfMjMw/MDAxNTMzMDg4NDAwMTE0.gDPRGifP9tYmNRSxOvNhKQfi1qsyR4luus9bgZdI6uIg.yzhhIvD7AWlpOb4OK1vOA5F4HLVxCEfGb57k9gndK94g.JPEG/Iq_cU6Sac798YMzN22yJSvrEU2GM.jpg"
  htmlURL = "https://google.com"
  
  savePath1 = "c:/test1.jpg"
  savePath2 = "c:/index.html"
  
  f = down.urlopen(imgUrl).read()
  f2 = down.urlopen(htmlURL).read()
  
  # 방법 1
  saveFile1 = open(savePath1, 'wb') # w: write, r : read, a : add/ wb= binary로 쓰겠다
  saveFile1.write(f) # 웹에서 가져온 resource를 읽겠다
  saveFile1.close() 
  # 자바든 python이든 항상 입출력 작업이나 DB 데이터 커넥션 작업을 하면 리소스를 반납해줘야함 
  
  # 방법 2 (이 방법을 더 선호) with를 벗어나면 close()가 자동으로 실행, 더 간결!
  with open(savePath2, 'wb') as saveFile2:
      saveFile2.write(f2)
  
  print("다운로드 완료!")
  ```



### 3. urlretrieve Vs urlopen

* **`urlretrieve`** :  직접적으로 데이터를 바로 받아옴
  * 저장 -> open('r') -> 변수에 할당 -> 파싱 -> 저장 ( **다이렉트 저장** )
  * 사진을 단체로 (1000장씩) 한번에 다운 받는데 있어서 적합
* **`urlopen`**: 어떤 html을 받아서 중간에 내가 필요로 하는 데이터를 파싱(분류)할 거면 urlopen이 적합
  * **변수 할당** -> 파싱 -> 저장(db)  ( **변수에 할당함**)
  * 중간 작업에서 다운 받기전에 조건에 맞게 걸러내는데 적합



## 파이썬 urllib을 활용한 웹에서 필요한 데이터 추출하기(2)

#### ● 오늘 배울 내용 정리

1. Urlopen 파라미터(Parameter) 전달 방법
2. Type (자료형 알아보기)
3.  decode, geturl, status, getheaders, info, urlparse

● 실습(과제): 네이버 홈페이지 (상단, 우측 배너 광고) 저장해보기

https://wikidocs.net/26

https://docs.python.org/3/library/urllib.request.html



#### ● decode, geturl, status, getheaders, info, urlparse

```python
print("geturl", mem.geturl())
# => geturl http://www.encar.com/index.do

print("status",mem.status) # 이런 페이지오류에 대해서 예외처리를 해줘야하므로 알아야함
# 200(정상), 404(페이지없음), 403(접속안됌), 500(서버문제)

print("headers", mem.getheaders())
# => headers [('Date', 'Wed, 29 May 2019 06:44:21 GMT'), ('Set-Cookie', 'WMONID=ZCzo03q9Eo2; Expires=Thu, 28-May-2020 15:44:21 GMT; Path=/'), ('Content-Type', 'text/html; charset=EUC-KR'), ('Connection', 'close'), ('Content-Language', 'ko-KR'), ('Set-Cookie', 'JSESSIONID=G12dw3QvRzVLtx1qT8g0gJ8FltB9ERzpw1YKOGpa6kO09z2GUtRzJ0YQB2OAfnao.encarwas4_servlet_engine3;Path=/'), ('P3P', "CP='CAO PSA CONi OTR OUR DEM ONL'"), ('X-UA-Compatible', 'IE=Edge'), ('Transfer-Encoding', 'chunked')]

print("info", mem.info())
# => info Date: Wed, 29 May 2019 06:44:21 GMT
# Set-Cookie: WMONID=ZCzo03q9Eo2; Expires=Thu, 28-May-2020 15:44:21 GMT; Path=/
# Content-Type: text/html; charset=EUC-KR
# Connection: close
# Content-Language: ko-KR
# Set-Cookie:     JSESSIONID=G12dw3QvRzVLtx1qT8g0gJ8FltB9ERzpw1YKOGpa6kO09z2GUtRzJ0YQB2OAfnao.encarwas4_servlet_engine3;Path=/
# P3P: CP='CAO PSA CONi OTR OUR DEM ONL'
# X-UA-Compatible: IE=Edge
# Transfer-Encoding: chunked

print("code", mem.getcode())
# => code 200

print("read",mem.read(50).decode("utf-8")) # decode는 글자가 깨지는걸 해결
# => 


# from urllib.parse import urlparse를 import 해줘야함

print(urlparse("http://www.encar.com?test=test"))
# => ParseResult(scheme='http', netloc='www.encar.com', path='', params='', query='test=test', fragment='')

```



* 구글 검색창에 `my ip api` 검색후 `ipify` 에 접속

  * ```python
    https://api.ipify.org #복사하기
    ```

  * ```python
    import sys
    import io
    import urllib.request as req
    from urllib.parse import urlencode
    
    
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
    
    API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
    
    values = {
        'ctxCd' : '1012' # 동적으로 할당이 가능함
    }
    
    print('before', values)
    # => before {'ctxCd': '1012'}
    
    params = urlencode(values) # urlencode를 import해줌
    # 딕셔너리 형태를 format=json으로 변경
    
    print('after', params)
    # => after ctxCd=1012
    
    url = API + "?" + params # 동적으로 할당
    print("요청 url", url)
    
    reqData = req.urlopen(url).read().decode('utf-8') # json형태로 ip를 출력
    print("출력",reqData)
    ```

  * 

## 과제

#### ● 네이버 홈페이지(상단, 우측 배너(동영상) 광고 저장하기)

#### * urlretrieve 를 사용

```python
import sys
import io
import urllib.request as down

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1232/1232463/f559a07b762c847abd0e_20190516105853290_2.jpg"
videoUrl = "https://tvetamovie.pstatic.net/libs/1240/1240992/99cc84da2fad76509100_20190524163455876.mp4-pBASE-v0-f82522-20190524163820588.mp4"

savePath1 = "C:/Users/student/Desktop/img1.jpg"
savePath2 = "C:/Users/student/Desktop/video1.mp4"

down.urlretrieve(imgUrl, savePath1)
down.urlretrieve(videoUrl, savePath2)

print("다운로드 완료!")
```

#### *urlopen을 사용

```python
imgUrl = "https://ssl.pstatic.net/tveta/libs/1232/1232463/f559a07b762c847abd0e_20190516105853290_2.jpg"
videoUrl = "https://tvetamovie.pstatic.net/libs/1240/1240992/99cc84da2fad76509100_20190524163455876.mp4-pBASE-v0-f82522-20190524163820588.mp4"

savePath1 = "C:/Users/student/Desktop/img1.jpg"
savePath2 = "C:/Users/student/Desktop/video1.mp4"


f1 = down.urlopen(imgUrl).read()
f2 = down.urlopen(videoUrl).read()

saveFile1 = open(savePath1, 'wb')
saveFile1.write(f1)
saveFile1.close()

saveFile2 = open(savePath2, "wb")
saveFile2.write(f2)
saveFile2.close()
```

#### *with를 사용

```python
imgUrl = "https://ssl.pstatic.net/tveta/libs/1232/1232463/f559a07b762c847abd0e_20190516105853290_2.jpg"
videoUrl = "https://tvetamovie.pstatic.net/libs/1240/1240992/99cc84da2fad76509100_20190524163455876.mp4-pBASE-v0-f82522-20190524163820588.mp4"

savePath1 = "C:/Users/student/Desktop/img1.jpg"
savePath2 = "C:/Users/student/Desktop/video1.mp4"


f1 = down.urlopen(imgUrl).read()
f2 = down.urlopen(videoUrl).read()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f1)

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)
```



