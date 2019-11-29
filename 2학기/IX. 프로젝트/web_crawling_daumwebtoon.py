from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# 크롬확장프로그램 > json viewer

if __name__ == '__main__':
    # 다음 웹툰 > 어쩌다 발견한 7월
    data = urlopen('http://webtoon.daum.net/data/pc/webtoon/view/findjuly')
    webtoon_json = json.loads(data.read())
    # print(webtoon_json)
    # print(webtoon_json['data']['webtoon']['webtoonEpisodes'])
    html = '<html><head><meta charset=\'utf-8\' /></head><body>'
    webtoonEpisodes = webtoon_json['data']['webtoon']['webtoonEpisodes']
    for episode in webtoonEpisodes:
        episode_id = episode['id']
        link = "http://webtoon.daum.net/webtoon/viewer/" + str(episode_id)
        image = episode['thumbnailImage']['url']
        title = episode['title']
        html += "<a href='{}'><img src='{}' />{}</a><br />".format(link, image, title)
    html += '</body></html>'

    # 예쁘게 html로 저장하자
    outputSoup = BeautifulSoup(html, 'lxml')
    prettyHtml = str(outputSoup.prettify())
    with open("연애혁명.html", "w", encoding="utf-8") as f:
        f.write(prettyHtml)
