import pytube
import os
import subprocess # 파이썬을 실행하면서 별도의 프로세스를 생성해서
# 터미널이나 커맨드에 명령어를 실행 할 수 있고 그 반환값을 가져 올 수 있다.


yt = pytube.YouTube("https://youtu.be/junvn7qKikc") # "" 안에 다운 받을 URL
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, ',', videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "C:/youtube" # 다운받을 URL 경로

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir,newFileName),
# ffmpeg를 환경변수로 등록하면 어디에서나 코드를 실행해도 관계없지만
# 그렇지 않은 경우에는 파이썬 코드를 영상을 받을 위치에 옮겨줘야한다.
])

print("동영상 다운로드 및 mp3 변환 완료")
