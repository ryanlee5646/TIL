import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.parse as req
import urllib.request as req
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 로그인 유저정보
LOGIN_INFO = {
    'user_id': 'ID',
    'user_pw': 'PASSWORD',
    'user-submit': rep.quote_plus('로그인'),
    'user-cookie': 1
}

# Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('페이지 주소',data=LOGIN_INFO)
    # HTML 소스확인
    # print('login_req',login_req.text)
    # Header 확인
    # print('headers',login_req.headers)
    if login_req.status_code == 200 and login_req.ok: # 로그인 후 특정 글을 가져올떄
        post_one = s.get('글의 주소') # get방식
        post_one.raise_for_status() #예외일때의 방식
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soup.prettify())
        badges = soup.select("div.badges > ul > li > a >img")
        for i,z in enumerate(badges,1):
            fullFileName = os.path.join("c:/",str(i)+'.jpg')
            req.urlretrieve(z['src'],fullFileName)
