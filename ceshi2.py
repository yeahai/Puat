# 2023/2/2 15:47
# 你好，夜嗨大帅比
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()

        self.resize(640,500)
        label = QLabel()

        pixmap = QPixmap("data_save/OIP.jpg")
        pix = pixmap.scaled(QSize(620,500),Qt.KeepAspectRatio)
        label.setPixmap(pix)
        label.setAlignment(Qt.AlignCenter)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=StackedExample()
    demo.show()
    sys.exit(app.exec_())