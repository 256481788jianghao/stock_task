'''
Created on 2019年12月30日

@author: Administrator
'''

from PyQt5 import QtWidgets, QtGui
from QTUI import Ui_MainWindow
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow();
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
