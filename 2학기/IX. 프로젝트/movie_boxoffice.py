from urllib.request import urlopen
from bs4 import BeautifulSoup



if __name__ == '__main__':
    with urlopen("https://movie.daum.net/boxoffice/weekly") as response:
        soup  =  BeautifulSoup(response, "lxml")

        print(soup)
