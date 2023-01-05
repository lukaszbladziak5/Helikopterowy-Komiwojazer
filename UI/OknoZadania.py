# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OknoZadania.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QLCDNumber,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_OknoZadania(object):
    def setupUi(self, OknoZadania):
        if not OknoZadania.objectName():
            OknoZadania.setObjectName(u"OknoZadania")
        OknoZadania.resize(1200, 800)
        OknoZadania.setAutoFillBackground(True)
        OknoZadania.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 214, 100);\n"
"	border: 2px solid rgb(115, 90, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(180, 214, 5);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(180, 214, 255);\n"
"}")
        OknoZadania.setInputMethodHints(Qt.ImhPreferUppercase)
        self.centralwidget = QWidget(OknoZadania)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.powrotPrzycisk = QCommandLinkButton(self.centralwidget)
        self.powrotPrzycisk.setObjectName(u"powrotPrzycisk")
        self.powrotPrzycisk.setGeometry(QRect(20, 30, 231, 41))
        self.tytulWybor = QLabel(self.centralwidget)
        self.tytulWybor.setObjectName(u"tytulWybor")
        self.tytulWybor.setGeometry(QRect(430, 50, 391, 61))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.tytulWybor.setFont(font)
        self.tytulWybor.setStyleSheet(u"")
        self.tytulWybor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tekstOpis = QTextBrowser(self.centralwidget)
        self.tekstOpis.setObjectName(u"tekstOpis")
        self.tekstOpis.setGeometry(QRect(390, 140, 451, 31))
        self.tekstOpis.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.tekstOpis.setFrameShape(QFrame.NoFrame)
        self.tekstPunkty = QTextBrowser(self.centralwidget)
        self.tekstPunkty.setObjectName(u"tekstPunkty")
        self.tekstPunkty.setGeometry(QRect(490, 200, 171, 31))
        self.tekstPunkty.setAutoFillBackground(False)
        self.tekstPunkty.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.tekstPunkty.setFrameShape(QFrame.NoFrame)
        self.liczbaPunktow = QLCDNumber(self.centralwidget)
        self.liczbaPunktow.setObjectName(u"liczbaPunktow")
        self.liczbaPunktow.setGeometry(QRect(660, 200, 64, 23))
        self.liczbaPunktow.setSmallDecimalPoint(False)
        self.liczbaPunktow.setDigitCount(4)
        self.liczbaPunktow.setMode(QLCDNumber.Dec)
        self.liczbaPunktow.setSegmentStyle(QLCDNumber.Flat)
        self.liczbaPunktow.setProperty("intValue", 0)
        self.tekstWynik = QTextBrowser(self.centralwidget)
        self.tekstWynik.setObjectName(u"tekstWynik")
        self.tekstWynik.setGeometry(QRect(250, 630, 241, 31))
        self.tekstWynik.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.tekstWynik.setFrameShape(QFrame.NoFrame)
        self.liczbaPunktow_2 = QLCDNumber(self.centralwidget)
        self.liczbaPunktow_2.setObjectName(u"liczbaPunktow_2")
        self.liczbaPunktow_2.setGeometry(QRect(480, 630, 61, 23))
        self.liczbaPunktow_2.setSmallDecimalPoint(False)
        self.liczbaPunktow_2.setDigitCount(4)
        self.liczbaPunktow_2.setMode(QLCDNumber.Dec)
        self.liczbaPunktow_2.setSegmentStyle(QLCDNumber.Flat)
        self.liczbaPunktow_2.setProperty("intValue", 0)
        self.tekstWynik_2 = QTextBrowser(self.centralwidget)
        self.tekstWynik_2.setObjectName(u"tekstWynik_2")
        self.tekstWynik_2.setGeometry(QRect(540, 630, 211, 31))
        self.tekstWynik_2.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.tekstWynik_2.setFrameShape(QFrame.NoFrame)
        self.tekstWynik_3 = QTextBrowser(self.centralwidget)
        self.tekstWynik_3.setObjectName(u"tekstWynik_3")
        self.tekstWynik_3.setGeometry(QRect(810, 630, 51, 31))
        self.tekstWynik_3.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.tekstWynik_3.setFrameShape(QFrame.NoFrame)
        self.liczbaMinut = QLCDNumber(self.centralwidget)
        self.liczbaMinut.setObjectName(u"liczbaMinut")
        self.liczbaMinut.setGeometry(QRect(750, 630, 64, 23))
        self.liczbaMinut.setSmallDecimalPoint(False)
        self.liczbaMinut.setDigitCount(4)
        self.liczbaMinut.setMode(QLCDNumber.Dec)
        self.liczbaMinut.setSegmentStyle(QLCDNumber.Flat)
        self.liczbaMinut.setProperty("intValue", 0)
        self.liczbaSekund = QLCDNumber(self.centralwidget)
        self.liczbaSekund.setObjectName(u"liczbaSekund")
        self.liczbaSekund.setGeometry(QRect(860, 630, 41, 23))
        self.liczbaSekund.setSmallDecimalPoint(False)
        self.liczbaSekund.setDigitCount(2)
        self.liczbaSekund.setMode(QLCDNumber.Dec)
        self.liczbaSekund.setSegmentStyle(QLCDNumber.Flat)
        self.liczbaSekund.setProperty("intValue", 0)
        self.tekstWynik_4 = QTextBrowser(self.centralwidget)
        self.tekstWynik_4.setObjectName(u"tekstWynik_4")
        self.tekstWynik_4.setGeometry(QRect(900, 630, 51, 31))
        self.tekstWynik_4.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.tekstWynik_4.setFrameShape(QFrame.NoFrame)
        self.startPrzycisk = QPushButton(self.centralwidget)
        self.startPrzycisk.setObjectName(u"startPrzycisk")
        self.startPrzycisk.setGeometry(QRect(540, 690, 141, 61))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(True)
        self.startPrzycisk.setFont(font1)
        self.startPrzycisk.setStyleSheet(u"")
        self.startPrzycisk.setCheckable(True)
        self.startPrzycisk.setChecked(False)
        self.uwagaTekst = QTextBrowser(self.centralwidget)
        self.uwagaTekst.setObjectName(u"uwagaTekst")
        self.uwagaTekst.setGeometry(QRect(395, 240, 441, 51))
        self.uwagaTekst.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.uwagaTekst.setFrameShape(QFrame.NoFrame)
        self.przecieciaPrzycisk = QRadioButton(self.centralwidget)
        self.przecieciaPrzycisk.setObjectName(u"przecieciaPrzycisk")
        self.przecieciaPrzycisk.setGeometry(QRect(1040, 30, 111, 20))
        self.posredniePrzycisk = QRadioButton(self.centralwidget)
        self.posredniePrzycisk.setObjectName(u"posredniePrzycisk")
        self.posredniePrzycisk.setGeometry(QRect(1040, 60, 141, 20))
        OknoZadania.setCentralWidget(self.centralwidget)

        self.retranslateUi(OknoZadania)

        QMetaObject.connectSlotsByName(OknoZadania)
    # setupUi

    def retranslateUi(self, OknoZadania):
        OknoZadania.setWindowTitle(QCoreApplication.translate("OknoZadania", u"MainWindow", None))
        self.powrotPrzycisk.setText(QCoreApplication.translate("OknoZadania", u"Powr\u00f3t do ekranu pocz\u0105tkowego", None))
        self.tytulWybor.setText(QCoreApplication.translate("OknoZadania", u"<html><head/><body><p align=\"center\">[metoda]</p></body></html>", None))
        self.tekstOpis.setHtml(QCoreApplication.translate("OknoZadania", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ZAZNACZ DOWOLN\u0104 ILO\u015a\u0106 PUNKT\u00d3W NA MAPIE, NASTEPNIE WCI\u015aNIJ START</p></body></html>", None))
        self.tekstPunkty.setHtml(QCoreApplication.translate("OknoZadania", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Aktualnie zaznaczone punkty: </p></body></html>", None))
        self.tekstWynik.setHtml(QCoreApplication.translate("OknoZadania", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WYNIK: Optymalna trasa sk\u0142adaj\u0105ca si\u0119 z</p></body></html>", None))
        self.tekstWynik_2.setHtml(QCoreApplication.translate("OknoZadania", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">punkt\u00f3w wyznaczona zosta\u0142a w czasie</p></body></html>", None))
        self.tekstWynik_3.setHtml(QCoreApplication.translate("OknoZadania", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">minut i</p></body></html>", None))
        self.tekstWynik_4.setHtml(QCoreApplication.translate("OknoZadania", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sekund.</p></body></html>", None))
        self.startPrzycisk.setText(QCoreApplication.translate("OknoZadania", u"START", None))
        self.uwagaTekst.setHtml(QCoreApplication.translate("OknoZadania", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">UWAGA! Rozwi\u0105zanie permutacyjne jest pogl\u0105dowe - czas oczekiwania na rozwi\u0105zanie dla wielu punkt\u00f3w pocz\u0105tkowych b\u0119dzie bardzo d\u0142ugi!</span></p></body></html>", None))
        self.przecieciaPrzycisk.setText(QCoreApplication.translate("OknoZadania", u"Unikaj przeci\u0119\u0107", None))
        self.posredniePrzycisk.setText(QCoreApplication.translate("OknoZadania", u"Poka\u017c trasy po\u015brednie", None))
    # retranslateUi

