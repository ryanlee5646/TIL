import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument('--log-level=3')
#`driver = webdriver.Firefox(firefox_options=firefox_options,executable_path='C:/section3/webdriver/firefox/geckodriver')
driver = webdriver.Firefox(executable_path='C:/section3/webdriver/firefox/geckodriver')

#driver.set_window_size(1920, 1280)
driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("c:/Website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("c:/Website2.png")
driver.quit()
