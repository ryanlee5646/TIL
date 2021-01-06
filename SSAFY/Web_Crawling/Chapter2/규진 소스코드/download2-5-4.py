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
h1 = soup.select("div#main > h1") # select를 사용하게 되면 리스트 형태로 저장됌
print("h1", h1)
print("h1", type(h1))
print(*h1)
for i in h1: # 리스트형태는 바로 스트링으로 출력을 못하기 때문에 for으로 요소를 꺼내줘야함
    print(i.string)

h2 = soup.select_one("div#main > h1") # 가지고올 Selector가 하나라면 select_one으로 접근해서 바로 스트링출력 가능
print('h1', h2.string)

list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li >>>", li.string)
