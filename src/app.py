# lib
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem

from modules.app_module import AppModule

# ui
import ui.url_download_window


def main():
    app_module = AppModule()
    app_module.generate_window(name='url_download_window', ui_class=ui.url_download_window.Ui_MainWindow, show=True)

    # --- #
    sys.exit(app_module.app.exec_())
