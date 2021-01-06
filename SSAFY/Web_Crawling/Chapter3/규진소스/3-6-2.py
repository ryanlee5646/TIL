import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('C:/section3/chrome/chromedriver')

driver.set_window_size(1920, 1280)
driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("c:/Website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("c:/Website2.png")
driver.quit()
