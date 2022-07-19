### 題目
[網頁連結](https://technews.tw/)<br>
爬取首頁如圖1紅色框框處資料，並將資料整理成如圖2格式<br>
圖1(2022/7/19)
![image](https://github.com/hsiaotingg/Python-web-crawler/blob/main/pic/technews-1.png)
圖2(圖例，日期非7/19)
![image](https://github.com/hsiaotingg/Python-web-crawler/blob/main/pic/technews-2.png)

### code
```
import json
import requests
from bs4 import BeautifulSoup

res = requests.get("https://technews.tw/")
soup = BeautifulSoup(res.text,"lxml")
ls1 = soup.find_all("li",class_ = "block2014")
ls2 = []

#整理分類、標題、連結成一個list
for i in ls1:
    d = {}
    d["category"] = i.find("div","cat01").text
    d["sum_title"] = i.find("div","sum_title").h3.text
    d["sum_title_url"] = i.find("div","img").a["href"]

    #將spotlist整理成一個list
    ls = []
    for x in i.find_all("li","spotlist"):
        d1 = {}
        d1["title"] = x.a.text
        d1["url"] = x.a["href"]
        ls.append(d1)
    d["spotlist"] = ls
    ls2.append(d)

#將整理好的資料寫入json檔
with open("output.json","w",encoding = "utf-8") as file:
    file.write(json.dumps(ls2,ensure_ascii=False))
```
