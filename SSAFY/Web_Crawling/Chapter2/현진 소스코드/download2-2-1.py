import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="http://post.phinf.naver.net/MjAxODA4MDFfMjMw/MDAxNTMzMDg4NDAwMTE0.gDPRGifP9tYmNRSxOvNhKQfi1qsyR4luus9bgZdI6uIg.yzhhIvD7AWlpOb4OK1vOA5F4HLVxCEfGb57k9gndK94g.JPEG/Iq_cU6Sac798YMzN22yJSvrEU2GM.jpg"
htmlURL ="https://google.com"

savePath1 ="c:/test1.jpg"
savePath2 ="c:/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1) # w : write, r : read , a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2: # with가 끝나는 부분에서 자동으로 close가 된다.
    saveFile2.write(f2)

print("다운로드 완료!")
