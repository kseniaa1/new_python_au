import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QAction

_scriptdir = os.path.dirname(os.path.realpath(__file__))

class MainDialog(*uic.loadUiType(os.path.join(_scriptdir, 'ui', 'uii.ui'))):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.cats.clicked.connect(self.btnClicked1)
        self.dogs.clicked.connect(self.btnClicked2)


    def btnClicked1(self):
        self.cats.hide()
        self.dogs.hide()
        self.label.setText("=^-^=")


    def btnClicked2(self):
        self.cats.hide()
        self.dogs.hide()
        self.label.setText("U• ω •U")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainDialog()
    w.show()

    sys.exit(app.exec_())
