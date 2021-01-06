import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:/section3/chrome/chromedriver') #Chrome 대문자

driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("c:/website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("c:/website2.png")

driver.quit()

print("스크린샷 완료")
