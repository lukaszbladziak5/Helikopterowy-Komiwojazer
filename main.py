from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget

from UI import zasoby

app = QApplication([])

win = uic.loadUi("UI\MenuGlowne.ui")
# win = uic.loadUi("UI\WyborTrybu.ui")
win.show()



app.exec()

