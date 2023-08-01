from PySide2.QtWidgets import QApplication , QMainWindow ,QPushButton,QPlainTextEdit,QMessageBox

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500,400)
        self.window.move(300,400)
        self.window.setWindowTitle("搜索")

        self.textEdit = QPlainTextEdit(self.window)



app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()