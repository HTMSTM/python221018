#DemoForm2.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹서버와 통신
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup


# 화면을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼 클래스 정의(QMainWindow로 변경)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 슬롯메서드 추가
    def firstClick(self):
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


        self.label.setText("네이버 웹툰 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼~~")

#진입점 체크(직접 실행한 경우 윈도위 생성)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()