### 題目
開啟 practice-technews-1 整理好的檔案，使用檔案裡面提供的連結，去爬報導內的正文內容文字，一個 url 則產生一個 txt 檔，內容為 url 的正文文字<br>

### code
```
import json
import requests
from bs4 import BeautifulSoup
with open("output.json","r",encoding="utf-8") as file:
    f = json.load(file)

for i in f:
    sum_file=("sum_"+i["category"] + "_" + i["sum_title"][:4])
    res = requests.get(i["sum_title_url"])
    soup = BeautifulSoup(res.text,"lxml")
    ls1 = soup.select("div.indent > p")
    f = open(sum_file + ".txt","w",encoding="utf-8")

    for x in ls1:
        f.write(x.text.strip())
    f.close()

    for x in i["spotlist"]:
        spotlist_file = ("spot_" + i["category"] + "_" +x["title"][:4])
        res = requests.get(x["url"])
        soup =BeautifulSoup(res.text,"lxml")
        ls = soup.select("div.indent > p")
        f = open(spotlist_file + ".txt","w",encoding="utf-8")
        for y in ls:
            f.write(y.text.strip())
        f.close()
   ``` 
