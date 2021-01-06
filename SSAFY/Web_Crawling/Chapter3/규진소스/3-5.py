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
ua = UserAgent()
# print(ua.ie) # explore
# Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
# print(ua.chrome) # chrome
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36
# print(ua.random) # linux
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14

with requests.Session() as s:
    # URL 연결
    s.get(URL)
    #Login 정보 Payload
    LOGIN_INFO = {
        'identification': 'ryanlee5646',
        'password':'rbwlsl91',
        'csrfmiddlewaretoken':s.cookies['csrftoken']
    }
    # 요청
    response = s.post(URL,data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'
    })

    #HTML 결과 확인
    # print('response',response.text)

    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select("table.table-responsive > tbody > tr")
        for i in projectList:
            print(i.find('th').string, i.find('td').text)
