from RulesWindowUI import Ui_MainWindow as RulesWindowUI
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow, RulesWindowUI):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
