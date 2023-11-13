import requests
from bs4 import BeautifulSoup
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'
}

r = requests.get('https://www.jpets.cl/collection/alimentos-para-gatos', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

data = json.loads(soup.find_all('script')[15].text)

print(data['itemListElement'][0]['item']['offers']['price'])