import random
import re
from bs4 import BeautifulSoup as bs
import requests as req
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # 自動更新webdriver pip install webdriver-manager
import time
from fake_useragent import UserAgent


# search 找尋的餐廳品牌 year 從現在到year資料全爬
def getDcardInfo(search, year):
    options = Options()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://www.dcard.tw/search?forum=food&query={}".format(search))

    dataList = []
    status = True
    while status:

        # 循环将滚动条下拉
        driver.execute_script("window.scrollBy(0,1000)")
        # sleep一下让滚动条反应一下
        html = driver.page_source
        soup = bs(html, "lxml")
        time.sleep(random.randint(2, 4))

        # 一個block
        data = soup.find_all("article", class_="sc-fc3be524-0 gFlPCQ")

        for item in data:
            dic = {}
            link = "https://www.dcard.tw" + item.find("a", class_="sc-fc3be524-3 fpKIeR").get("href")
            date = item.find_all("div", class_="sc-1b1fbd22-3 gqlsdQ")[-1].text
            # 組合成一個title
            title = "".join([t.text for t in item.find("a", class_="sc-fc3be524-3 fpKIeR")])

            dic["title"] = title
            dic["date"] = date
            dic["link"] = link
            dataList.append(dic)

            # 日期達到才停止
            result = re.findall("\d{4}", date)
            if result !=[] and int(result[0]) <= int(year):
                status = False
                break
    driver.quit()
                # try:
                #
                # except:
                #     pass
                # if int(year) >= int([0]):
                #     status = False
                #     break

    # 最後一筆為前年
    return dataList[:-1]


def clearData(dataList):
    # 找出重複的
    ClearData = []
    titlelist = []
    for i, item in enumerate(dataList):
        title = item["title"]
        if title not in titlelist:
            ClearData.append(item)
            titlelist.append(title)

    with open("dcard(時時香).json", "w", encoding="utf-8") as f:
        json.dump(ClearData, f, ensure_ascii=False, indent=1)


datalist = getDcardInfo("時時香", '2020')  #輸入想要找尋的品牌及"年度"以前的文章
clearData(datalist)

textlist=[]
# def linkClick(dic):
with open("dcard(時時香).json", "r", encoding="utf-8") as file:
    datas = json.load(file)

link_list = []
for l in datas:
    link_list.append(l["link"])
# print(len(link_list))


ua = UserAgent()
content_list = []
# a = 45
# while a < 53 : #0~53
#     a+=1
for link in link_list:

    res = req.get(link)
    soup = bs(res.text, "lxml")
    time.sleep(random.uniform(2, 6))
    title = soup.find("h1",class_="sc-ae7e8d73-0 wYxxj").text

    time.sleep(random.randint(40 ,60))
    try:
        content = soup.find_all("div", class_="sc-ebb1bedf-0 aiaXw")[0].find_all("span")
        for i in content:
            textlist.append(i.text.strip().replace("\n",''))
    except:
        pass

    dic = {}
    dic["title"] = title
    dic["content"] = "".join(textlist)
    content_list.append(dic)
    textlist = []

with open("dcard-content(時時香).json", "w", encoding="utf-8") as f:
    f.write(json.dumps(content_list, ensure_ascii=False, indent=1)[1:-1])