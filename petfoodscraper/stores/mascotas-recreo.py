import requests
import json
from bs4 import BeautifulSoup
import time

np = 0

def requestData(np):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'
    }
    r = requests.get('https://www.mascotasrecreo.cl/collection/alimento-gatos?limit=12&with_stock=0&smart_stock=0&order=price&way=ASC&page={}'.format(np), headers=headers)
    return r

def parseData(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    script = soup.find_all('script')[18].text.strip()[29:-2]
    data = json.loads(script)
    return data

def findData(d):
    if len(d['items']) == 0:
        return False
    for x in range(0, len(d['items'])):
        print(d['items'][x]['title'], d['items'][x]['finalPrice'])
    return True

def init(np):
    html = requestData(np)
    data = parseData(html)
    verf = findData(data)
    if verf == False:
        return
    time.sleep(120)
    np += 1
    init(np)
    
init(np)