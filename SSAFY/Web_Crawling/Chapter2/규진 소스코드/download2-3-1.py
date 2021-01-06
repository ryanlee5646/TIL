import sys
import io
import urllib.request as req
from urllib.parse import urlparse


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"

mem = req.urlopen(url)

# print(type(mem))
# print("geturl", mem.geturl())
# print("status",mem.status) # 이런 페이지오류에 대해서 예외처리를 해줘야하므로 알아야함
# # 200(정상), 404(페이지없음), 403(접속안됌), 500(서버문제)
# print("headers", mem.getheaders())
#
# print("info", mem.info())
# print("code", mem.getcode())
# print("read",mem.read(105).decode("utf-8")) # decode는 글자가 깨지는걸 해결
#
print(urlparse("http://www.encar.com?test=test"))
