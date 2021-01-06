from bs4 import BeautifulSoup
import io
import urllib.request as req
import urllib.parse as rep # 유니코드로 변환하는 코드
import sys


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")

url = base + quote

res = req.urlopen(url).read()

soup = BeautifulSoup(res, "html.parse")

recommand = soup.select("ul.slides")[0] # id가 slides인 항목이 3갠데 원하는 카테고리는 첫번째 slide

for i,e in enumerate(recommand,1):
    print(e.select_one("h4.block_title > a").string)
