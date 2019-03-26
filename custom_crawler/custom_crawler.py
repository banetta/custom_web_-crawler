import requests
from bs4 import BeautifulSoup

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

##  HTML GET Request
req = requests.get('http://bbs.ruliweb.com/')

##  HTML to Text
html = req.text

soup = BeautifulSoup(html, 'html.parser')
header = req.headers
status = req.status_code
is_ok = req.ok

if is_ok:
    print("Sucess")
else:
    print("Failure")

titles = soup.select(
    'a'
)

data = {}

for title in titles:
    if  title.get('href') not in ('None', 'javascript', 'null'):
        data[title.text] = title.get('href')

    with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
        json.dump(data, json_file)


