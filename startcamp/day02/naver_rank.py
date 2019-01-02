#네이버 실시간 검색 크롤링
import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
#result = soup.select('div.PM_CL_realtimeKeyword_list_base span.ah_k')
result = soup.select('div.PM_CL_realtimeKeyword_list_base a.ah_a')
#result = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base')

for item in result:
    rank = item.select_one('.ah_r').text
    keyword = item.select_one('.ah_k').text
    print(f'{rank} / {keyword}')