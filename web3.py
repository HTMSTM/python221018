#web3.py
#웹서버와 통신
import urllib.request

#웹크롤링
from bs4 import BeautifulSoup

#파일로 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")

#페이징 처리
for i in range(1,6):
    url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i)
    print( url )
    data = urllib.request.urlopen( url )

    #검색ㅇ이 용이한 객체
    soup = BeautifulSoup(data, "html.parser")

    #필터링 : < td class="title">

    cartoons = soup.find_all("td", class_="title")
    print("갯수:{0}".format( len(cartoons) ))
    title = cartoons[0].find("a").text
    link = cartoons[0].find("a")["href"]

    #print(title)
    #print(link)

    #<td class = "title">
    #   <a href="/webtoon/detail?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
    # </td>
    for item in cartoons:
        title = item.find("a").text
        print(title)
        f.write(title + "\n")

f.close()