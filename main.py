from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget
from UI import zasoby
import sys

class EkranPoczatkowy(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("UI/EkranPoczatkowy.ui", self)
        self.startPrzycisk.clicked.connect(self.rozpocznij)
        self.koniecPrzycisk.clicked.connect(self.zakoncz)

    def rozpocznij(self):
        startPrzycisk = WyborTrybu()
        widget.addWidget(startPrzycisk)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def zakoncz(self):
        app.quit()

class WyborTrybu(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("UI/WyborTrybu.ui", self)
        self.powrotPrzycisk.clicked.connect(self.powrotDoEkranuPoczatkowego)
        self.permutacjaPrzycisk.clicked.connect(self.wybranoTryb)
        self.bnbPrzycisk.clicked.connect(self.wybranoTryb)
        self.genetycznyPrzycisk.clicked.connect(self.wybranoTryb)

    def wybranoTryb(self):
        przyciskTrybu = OknoZadania()
        widget.addWidget(przyciskTrybu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def powrotDoEkranuPoczatkowego(self):
        cofaniePrzycisk = EkranPoczatkowy()
        widget.addWidget(cofaniePrzycisk)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class OknoZadania(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("UI/OknoZadania.ui", self)
        self.powrotPrzycisk.clicked.connect(self.powrotDoEkranuPoczatkowego)

    def powrotDoEkranuPoczatkowego(self):
        cofaniePrzycisk = EkranPoczatkowy()
        widget.addWidget(cofaniePrzycisk)
        widget.setCurrentIndex(widget.currentIndex() + 1)

app = QApplication(sys.argv)
widget = QStackedWidget()
welcome = EkranPoczatkowy()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.setWindowTitle('Helikopterowy Komiwojażer')
widget.setWindowIcon(QtGui.QIcon('UI/images/helicopter-ga81252117_640.png'))
widget.show()
sys.exit(app.exec())