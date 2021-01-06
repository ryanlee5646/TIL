import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    # 초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") # CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="c:sections3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 && 출석 체크
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name("id").send_keys('네이버 ID')
        self.driver.find_element_by_name("pw").send_keys('비밀번호')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get('글을 작성하고자하는 url')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다!!.')
        self.driver.find_element_by_xpath('글 입력버튼 xpath')
        time.sleep(3)

    # 소멸자
    def __del__(self):
        # self.driver.close() # 현재 실행 포커스 된 영역을 종료
        self.driver.quit() #  selenium 전체 프로그램 종료
        print("Removed driver Object")

    # 실행
    if __name__ == '__main__':
        # 객체 생성
        a = NcafeWriteAtt()
        # 시작 시간
        start_time = time.time()
        # 프로그램 실행
        a.writeAttendCheck()
        # 종료 시간 출력
        print("---Total %s seconds ---" % (time.time() - start_time))
        # 객체 소멸
        del a
