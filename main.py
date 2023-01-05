import sys
import UI
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from UI import *
from UI.EkranPoczatkowy import *
from UI.WyborTrybu import *
from UI.OknoZadania import *
from UI import zasoby


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
        self.ui.permutacjaPrzycisk.clicked.connect(self.wybranoTryb1)
        self.ui.bnbPrzycisk.clicked.connect(self.wybranoTryb2)
        self.ui.genetycznyPrzycisk.clicked.connect(self.wybranoTryb3)

    def wybranoTryb1(self):
        global nazwaTrybu
        nazwaTrybu = 1
        przyciskTrybu = OknoZadania()
        widget.addWidget(przyciskTrybu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def wybranoTryb2(self):
        global nazwaTrybu
        nazwaTrybu = 2
        przyciskTrybu = OknoZadania()
        widget.addWidget(przyciskTrybu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def wybranoTryb3(self):
        global nazwaTrybu
        nazwaTrybu = 3
        przyciskTrybu = OknoZadania()
        widget.addWidget(przyciskTrybu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def powrotDoEkranuPoczatkowego(self):
        cofaniePrzycisk = EkranPoczatkowy()
        widget.addWidget(cofaniePrzycisk)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class OknoZadania(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_OknoZadania()
        self.ui.setupUi(self)
        self.ui.powrotPrzycisk.clicked.connect(self.powrotDoEkranuPoczatkowego)
        self.ui.startPrzycisk.clicked.connect(self.playAnim)
        self.setMouseTracking(True)
        self.points = QPointFList()
        self.path = None
        self.timeline = QTimeLine(3000, self)
        self.timeline.setEasingCurve(QEasingCurve.Linear)
        self.timeline.valueChanged.connect(self.timelineChanged)
        self.dashOffset = 0
        self.dashLength = 0

        global nazwaTrybu
        if nazwaTrybu == 1:
            self.ui.tytulWybor.setText('Rozwiązanie permutacyjne')
            self.ui.tekstWynik.hide()
            self.ui.tekstWynik_2.hide()
            self.ui.tekstWynik_3.hide()
            self.ui.tekstWynik_4.hide()
            self.ui.liczbaPunktow_2.hide()
            self.ui.liczbaMinut.hide()
            self.ui.liczbaSekund.hide()
        elif nazwaTrybu == 2:
            self.ui.tytulWybor.setText('Metoda podziału i ograniczeń')
            self.ui.uwagaTekst.hide()
            self.ui.tekstWynik.hide()
            self.ui.tekstWynik_2.hide()
            self.ui.tekstWynik_3.hide()
            self.ui.tekstWynik_4.hide()
            self.ui.liczbaPunktow_2.hide()
            self.ui.liczbaMinut.hide()
            self.ui.liczbaSekund.hide()
        elif nazwaTrybu == 3:
            self.ui.tytulWybor.setText('Algorytm genetyczny')
            self.ui.uwagaTekst.hide()
            self.ui.tekstWynik.hide()
            self.ui.tekstWynik_2.hide()
            self.ui.tekstWynik_3.hide()
            self.ui.tekstWynik_4.hide()
            self.ui.liczbaPunktow_2.hide()
            self.ui.liczbaMinut.hide()
            self.ui.liczbaSekund.hide()
        else:
            print("Bląd")

    def timelineChanged(self, val):
        self.dashOffset = val * self.dashLength
        self.update()

    def playAnim(self):
        print('hello')
        self.path.closeSubpath()
        self.timeline.setDirection(QTimeLine.Forward)
        self.timeline.start()

    def paintEvent(self, event):
        qp = QPainter(self)
        # qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        pen = QPen(Qt.black, 5, c=Qt.RoundCap)
        qp.setPen(pen)

        qp.save()
        # qp.end()
        if self.path:
            p = self.path
            self.dashLength = p.length()/pen.width()
            pen.setDashPattern([self.dashLength, self.dashLength])
            pen.setDashOffset(self.dashLength - self.dashOffset)

            qp.setPen(pen)
            qp.drawPath(p)

        qp.restore()
        qp.drawPoints(self.points)

    def mousePressEvent(self, event):
        mp = event.position()
        self.points.append(mp)
        if len(self.points) > 1:
            self.path.lineTo(mp)
        else:
            self.path = QPainterPath(mp)
        self.ui.liczbaPunktow.display(len(self.points))
        self.update()

    def sizeHint(self):
        return QSize(600, 600)

    def mouseMoveEvent(self, event):
        mp = event.position()
        p = self.mapToGlobal(mp.toPoint())
        p.setY(p.y() - 60)
        p.setX(p.x() + 10)
        QToolTip.showText(p, f"x:{int(mp.x())}\ny:{int(mp.y())}")

    def powrotDoEkranuPoczatkowego(self):
        cofaniePrzycisk = EkranPoczatkowy()
        widget.addWidget(cofaniePrzycisk)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == "__main__":
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
