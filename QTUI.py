# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 267, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateTimeEdit_Update_StartTime = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_Update_StartTime.setDate(QtCore.QDate(2019, 1, 1))
        self.dateTimeEdit_Update_StartTime.setObjectName("dateTimeEdit_Update_StartTime")
        self.horizontalLayout.addWidget(self.dateTimeEdit_Update_StartTime)
        self.dateTimeEdit_Update_EndTime = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_Update_EndTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_Update_EndTime.setDate(QtCore.QDate(2020, 1, 1))
        self.dateTimeEdit_Update_EndTime.setObjectName("dateTimeEdit_Update_EndTime")
        self.horizontalLayout.addWidget(self.dateTimeEdit_Update_EndTime)
        self.pushButton__UpdateDateBase = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton__UpdateDateBase.setObjectName("pushButton__UpdateDateBase")
        self.horizontalLayout.addWidget(self.pushButton__UpdateDateBase)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView_stockbasic = QtWidgets.QTableView(self.layoutWidget)
        self.tableView_stockbasic.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableView_stockbasic.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableView_stockbasic.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableView_stockbasic.setObjectName("tableView_stockbasic")
        self.verticalLayout.addWidget(self.tableView_stockbasic)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu__command = QtWidgets.QMenu(self.menubar)
        self.menu__command.setObjectName("menu__command")
        self.menu_aboat = QtWidgets.QMenu(self.menubar)
        self.menu_aboat.setObjectName("menu_aboat")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpdateDataBase = QtWidgets.QAction(MainWindow)
        self.actionUpdateDataBase.setCheckable(False)
        self.actionUpdateDataBase.setObjectName("actionUpdateDataBase")
        self.menu__command.addAction(self.actionUpdateDataBase)
        self.menubar.addAction(self.menu__command.menuAction())
        self.menubar.addAction(self.menu_aboat.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton__UpdateDateBase.clicked.connect(MainWindow.slot_UpdateDataBase)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dateTimeEdit_Update_StartTime.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.dateTimeEdit_Update_EndTime.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.pushButton__UpdateDateBase.setText(_translate("MainWindow", "更新数据库"))
        self.menu__command.setTitle(_translate("MainWindow", "命令"))
        self.menu_aboat.setTitle(_translate("MainWindow", "关于"))
        self.actionUpdateDataBase.setText(_translate("MainWindow", "UpdateDataBase"))
