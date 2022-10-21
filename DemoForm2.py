#DemoForm2.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 화면을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼 클래스 정의(QMainWindow로 변경)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 슬롯메서드 추가
    def firstClick(self):
        self.label.setText("첫번째 버튼~~")
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