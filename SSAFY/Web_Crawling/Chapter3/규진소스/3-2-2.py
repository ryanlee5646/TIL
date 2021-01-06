import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Response 상태 코드
s = requests.Session()
r = s.get("http://httpbin.org/get")
# print(r.status_code)
# print(r.ok)

# https://jsonplaceholder.typicode.com

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
# print(r.text)
print(r.json()) # 데이터를 json형태로 컨버트해줌
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content) # b가 붙음으로 바이너리 형태로 줄바꿈을 문자를 포함하여 가져옴
print(r.raw)
