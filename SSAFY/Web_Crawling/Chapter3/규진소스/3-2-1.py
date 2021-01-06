import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session() # Session을 열어주는 명령어,
# r = s.get("https://www.naver.com")  # PUT(FETCH), DELETE, GET, POST
# print('1', r.text)

# r = s.get('http://httpbin.org/cookies', cookies={'from':'myName'})
# print(r.text)

url = "https://httpbin.org/get"
headers = {'user-agent': 'myPythonApp_1.0.0'}

# r = s.get(url,headers=headers)
# print(r.text)

s.close() # 반드시 리소스 낭비를 위해 닫아줘야함

with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)
