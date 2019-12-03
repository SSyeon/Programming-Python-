from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

if __name__ == '__main__':
    # response = urlopen("https://www.youtube.com/feed/trending?gl=KR")
    # soup  = BeautifulSoup(response,"lxml")
    url = "https://www.youtube.com/user/feellikefeel/videos "
    response = requests.get(url)
    soup = BeautifulSoup (response.text,"lxml")
    # print(soup)
    youtube_titles   = soup.find_all("a", attrs = {"class":"yt-uix-tile-link"})
    for youtube_titles in youtube_titles:
        print(youtube_titles.text)
        print("https://www.youtube.com/"+youtube_titles["href"])
