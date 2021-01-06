import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream=True)
# print(r.text)
# print(r.encoding) # 위 사이트는 encoding형태가 none으로 되있음
# print(r.json())

if r.encoding == None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    # print(line)
    b = json.loads(line) # dict형태
    # print(type(b))
    # print(b['origin'])
    for e in b.keys():
        print("key:", e, "vlaues:",b[e])
