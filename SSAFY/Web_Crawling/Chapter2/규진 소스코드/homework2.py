from bs4 import BeautifulSoup
import urllib.request as request
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://www.naver.com/"
res = request.urlopen(url).read()

soup = BeautifulSoup(res,"html.parser")

popular = soup.select(".ah_l > .ah_item > .ah_a > .ah_r")
search = soup.select(".ah_l > .ah_item > .ah_a > .ah_k ")

for i in range(0,20):
    print("{} {}".format(popular[i].string, search[i].string))
