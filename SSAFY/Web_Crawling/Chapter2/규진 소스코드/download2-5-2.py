from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부 </h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser') # 첫번째 인자로는 URL, html등을 받음, 두번째 인자로 parser를 지정
# print('soup', type(soup))
# print('prettify',soup.prettify()) # prettify 함수를 쓰면 들여쓰기를 해줌
<li>



h1 = soup.html.body.h1
print('h1',h1)
print('h1', type(h1))
print('h1', h1.string) # 스트링만 출력

p1 = soup.html.body.p
print('p1', p1)

p2 = p1.next_sibling.next_sibling
# 같은 형제위치에 있는 selector가 여러개면 next_sibling으로 '다음'' 위치태그 접근 가능
# 줄바꿈했을 경우 next_sibling을 한번 더 입력 해야함
print('p2', p2)

p3 = p2.previous_sibling.previous_sibling
# 같은 형제위치에 있는 selector가 여러개면 next_sibling으로 '이전' 위치태그 접근 가능
# 더 이상 형제가 없다면 그 위에 상위 부모 selector로 이동
print('p3', p3)

print("h1 >> ", h1.string)
print("p >> ", p1.string)
print("p >> ", p2.string)

# 사실상 현업에서 중간에 코드를 삽입하고 수정하는 경우가 많기때문에 이렇게 수동으로 접근하는 방법은 잘 쓰이지 않음
