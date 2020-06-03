import sys
from PySide2 import QtCore, QtGui, QtWidgets

class Worker(QtCore.QObject):
    def init(self):
        print("worker is ready.")

    def work(self):
        derp = self.sender()
        print (derp.text())
        derp.setText("It works!")

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Kick!")
button.show()

worker = Worker()
button.clicked.connect(worker.work)

app.exec_()
sys.exit()