import requests
from bs4 import BeautifulSoup
import pandas as pd
Names=[]
Prices=[]
Desc=[]
Ratings=[]

for i in range(1,10):
    url=("https://www.flipkart.com/search?q=mobiles%20under%20100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i))
    r= requests.get(url)
    print(r)
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    names=box.find_all("div",class_="_4rR01T")

    for i in names:
        n=i.text
        Names.append(n)
    print(Names)

    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in prices:
        p=i.text
        Prices.append(p)
    print(Prices)

    desc=box.find_all("ul",class_="_1xgFaf")
    for i in desc:
        d=i.text
        Desc.append(d)
    print(Desc)

    rev=box.find_all("div",class_="_3LWZlK")
    for i in rev:
        r=i.text
        Ratings.append(r)
    print(Ratings)

    df=pd.DataFrame({"Product name":Names, "Prices": Prices,"Description":Desc, "User Ratings":Ratings})
    print(df)
    df.to_csv("mobile_flipkart.csv")






