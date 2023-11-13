import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'
}

r = requests.get('https://www.fullerton.cl/categoria-producto/gato/', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

data = soup.find('ul', {'class': 'products columns-3'})

print(data)