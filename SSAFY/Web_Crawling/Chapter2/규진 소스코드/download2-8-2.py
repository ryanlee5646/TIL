from bs4 import BeautifulSoup
import urllib.request as request
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

base =
quote = rep.quote_plus("") # 한글을 유니코드로 변환시켜주는 함수
url = base + quote


res = request.urlopen(url)
savePath = "C:/Users/student/Desktop/imagedown/"

try:
    if not (os.path.isdir(savePath)): # 만약 이 경로에 폴더가 없다면
        os.makedirs(os.path.join(savePath)) # 폴더를 만들어라
except OSError as e: # 만약 폴더만들때 에러가 발생 했다면
    if e.errno != errno.EEXIST: # 폴더가 이미 존재한다는 에러가 났으면 그냥 아무것도 실행 안하면됨 그에 아니라면 폴더 만들기 실패
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")

for i, img_list in enumerate(img_list, 1):
    fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    request.urlretrieve(img_list['data-source'], fullFileName)

print("다운로드 완료")
