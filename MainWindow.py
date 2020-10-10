from MainWindowUI import Ui_MainWindow as MainWindowUI
from RulesWindow import MainWindow as RulesWindow
from SettingsWindow import MainWindow as SettingsWindow
from Game import *
from GameState import GameState
from GameMode import GameMode

from PyQt5.QtGui import *
from PyQt5.QtGui import QKeyEvent, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets


class MainWindow(QMainWindow, MainWindowUI, QtWidgets.QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__mode = GameMode.CLASSIC
        self.__signal_changed_mode = False
        self.rw = RulesWindow()
        self.sw = SettingsWindow()
        self.sw.pushButtonOk.clicked.connect(self.set_mode)
        self.__game = Game()
        self.__model = QStandardItemModel(self.__game.row_count, self.__game.col_count)
        self.startButton.clicked.connect(self.on_new_game)
        self.actionRules.triggered.connect(self.show_rules)
        self.actionChange.triggered.connect(self.show_settings)
        # self.gameFieldTableView.setFocusPolicy(Qt.NoFocus)
        self.gameFieldTableView.keyPressEvent = self.keyPressEvent
        self.__the_best_scores = {"CLASSIC": 0, "LARGE": 0}

    @property
    def mode(self):
        return self.__mode

    @property
    def signal_changed_mode(self):
        return self.__signal_changed_mode

    def game_resize(self) -> None:
        for row in range(self.__game.row_count):
            for col in range(self.__game.col_count):
                if self.__game.field[row][col].value != 0:
                    item = QStandardItem(str(self.__game.field[row][col].value))
                else:
                    item = QStandardItem('')
                item.setFlags(Qt.ItemIsEnabled)
                item.setTextAlignment(Qt.AlignCenter)
                self.__model.setItem(row, col, item)

        self.gameFieldTableView.setModel(self.__model)
        self.valueScore.setText(str(self.__game.score))
        self.valueTheBestScore.setText(str(self.__game.the_best_score))

        self.checking_states()

    def on_new_game(self):
        self.winOrLose.setVisible(False)
        self.gameFieldTableView.setEnabled(True)
        if self.__mode == GameMode.CLASSIC:
            self.__the_best_scores["CLASSIC"] = self.__game.the_best_score
        elif self.__mode == GameMode.LARGE:
            self.__the_best_scores["LARGE"] = self.__game.the_best_score

        if self.__signal_changed_mode:
            if self.__mode == GameMode.CLASSIC:
                self.__mode = GameMode.LARGE
                self.__signal_changed_mode = False
            elif self.__mode == GameMode.LARGE:
                self.__mode = GameMode.CLASSIC
                self.__signal_changed_mode = False

        if self.__mode == GameMode.CLASSIC:
            self.gameFieldTableView.horizontalHeader().setDefaultSectionSize(100)
            self.gameFieldTableView.verticalHeader().setDefaultSectionSize(100)
            self.gameFieldTableView.setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))
            self.__game.new_game(4, 4, 2048, self.__the_best_scores["CLASSIC"])
        elif self.__mode == GameMode.LARGE:
            self.gameFieldTableView.horizontalHeader().setDefaultSectionSize(50)
            self.gameFieldTableView.verticalHeader().setDefaultSectionSize(50)
            self.gameFieldTableView.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
            self.__game.new_game(8, 8, 16384, self.__the_best_scores["LARGE"])  # 16384)
        self.game_resize()

    def checking_states(self):
        if self.__game.state == GameState.FAIL:
            self.gameFieldTableView.setEnabled(False)
            self.winOrLose.setText("Проигрыш(")
            self.winOrLose.setVisible(True)
        if self.__game.state == GameState.WIN:
            self.gameFieldTableView.setEnabled(False)
            self.winOrLose.setText("Победа!")
            self.winOrLose.setVisible(True)
            self.continueButton.setVisible(True)
            self.continueButton.clicked.connect(self.keep_playing)

    def keyPressEvent(self, me: QKeyEvent = None) -> None:
        if self.__game.state == GameState.PLAYING:
            if me.key() == Qt.Key_W or me.key() == Qt.Key_Up:
                self.__game.moving(0, 0)
            elif me.key() == Qt.Key_S or me.key() == Qt.Key_Down:
                self.__game.moving(1, 0)
            elif me.key() == Qt.Key_A or me.key() == Qt.Key_Left:
                self.__game.moving(0, 1)
            elif me.key() == Qt.Key_D or me.key() == Qt.Key_Right:
                self.__game.moving(1, 1)
            self.game_resize()

    def keep_playing(self):
        self.winOrLose.setVisible(False)
        self.continueButton.setVisible(False)
        self.gameFieldTableView.setEnabled(True)
        self.__game.state = GameState.PLAYING

    def show_rules(self):
        self.rw.show()

    def show_settings(self):
        self.sw.show()

    def set_mode(self):
        self.__signal_changed_mode = True
        self.sw.close()
