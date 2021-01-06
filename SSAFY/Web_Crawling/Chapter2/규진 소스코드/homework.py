import sys
import io
import urllib.request as down

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1232/1232463/f559a07b762c847abd0e_20190516105853290_2.jpg"
videoUrl = "https://tvetamovie.pstatic.net/libs/1240/1240992/99cc84da2fad76509100_20190524163455876.mp4-pBASE-v0-f82522-20190524163820588.mp4"

savePath1 = "C:/Users/student/Desktop/img1.jpg"
savePath2 = "C:/Users/student/Desktop/video1.mp4"

# 방법 1
# down.urlretrieve(imgUrl, savePath1)
# down.urlretrieve(videoUrl, savePath2)

# 방법 2
# f1 = down.urlopen(imgUrl).read()
# f2 = down.urlopen(videoUrl).read()
#
# saveFile1 = open(savePath1, 'wb')
# saveFile1.write(f1)
# saveFile1.close()
#
# saveFile2 = open(savePath2, "wb")
# saveFile2.write(f2)
# saveFile2.close()

# 방법 3
f1 = down.urlopen(imgUrl).read()
f2 = down.urlopen(videoUrl).read()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f1)

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)



print("다운로드 완료!")
