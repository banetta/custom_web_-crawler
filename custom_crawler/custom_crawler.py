import requests
from bs4 import BeautifulSoup

import json
import os

##  HTML GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

##  HTML Soruce Get
html = req.text

soup = BeautifulSoup(html, 'html.parser')
header = req.headers
status = req.status_code
is_ok = req.ok

my_titles = soup.select(
    'h3 > a'
)

if is_ok:
    print("Sucess")
else:
    print("Failure")

for title in my_titles:
    ## Tag안의 텍스트
    print(title.text)
    ## Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))