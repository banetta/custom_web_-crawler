from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('/Users/banetta/Documents/git/custom_web_crawler/chromedriver')
driver.implicitly_wait(3)

start_time = time.time()

driver.get('http://ruliweb.com')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
lists = soup.select('a')

for n in lists:
    print(list.get('href'))

print("start_time", start_time)  # 출력해보면, 시간형식이 사람이 읽기 힘든 일련번호형식입니다.
print("--- %s seconds ---" % (time.time() - start_time))
print("Complete")

