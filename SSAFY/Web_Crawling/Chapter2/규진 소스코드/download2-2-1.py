import sys
import io
import urllib.request as down

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('hi')
print('하이')

imgUrl = "http://post.phinf.naver.net/MjAxODA4MDFfMjMw/MDAxNTMzMDg4NDAwMTE0.gDPRGifP9tYmNRSxOvNhKQfi1qsyR4luus9bgZdI6uIg.yzhhIvD7AWlpOb4OK1vOA5F4HLVxCEfGb57k9gndK94g.JPEG/Iq_cU6Sac798YMzN22yJSvrEU2GM.jpg"
htmlURL = "https://google.com"

savePath1 = "c:/test1.jpg"
savePath2 = "c:/index.html"

down.urlretrieve(imgUrl, savePath1)
down.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
