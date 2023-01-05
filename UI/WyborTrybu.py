# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WyborTrybu.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)
# import zasoby_rc
# import zasoby_rc

class Ui_WyborTrybu(object):
    def setupUi(self, WyborTrybu):
        if not WyborTrybu.objectName():
            WyborTrybu.setObjectName(u"WyborTrybu")
        WyborTrybu.resize(1200, 800)
        WyborTrybu.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(207, 240, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
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
        self.centralwidget = QWidget(WyborTrybu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.permutacjaPrzycisk = QPushButton(self.centralwidget)
        self.permutacjaPrzycisk.setObjectName(u"permutacjaPrzycisk")
        self.permutacjaPrzycisk.setGeometry(QRect(170, 430, 231, 61))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.permutacjaPrzycisk.setFont(font)
        self.permutacjaPrzycisk.setStyleSheet(u"")
        self.permutacjaPrzycisk.setCheckable(True)
        self.permutacjaPrzycisk.setChecked(False)
        self.bnbPrzycisk = QPushButton(self.centralwidget)
        self.bnbPrzycisk.setObjectName(u"bnbPrzycisk")
        self.bnbPrzycisk.setGeometry(QRect(500, 430, 231, 61))
        self.bnbPrzycisk.setFont(font)
        self.bnbPrzycisk.setStyleSheet(u"")
        self.bnbPrzycisk.setCheckable(True)
        self.bnbPrzycisk.setChecked(False)
        self.genetycznyPrzycisk = QPushButton(self.centralwidget)
        self.genetycznyPrzycisk.setObjectName(u"genetycznyPrzycisk")
        self.genetycznyPrzycisk.setGeometry(QRect(830, 430, 231, 61))
        self.genetycznyPrzycisk.setFont(font)
        self.genetycznyPrzycisk.setStyleSheet(u"")
        self.genetycznyPrzycisk.setCheckable(True)
        self.genetycznyPrzycisk.setChecked(False)
        self.powrotPrzycisk = QCommandLinkButton(self.centralwidget)
        self.powrotPrzycisk.setObjectName(u"powrotPrzycisk")
        self.powrotPrzycisk.setGeometry(QRect(20, 20, 231, 41))
        self.tytulWybor = QLabel(self.centralwidget)
        self.tytulWybor.setObjectName(u"tytulWybor")
        self.tytulWybor.setGeometry(QRect(440, 110, 331, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe Script"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.tytulWybor.setFont(font1)
        self.tytulWybor.setStyleSheet(u"")
        self.tytulWybor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tekstOpis = QTextBrowser(self.centralwidget)
        self.tekstOpis.setObjectName(u"tekstOpis")
        self.tekstOpis.setGeometry(QRect(420, 200, 371, 31))
        self.tekstOpis.setFrameShape(QFrame.NoFrame)
        WyborTrybu.setCentralWidget(self.centralwidget)

        self.retranslateUi(WyborTrybu)

        QMetaObject.connectSlotsByName(WyborTrybu)
    # setupUi

    def retranslateUi(self, WyborTrybu):
        WyborTrybu.setWindowTitle(QCoreApplication.translate("WyborTrybu", u"MainWindow", None))
        self.permutacjaPrzycisk.setText(QCoreApplication.translate("WyborTrybu", u"ROZWI\u0104ZANIE PERMUTACYJNE", None))
        self.bnbPrzycisk.setText(QCoreApplication.translate("WyborTrybu", u"METODA PODZIA\u0141U I OGRANICZE\u0143", None))
        self.genetycznyPrzycisk.setText(QCoreApplication.translate("WyborTrybu", u"ALGORYTM GENETYCZNY", None))
        self.powrotPrzycisk.setText(QCoreApplication.translate("WyborTrybu", u"Powr\u00f3t do ekranu pocz\u0105tkowego", None))
        self.tytulWybor.setText(QCoreApplication.translate("WyborTrybu", u"<html><head/><body><p align=\"center\">WYB\u00d3R METODY</p></body></html>", None))
        self.tekstOpis.setHtml(QCoreApplication.translate("WyborTrybu", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WYBIERZ METOD\u0118 ROZWI\u0104ZANIA PROBLEMU KOMIWOJA\u017bERA</p></body></html>", None))
    # retranslateUi

