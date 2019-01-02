import requests
import bs4

h = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get('https://www.melon.com/index.htm',headers=h).text
print(response)
# soup = bs4.BeautifulSoup(response, 'html.parser')
# result = soup.select('')

# for item in result:
#     rank = item.select_one('').text
#     keyword = item.select_one('').text
#     print(f'{rank} / {keyword}')