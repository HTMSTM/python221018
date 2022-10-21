#DemoForm1.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 화면을 로딩
form_class = uic.loadUiType("DemoForm1.ui")[0]

#폼 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 PyQt 데모")

#진입점 체크(직접 실행한 경우 윈도위 생성)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow = show()
    app.exec_()