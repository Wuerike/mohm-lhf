import sys
from PySide2.QtWidgets import *

class MyLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MyLineEdit, self).__init__(parent)

    def focusInEvent(self, e):
        sender = self.sender()
        print (sender)
        print("evento")
        self.selectAll()      

app = QApplication(sys.argv)
top = QWidget()
layout = QVBoxLayout()
layout.addWidget(MyLineEdit())
layout.addWidget(MyLineEdit())
top.setLayout(layout)
top.show()
app.exec_()


"""
colocando no gui core funciona

class MyPlainText(QPlainTextEdit):
    def __init__(self, parent=None):
        super(MyPlainText, self).__init__(parent)

    def focusInEvent(self, e):
        print("evento")
        self.selectAll() 
"""