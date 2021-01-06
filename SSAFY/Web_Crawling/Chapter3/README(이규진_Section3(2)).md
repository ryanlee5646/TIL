# Section 3 - 파이썬 고급 스크랩핑

## 파이썬 requests 통신 실습(로그인 처리) 고급(2) - 위시캣

#### ● 오늘 내용 정리

1. **보안 토큰(csrf Token), Fake User-agent, Header Payload** 처리
2. **위시캣(wishket)** 사이트 로그인 처리 후 정보 가져오기



**Fake-UserAgent** - https://pypi.python.org/pypi/fake-useragent

`pip install fake-useragent`



#### 1. 위시캣

```python
import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 요청 URL
URL = 'https://www.wishket.com/accounts/login/'

#Fake User-Agent 생성
ua = UserAgent() # 유저 우회접속같은 거?
print(ua.ie) # explore
# Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
print(ua.chrome) # chrome
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36
print(ua.random) # linux
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14

with requests.Session() as s:
    # URL 연결
    s.get(URL)
    #Login 정보 Payload
    LOGIN_INFO = {
        'identification': '',
        'password':'',
        'csrfmiddlewaretoken':s.cookies['csrftoken']
    }
    # 요청
    response = s.post(URL,data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'
    })

    #HTML 결과 확인
    # print('response',response.text)

    if response.status_code == 200 and response.ok: # 데이터 가져오기
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select("table.table-responsive > tbody > tr")
        for i in projectList:
            print(i.find('th').string, i.find('td').text)
```



## 웹 브라우저 없는 스크랩핑 및 파싱 실습(1)

#### ● 오늘 내용 정리

1. Selenium 개념 및 설치(크롬, 파이어폭스)
2. PhantomJS 개념 및 설치
3. Selenium을 이용한 사이트 이미지 캡쳐 테스트 및 예제 작성(전체)
4. Selenium을 이용한 인프런(Inflearn) 로그인 자동화 처리하기
5. Selenium & Chrome Or Firefox Headless Mode 최종 세팅

#### 실습(과제): encar(엔카) 사이트 접속 후 자동으로 매물 조회하기

Selenium 문서: http://selenium-python.readthedocs.io/index.html

phantomjs 문서: http://phantomjs.org/documentation/

다운로드: http://phantomjs.org/download.html

다운로드(Chrome): https://sites.google.com/a/chromium.org/chromedriver/downloads

#### ● Selenium 사용하는 이유

=> urllib통해 파싱, requests를 통해 로그인처리, fake-useragent를 통해 브라우저를 속임

이거를 하는 이유는 웹브라우저를 사용하지 않기 때문에 서버에 거절을 당함, 경우에 따라서는 데이터를 못가져오거나, 가져오는 과정이 어려움



### 1. Selenium + 크롬

### 2. Selenium + 파이어폭스 (가장 권장)

### 3. Selenium + PhantomJS

#### * Selenium설치 => `pip install selenium`

```python
import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('C:/section3/chrome/chromedriver')

driver.set_window_size(1920, 1280)
driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("c:/Website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("c:/Website2.png")
driver.quit()
```



## 웹 브라우저 없는 스크랩핑 및 파싱 실습(2)

#### 오늘 내용 정리

1. Selenium을 이용한 네이버 카페 자동으로 글쓰기
2. 네이버 로그인 처리 후 회원 리스트 정보 가져오기
3. Class Module 실습 작성 
4. 자주 사용하는 Selenium 레퍼런스(Reference) 문서 훑어보기

#### 실습(과제): 권한이 필요한 사이트 게시판 페이지 별 리스트 추출해보기



```python
import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeMemberExr:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="c:/section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    #네이버 카페 회원 1페이지 정보 리스트 추출
    def getMemberList(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('')
        self.driver.find_element_by_name('pw').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.get('http://cafe.naver.com/CafeMemberView.nhn?m=view&clubid=19756449')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame('innerframe')
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        return soup.select('div.mem_wrap > div.mem_list div.ellipsis.m-tcol-c')

    #네이버 회원 리스트 출력 및 저장
    def printMemberList(self,list):
        f = open("C:/memberList.txt",'wt')
        for i in list:
            f.write(i.string.strip()+"\n")
            print(i.string.strip())
        f.close()

    # 소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit()  #Seleninum 전체 프로그램 종료
        print("Removed driver Object")

#실행
if __name__ == '__main__':
    #객체 생성
    a = NcafeMemberExr()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.printMemberList(a.getMemberList())
    #종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a

```

