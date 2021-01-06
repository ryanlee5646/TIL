import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"

mem = req.urlopen(url)

# print(type(mem))
# print(type({}))
# print(type([]))
# print(type(()))

# print("geturl", mem.geturl())
# print("status", mem.status) # 200, 404, 403, 500
# print("headers", mem.getheaders())
# print("info", mem.info())
# print("code", mem.getcode())
# print("read", mem.read())
# print("read", mem.read(50).decode("utf-8")) # euc-kr ...
print(urlparse("http://www.encar.com?test=test"))
