# @author : Bezmican Zehir | LinkedIn: bezmicanzehir | IG: @bayonuc
# This file converts .ui to .py
from PyQt5 import uic

with open('../src/ui/url_download_window.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('../ui/url_download_window.ui', fout)
