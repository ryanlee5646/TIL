import sys
import io
import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 로그인 유저정보
LOGIN_INFO = {
    'user_id': 'ryanlee5646',
    'user_pw': 'rbwlsl91',
    'user-submit': rep.quote_plus('로그인'),
    'user-cookie':1
}

# Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('', data=LOGIN_INFO)
    # HTML 소스 확인
    # print('Login_req', Login_req.text)
    # Header 확인
    # print('headers', Login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        print(soup.prettify())
