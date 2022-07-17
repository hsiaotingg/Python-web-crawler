### 題目
請把下方網頁的所有英文句子(EX. You bet!)(只要文字)用 SELENIUM 抓下來,
且爬取的時候不顯示螢幕,並把爬下來的語料存成三種形式
1. txt
2. 直接串資料庫存入
3. pickle (課程中沒有此部分,請自我突破)<br>
[網站連結](https://gogakuru.com/english/phrase/genre/180_%E5%88%9D%E7%B4%9A%E3%83%AC%E3%83%99%E3%83%AB.html?layoutPhrase=1&orderPhrase=1&condMovie=0&flow=enSearchGenre&condGenre=180&perPage=50)

### code
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager #自動更新chrome版本
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random
import time
import pymysql
import pickle

# 爬蟲前置
ua = UserAgent()
opts = Options()
opts.add_argument('--headless')
opts.add_argument("user-agent=" + ua.chrome)
driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
soup = BeautifulSoup(driver.page_source,"lxml")

# 1.把爬下來的語料存成txt檔
count = 0
for i in range(1,199):
    driver.get(f"https://gogakuru.com/english/phrase/genre/180_%E5%88%9D%E7%B4%9A%E3%83%AC%E3%83%99%E3%83%AB.html?pageID={i}&layoutPhrase=1&orderPhrase=1&condMovie=0&perPage=50&flow=enSearchGenre&condGenre=180")
    driver.implicitly_wait(10)
    titles = soup.select("span.font-en")
    time.sleep(random.randint(2, 4))
    with open("title.txt", "a", encoding="utf-8") as file:
        for title in titles:
            file.write(title.text.strip()+"\n")
            count+=1
driver.close()

# 2. 直接串資料庫存入
conn = pymysql.connect(
    host ="127.0.0.1",
    port = 3306,
    user = "root",
    password = "",
    db = "exam3",
    charset = "utf8")

try:
    cursor = conn.cursor()

    sql = """INSERT INTO charts(title) VALUES (%s)""" #sql語法:新增資料

    for title in open("title.txt","r",encoding="utf-8").readlines():
        cursor.execute(sql,title)
    conn.commit()
    conn.close()
except Exception as ex:
    print("Exception",ex)



 # 3. pickle (課程中沒有此部分,請自我突破)
with open("title.txt","r",encoding="utf-8")as f:
   a = f.read()

with open("exam.pickle","wb") as f1:
    pickle.dump(a,f1)
```
