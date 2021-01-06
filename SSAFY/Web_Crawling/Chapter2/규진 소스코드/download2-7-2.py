from bs4 import BeautifulSoup
import io
import urllib.request as req
import sys


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('cp949') # 한글이 깨지므로 cp949로 디코드
soup = BeautifulSoup(res,"html.parser") # daum 금융페이지의 html코드를 가지고옴

top10 = soup.select('#siselist_tab_0 > tr')

i = 0
for i,e in enumerate(top10):
    if e.find("a") is not None: # a태그를 찾았을 때 None이 아니라면
        print(i-1,e.select_one(".tltle").string) # a태그가 없으면 none 반
            # 고의적으로 종목명의 id값이 title이 아닌 tltle로 되있음
        i += 1
        # 현재는 top5까지만 나와있음
