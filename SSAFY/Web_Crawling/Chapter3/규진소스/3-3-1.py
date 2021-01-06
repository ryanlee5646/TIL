import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# r = requests.get("https://api.github.com/events")
# r.raise_for_status() # requests에서 에러가 발생했을 때 예외를 발생 시켜줌
# # 페이지가 없으면 404에러를 발생시킴
# print(r.text)

jar = requests.cookies.RequestsCookieJar()

jar.set('name','kim',domain='httpbin.org',path='/cookies')

# r = requests.get('http://httpbin.org/cookies',cookies=jar)
# r.raise_for_status()
# print(r.text)

# r = requests.get('https://github.com',timeout=3)
# print(r.text)

# r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
# print(r.text)

payload1 = {'key1':'value1', 'key2':'value2'}
payload2 = (('key2','value2'),('key3','value3'))
payload3 = {'some':'nice'}

r = requests.post("http://httpbin.org/post", data=payload1) # form데이터로 요청
print(r.text)

r = requests.post("http://httpbin.org/post", data=json.dumps(payload3)) # json데이터로 요청
print(r.text)
