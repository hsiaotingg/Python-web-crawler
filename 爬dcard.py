import random
from bs4 import BeautifulSoup as bs
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # 自動更新webdriver pip install webdriver-manager
import time
from fake_useragent import UserAgent

search = "王品"
ua = UserAgent()
options = Options()
options.add_argument("user-agent=" + ua.chrome)
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.dcard.tw/search?forum=food&query={}".format(search))

temp_height = 0
link_list = []
status = True
while status:
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(random.randint(5, 15))
    check_height = driver.execute_script("return document.documentelement.scrolltop || window.pageyoffset || document.body.scrolltop;")
    if check_height == temp_height:
        break
    temp_height = check_height
driver.quit()

soup = bs(driver.page_source, 'lxml')
url = soup.find_all('a', class_="sc-b205d8ae-3 iOQsOu")
link_list.append("https://www.dcard.tw" + url.get("href"))

dic = {}
dic["link"] = link_list
ls = []
ls.append(dic)
with open("link.json","r",encoding="utf-8") as file:
    json.dump(ls, file, ensure_ascii=False)



'''
driver.get('https://www.dcard.tw/f/food/p/238891380')
soup = bs(driver.page_source,'lxml')
title = soup.find('div',class_='sc-6976ab12-2 kYbXlA')
content = soup.find("div", class_="sc-8ec6ca7a-0 kdymLJ")
date = soup.find_all('div',class_='sc-6976ab12-4 gNkeps')[1]
'''