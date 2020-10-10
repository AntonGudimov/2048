# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\rules.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 446)
        MainWindow.setMinimumSize(QtCore.QSize(450, 455))
        MainWindow.setMaximumSize(QtCore.QSize(450, 455))
        MainWindow.setGeometry(QtCore.QRect(80, 110, 450, 455))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 431, 391))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 21))
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Правила игры</span></p><p><span style=\" font-size:10pt;\">1. В каждом раунде появляется плитка номинала «2» (с вероятностью 90,9090909 %) или «4» (с вероятностью 9,09090909 %)</span></p><p><span style=\" font-size:10pt;\">2. Нажатием стрелки игрок может скинуть все плитки игрового поля в одну из 4 сторон. Если при сбрасывании две плитки одного номинала «налетают» одна на другую, то они слипаются в одну, номинал которой равен сумме соединившихся плиток. После каждого хода на свободной секции поля появляется новая плитка номиналом «2» или «4». Если при нажатии кнопки местоположение плиток или их номинал не изменится, то ход не совершается.</span></p><p><span style=\" font-size:10pt;\">3. Если в одной строчке или в одном столбце находится более двух плиток одного номинала, то при сбрасывании они начинают слипаться с той стороны, в которую были направлены. Например, находящиеся в одной строке плитки (4, 4, 4) после хода влево они превратятся в (8, 4), а после хода вправо — в (4, 8). Данная обработка неоднозначности позволяет более точно формировать стратегию игры.</span></p><p><span style=\" font-size:10pt;\">4. За каждое соединение игровые очки увеличиваются на номинал получившейся плитки.</span></p><p><span style=\" font-size:10pt;\">5. Игра заканчивается поражением, если после очередного хода невозможно совершить действие.</span></p><p><br/></p><p><br/></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.actionClose.setText(_translate("MainWindow", "Закрыть"))

