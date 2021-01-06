import sys
import io
from bs4 import BeautifulSoup
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 로그인 유저정보
LOGIN_INFO = {
    'user_id': 'outsider7224',
    'user_pw': '11111112!!!'
}

# Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    # HTML 소스확인
    # print('login_req',login_req.text)
    # Header 확인
    # print('headers',login_req.headers)
    if login_req.status_code == 200 and login_req.ok: # 로그인 후 특정 글을 가져올떄
        post_one = s.get('글의 주소') # get방식
        post_one.raise_for_status() #예외일때의 방식
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soup.prettify())
        aritcle = soup.select_one("table:nth-of-type(3)").find_all('p')
        # print(article)
        for i in article:
            if i.string is not None:
                #DB INSERT, 엑셀로 저장, 텍스트 가공
                print(i.string)
