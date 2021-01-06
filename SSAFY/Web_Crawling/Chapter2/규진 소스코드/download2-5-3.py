from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
      </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
# print('links', type(links))
a = soup.find_all("a",string='daum') # string이 daum인 요소만 갖고옴
print('a', a)

b = soup.find("a") # find는 하나만 가져옴(가장 첫번째 것)
print('b', b)

c = soup.find_all("a", limit=2) # limit까지의 수만큼 가져옴
print('c', c)

d = soup.find_all(string=["naver", "google"]) # 해당 스트링을 가지고옴
print('d', d)

for a in links:
    print('a', type(a), a)
    href = a.attrs['href'] # attrs를 사용하면 key=value형태로 반환 (href가 키인 value(링크)를 반환)
    txt = a.string
    print('txt >>', txt, 'href >>', href)
