import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # Qt Designer에서 제작한 Ui를 불러오는 클래스

form_class = uic.loadUiType("ui/test.ui")[0]  # Qt Designer에서 만든 ui를 불러옴

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스 생성자 호출
        self.setupUi(self)  # 위에서 불러온 test.ui를 연결
        self.setWindowTitle("연습 프로그램")
        self.button1.clicked.connect(self.button1_click)
        # 버튼1이 클릭되면 button1_click 메서드 호출
        self.button2.clicked.connect(self.button2_click)
        # 버튼2이 클릭되면 button2_click 메서드 호출

    def button1_click(self):
        self.label1.setText("HelloWorld!!!")

    def button2_click(self):
        self.label1.setText("안녕하세요!!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())




