import requests
from bs4 import BeautifulSoup

r = requests.get("https://codingeverybody.github.io/scraping_sample/1.html")

print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print('Title: '+soup.title.string)

articles = soup.findAll('div', {'class' : 'em'})

print(articles)
print(articles[0])
print(articles[0].text)


#=========================================================================#

r = requests.get("https://codingeverybody.github.io/scraping_sample/2.html")

print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print('Title: '+soup.title.string)

articles = soup.findAll('div', {'class' : 'strong'})

print(articles)
print(articles[0])
print(articles[0].text)