#web1.py
# 웹 크롤링을 위한 선언

from bs4 import BeautifulSoup

#페이지 로딩: 연속적으로 함수(메서드) 호출. 메서드 체인
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체 생성

soup = BeautifulSoup(page, "html.parser")

#print(soup.prettify())

#모든 <p> 검색
#print( soup.find_all("p"))

#print( soup.find("p"))

#<p class='outer-text'>컨텐츠</p>
#print( soup.find_all("p", class_="outer-text"))

# 반복문으로 컨텐츠만 출력
for tag in soup.find_all("p"):
    #태그 내부의 문자열만 출력 : .text
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

