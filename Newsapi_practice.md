## 題目
使用 python(請使用: from newsapi import NewsApiClient 的語法取資料,不要用 requests.get),<br>
控制 newsapi 裡面的選項取得報導,且報導須滿足以下要求:<br>
1. 標題或報導內容一定要有 武漢肺炎 四個字,且一定不能出現 外遇 兩個字<br>
2. 爬出來的新聞只能來自 ETtoday , 風傳媒, 中國時報, 聯合新聞網<br>
3. 由新到就排序<br>
4. 一頁呈現 100 篇報導<br>

## code
```
from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key="88eb1f6d5f21400dbe14838f9a6c3423")
all_articles = newsapi.get_everything(q = '武漢肺炎 -外遇',domains = 'ettodaay.net,storm.mg,chinatimes.com,udn.com', from_param = '2022-04-21', to = '2021-04-12', sort_by = 'publishedAt', page_size = 100)
with open("exam.json","w",encoding = "utf-8") as file:
    exam = (file.write(json.dumps(i, ensure_ascii=False)) for i in all_articles["articles"])
``` 
