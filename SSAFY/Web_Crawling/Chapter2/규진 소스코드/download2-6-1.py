from bs4 import BeautifulSoup
import sys
import io
import re # regex


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a id="naver" href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
      </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="naver").string)
li = soup.find_all(href=re.compile(r"^https://")) # 정규식표현 ^은 https://로 시작하는 문자열 

print('li', li)
for e in li:
    print(e.attrs['href'])
