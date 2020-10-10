from SettingsWindowUI import Ui_MainWindow as SettingsWindowUI
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow, SettingsWindowUI):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.radioButtonClassicMode.clicked.connect(self.set_radio_button_classic_mode)
        self.radioButtonBigMode.clicked.connect(self.set_radio_button_large_mode)

    def set_radio_button_classic_mode(self):
        self.radioButtonClassicMode.setChecked(True)

    def set_radio_button_large_mode(self):
        self.radioButtonBigMode.setChecked(True)
