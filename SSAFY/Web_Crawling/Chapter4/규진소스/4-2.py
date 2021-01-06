import sys
import io
import urllib.request as request
from bs4 import BeautifulSoup
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 다운로드 url
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "C:/Users/student/Desktop/section4/forecast.xml"

if not os.path.exists(savename): # 이 경로에 파일이 없다면 저장경로를 설정
    request.urlretrieve(url, savename)
    print("다운로드 확인")

# BeautifulSoup 파싱
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')


# 지역확인
# xml파일을 파싱할때는 find쓰는게 select쓰는것 보다 효율적
# 특정 아이디 값이 없음
info = {}
for location in soup.find_all("location"):
    loc = location.find("city").string
    # print(loc)
    weather = location.find_all("tmn")
    # print(weather)
    if not (loc in info):
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)
# print(info)
print(info.keys())
print(info.values())
# 각 지역별 날씨 텍스트 쓰기
with open('C:/Users/student/Desktop/section4/forecast.txt',"wt") as f:
    for loc in sorted(info.keys()):
        print("+",loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:
            print("-",n)
            f.write('\t'+str(n)+'\n')
