# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 199)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelSettings = QtWidgets.QLabel(self.centralwidget)
        self.labelSettings.setGeometry(QtCore.QRect(10, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelSettings.setFont(font)
        self.labelSettings.setObjectName("labelSettings")
        self.radioButtonClassicMode = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonClassicMode.setGeometry(QtCore.QRect(50, 80, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButtonClassicMode.setFont(font)
        self.radioButtonClassicMode.setObjectName("radioButtonClassicMode")
        self.radioButtonBigMode = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBigMode.setGeometry(QtCore.QRect(50, 100, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButtonBigMode.setFont(font)
        self.radioButtonBigMode.setObjectName("radioButtonBigMode")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonOk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOk.setGeometry(QtCore.QRect(210, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButtonOk.setFont(font)
        self.pushButtonOk.setObjectName("pushButtonOk")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.radioButtonClassicMode.setChecked(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSettings.setText(_translate("MainWindow", "Настройки"))
        self.radioButtonClassicMode.setText(_translate("MainWindow", "Классический"))
        self.radioButtonBigMode.setText(_translate("MainWindow", "Большой"))
        self.label.setText(_translate("MainWindow", "Версия игры 2048:"))
        self.pushButtonOk.setText(_translate("MainWindow", "ОК"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.actionClose.setText(_translate("MainWindow", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

