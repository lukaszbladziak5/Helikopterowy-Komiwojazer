import os
import sys
import UI
from PySide6 import QtGui
from PySide6.QtWidgets import *
from UI import zasoby
from UI.EkranPoczatkowy import *
from UI.WyborTrybu import *


class EkranPoczatkowy(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EkranPoczatkowy()
        self.ui.setupUi(self)
        self.ui.startPrzycisk.clicked.connect(self.rozpocznij)
        self.ui.koniecPrzycisk.clicked.connect(self.zakoncz)
        self.show()

    def rozpocznij(self):
            startPrzycisk = WyborTrybu()
            widget.addWidget(startPrzycisk)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def zakoncz(self):
            app.quit()


class WyborTrybu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_WyborTrybu()
        self.ui.setupUi(self)
        self.ui.powrotPrzycisk.clicked.connect(self.powrotDoEkranuPoczatkowego)
        self.ui.permutacjaPrzycisk.clicked.connect(self.wybranoPermutacje)
        self.ui.bnbPrzycisk.clicked.connect(self.wybranoBnB)
        self.ui.genetycznyPrzycisk.clicked.connect(self.wybranoGenetyczny)

    def wybranoPermutacje(self):
        os.system('python TSP_algorithms/metoda_permutacyjna.py')

    def wybranoBnB(self):
        os.system('python TSP_algorithms/metoda_podzialu_i_ograniczen.py')

    def wybranoGenetyczny(self):
        os.system('python TSP_algorithms/algorytm_genetyczny.py')

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