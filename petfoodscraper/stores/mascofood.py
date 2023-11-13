import requests
import json
from bs4 import BeautifulSoup
import time

np = 1

def requestData(np):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'
    }
    r = requests.get('https://mascofood.cl/collections/gato?page={}'.format(np), headers=headers)
    return r

def parseData(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    script = soup.find_all('script')[23].text.strip()[182: -79]
    data = json.loads(script)
    return data

def findData(data):
    if len(data['products']) == 0:
        return False
    for x in range(0, len(data['products'])):
        print(data['products'][x]['variants'][0]['name'] ,int(data['products'][x]['variants'][0]['price'] / 100))
    return True

def init(np):
    html = requestData(np)
    data = parseData(html)
    verf = findData(data)
    if verf == False:
        return
    time.sleep(20)
    np += 1
    init(np)

init(np)