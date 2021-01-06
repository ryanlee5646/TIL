from bs4 import BeautifulSoup
import io
import urllib.request as req
import sys


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "http://finance.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser") # daum 금융페이지의 html코드를 가지고옴
# print("soup", soup.prettify())

top = soup.select("ul#topMyListNo1 > li")

print(top)

for i,e in enumerate(top): # 여기서 e는 아직 객체의 형태
    print(i, ",",e.find("a").string, ":", e.find("span").string) # e에서 a태크를 가진 요소에 접근
# 1, 삼성전자 : 2,442,000
# 2, SK하이닉스 : 72,900 ...
