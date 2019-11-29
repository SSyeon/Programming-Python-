# 유튜브 워크맨 이번달
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':
    with urlopen("http://www.oliveyoung.co.kr/store/main/getBestList.do") as response:
        soup  =  BeautifulSoup(response, "lxml")

        # print(soup)
        n = 1
    # <p class="tx_name">피지오겔 DMT 바디로션 400ml</p>
    olive_products = soup.find_all("p", attrs={"class":"tx_name"})
    for best_product in olive_products:
        print(n,best_product.text)
        n+=1

