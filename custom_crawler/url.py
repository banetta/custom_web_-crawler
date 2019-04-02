import json
import os
import time

import requests
from bs4 import BeautifulSoup
# from selenium import webdriver



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

start_time = time.time()

titles = soup.select(
    'a'
)

data = {}

print("select complete")


for title in titles:
    if title.get('href'):
        data[title.text] = title.get('href')
    with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
        json.dump(data, json_file)

print("start_time", start_time) #출력해보면, 시간형식이 사람이 읽기 힘든 일련번호형식입니다.
print("--- %s seconds ---" %(time.time() - start_time))
print("Complete")


