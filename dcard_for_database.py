import json
from datetime import datetime  #strftime、strptime需用這一條才叫的到，直接import叫不到
import datetime as dt #1. datetime.datetime要用這條才叫的到。 2.因為上面那條，所以需再另外取名，python才不會搞混。

brand = input("請輸入品牌名稱:")
with open("dcard({}).json".format(brand),"r",encoding="utf-8") as f1:
    data1 = json.load(f1)
with open("dcard-content({}).json".format(brand),"r",encoding="utf-8") as f2:
    data2 = json.load(f2)

for i in data1:
    try:
        #Dcard 的文章如果是近幾天發文，不會顯示日期，會顯示" n天前"
        if "天前" in i["date"]:
            delta_date = dt.datetime.now() + dt.timedelta(days=-int(i["date"][0]))
            i["date"] = delta_date.strftime("%Y-%m-%d")

        #Dcard 的文章如果是當年度發文，不會顯示年份，只會顯示" n 月 n 日"
        elif "年" not in i["date"]:
            i["date"] = "2022年" + i["date"]

        i["date"] = i["date"].replace("年","-")
        i["date"] = i["date"].replace("月","-")
        i["date"] = i["date"].replace("日","")
        i['date'] = datetime.strptime(i['date'].replace(" ",""), "%Y-%m-%d").isoformat()
    except:
        pass


ls = []
for a,b in zip(data1,data2):
    dic={}
    dic["time"] = a["date"].replace(" ","")
    dic["content"] = b["content"]
    ls.append(dic)
with open("{}_dcard.json".format(brand),"w",encoding="utf-8") as file:
    file.write(json.dumps(ls,ensure_ascii=False, indent=1))


