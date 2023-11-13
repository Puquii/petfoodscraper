import requests
import json
from bs4 import BeautifulSoup

counter = 0
stack = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'
}

link = 'https://www.befoods.cl/collections/alimento-gatos?page=1'

r = requests.get(link, headers=headers)
    
soup = BeautifulSoup(r.content, 'html.parser')

script = soup.find('script', {'type': 'text/javascript'}).string

for c in script[460: -3]:
    if c == '[':
        stack.append('[')
    if c == ']':
        stack.pop()
    counter += 1
    if bool(stack) == False:
        break

e = counter + 460

jtext = json.loads(script[460: e])

for x in range(0, len(jtext)):
    print(jtext[x]['title'], jtext[x]['price']/100)