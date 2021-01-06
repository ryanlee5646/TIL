import urllib.request as request
import simplejson as json
import os.path

# url

url = "https://api.github.com/repositories"

# 경로 & 파일명
savename = "C:/Users/student/Desktop/section4/member.json"

if not os.path.exists(url):
    request.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding='utf-8'))
items = json.loads(open(savename, 'r', encoding='utf-8').read())

# 출력
for item in items:
    print(item['full_name'] + "-" + item['owner']['url'])
