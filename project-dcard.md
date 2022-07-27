### 爬蟲一條龍專題-餐飲趨勢分析
爬取方向：Dcard美食版，搜尋王品、陶板屋、西堤、夏慕尼、石二鍋、瓦城、非常泰、時時香、1010湘，爬取搜尋結果的標題、發文日期、發文內文並整理成json檔以利入M資料庫

### Code
```
import random
from bs4 import BeautifulSoup
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
# options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.dcard.tw/search?forum=food&query={}".format(search))

# 無限滾動
temp_height = 0
link_list = []
while True:
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(random.randint(5, 15))
    check_height = driver.execute_script("return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
    if check_height == temp_height:
        break
    temp_height = check_height
driver.quit()

soup = Beautifulsoup(driver.page_source, 'lxml')
url = soup.find_all('a', class_="sc-b205d8ae-3 iOQsOu")
link_list.append("https://www.dcard.tw" + url.get("href"))

dic = {}
dic["link"] = link_list
ls = []
ls.append(dic)
with open("link.json","r",encoding="utf-8") as file:
    json.dump(ls, file, ensure_ascii=False)
```
*未完
