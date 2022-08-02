### 爬蟲一條龍專題-餐飲趨勢分析
爬取方向：Dcard美食版，搜尋王品、陶板屋、西堤、夏慕尼、石二鍋、瓦城、非常泰、時時香、1010湘，爬取搜尋結果的標題、發文日期、發文內文並整理成json檔以利入M資料庫

### Code
```
import pandas as pd
from bs4 import BeautifulSoup as bs
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
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.dcard.tw/search?forum=food&query={}".format(search))

SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

datalist = []
while True:  #無限滾動
    #滾到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    soup = bs(driver.page_source, 'lxml')
    url = soup.find_all('a', class_="sc-8fe4d6a1-3 kfHo")
    link_list = ["https://www.dcard.tw" + i.get("href") for i in url]

    #休息
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    [datalist.append(link) for link in link_list]  #將搜尋結果的文章結果整理

link = list(set(datalist)) #排除重複的資料
df = pd.DataFrame(link,columns=['link'])
df.to_csv("link_{}.csv".format(search))
for x in df['link']:
    pass
```
*未完
