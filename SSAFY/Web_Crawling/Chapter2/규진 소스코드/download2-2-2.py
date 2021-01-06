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

f = down.urlopen(imgUrl).read()
f2 = down.urlopen(htmlURL).read()

# 방법 1
saveFile1 = open(savePath1, 'wb') # w: write, r : read, a : add/ wb= binary로 쓰겠다
saveFile1.write(f) # 웹에서 가져온 resource를 읽겠다
saveFile1.close()
# 자바든 python이든 항상 입출력 작업이나 DB 데이터 커넥션 작업을 하면 리소스를 반납해줘야함

# 방법 2 (이 방법을 더 선호) with를 벗어나면 close()가 자동으로 실행, 더 간결!
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
