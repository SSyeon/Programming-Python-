from urllib.request import urlopen
from bs4 import BeautifulSoup



if __name__ == '__main__':
    with urlopen("https://movie.daum.net/boxoffice/yearly") as response:
        soup  =  BeautifulSoup(response, "lxml")

        # print(soup)
    # movie_titles = soup.find_all("a", attrs={"class":"link_g"})
    # print("<<<다음 영화 박스오피스>>>")
    # n =  1
    # for movie_title in movie_titles[2:] :
    #     print(n,"위",movie_title.text)
    #     n+=1

    #-------------------------------
    with urlopen("https://search.naver.com/search.naver?where=nexearch&query=%b9%da%bd%ba%bf%c0%c7%c7%bd%ba%bc%f8%c0%a7") as response:
        soup  =  BeautifulSoup(response, "lxml")
    print("네이버 영화 박스오피스")
    n=1
    movie_titles_naver = soup.find_all("strong", attrs={"class": "_text"})
    for movie_title in movie_titles_naver[:10]: #1~10위
        print(n,movie_title.text)
        n+=1