# lib
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem

from modules.app_module import AppModule
from src.binders.element_binder_base import ElementBinderBase
from src.binders.url_download_binder import UrlDownloadWindowBinder

# ui
import ui.url_download_window


def main():
    app_module = AppModule()
    binders: list[ElementBinderBase] = []

    # url download window
    ui_class = ui.url_download_window.Ui_MainWindow()
    app_module.generate_window(name='url_download_window', ui_class=ui_class, show=True)
    binders.append(UrlDownloadWindowBinder(ui_class=ui_class))

    # bind
    for e in binders:
        e.bind_elements()

    # --- #
    sys.exit(app_module.app.exec_())
