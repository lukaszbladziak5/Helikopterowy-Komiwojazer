from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

app = QApplication([])

win = uic.loadUi("UI\MenuGlowne.ui")
win.show()

app.exec()