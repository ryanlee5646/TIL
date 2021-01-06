import sys
import io
import urllib.request as req
from urllib.parse import urlencode


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd' : '1012'
}

print('before', values)
params = urlencode(values) # urlencode를 import해줌
# 딕셔너리 형태를 format=json으로 변경
print('after', params)

url = API + "?" + params # 동적으로 할당
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8') # json형태로 ip를 출력
print("출력",reqData)
