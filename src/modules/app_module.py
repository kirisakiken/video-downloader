import sys
from PyQt5 import QtWidgets


class AppModule:
    __app: QtWidgets.QApplication
    __windows: dict[str, QtWidgets.QMainWindow]

    def __init__(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__windows = {}

    def generate_window(self, name: str, ui_class, show: bool = False):
        if self.__windows.get(name):
            raise KeyError(f'Key: {name} already exists in windows collection')

        window = QtWidgets.QMainWindow()
        window_class = ui_class()
        window_class.setupUi(window)
        self.__windows[name] = window
        self.__windows[name].show()

    @property
    def app(self):
        return self.__app

    @property
    def windows(self) -> dict[str, QtWidgets.QMainWindow]:
        return self.__windows
