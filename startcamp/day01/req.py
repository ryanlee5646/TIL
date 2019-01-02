import requests
import bs4

response = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section').text
soup = bs4.BeautifulSoup(response, 'html.parser' )
result = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(result)
#ctrl + '(backtick)