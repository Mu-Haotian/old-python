import sys
from PySide2.QtCore import QSize
from PySide2.QGui import QIcon
from PySide2.QtWidgets import*
from ui_cards import Ui_cards


class MyCads(QMainWindow,Ui_cards):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
    
    def init_button(self):
        pbth_list = self.pbth_img.buttons()
        for bth in pbth_list:
            bth.setText("")
            bth.setIcon(QIcon("bg.png"))
            bth.setIconSize(QSize(150,150))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MyCads()
    sys.exit(app.exec_())