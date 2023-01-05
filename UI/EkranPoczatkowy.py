# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EkranPoczatkowy.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)
# import zasoby_rc

class Ui_EkranPoczatkowy(object):
    def setupUi(self, EkranPoczatkowy):
        if not EkranPoczatkowy.objectName():
            EkranPoczatkowy.setObjectName(u"EkranPoczatkowy")
        EkranPoczatkowy.setWindowModality(Qt.NonModal)
        EkranPoczatkowy.resize(1200, 800)
        EkranPoczatkowy.setStyleSheet(u"QWidget{\n"
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
"}\n"
"\n"
"")
        self.centralwidget = QWidget(EkranPoczatkowy)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tytul = QLabel(self.centralwidget)
        self.tytul.setObjectName(u"tytul")
        self.tytul.setGeometry(QRect(420, 60, 371, 121))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.tytul.setFont(font)
        self.tytul.setStyleSheet(u"")
        self.tekstAutor = QTextBrowser(self.centralwidget)
        self.tekstAutor.setObjectName(u"tekstAutor")
        self.tekstAutor.setGeometry(QRect(930, 600, 256, 192))
        self.tekstAutor.setFrameShape(QFrame.NoFrame)
        self.tekstWersja = QLabel(self.centralwidget)
        self.tekstWersja.setObjectName(u"tekstWersja")
        self.tekstWersja.setGeometry(QRect(10, 760, 121, 16))
        font1 = QFont()
        font1.setItalic(True)
        self.tekstWersja.setFont(font1)
        self.startPrzycisk = QPushButton(self.centralwidget)
        self.startPrzycisk.setObjectName(u"startPrzycisk")
        self.startPrzycisk.setGeometry(QRect(540, 350, 141, 61))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setItalic(True)
        self.startPrzycisk.setFont(font2)
        self.startPrzycisk.setStyleSheet(u"")
        self.startPrzycisk.setCheckable(True)
        self.startPrzycisk.setChecked(False)
        self.koniecPrzycisk = QPushButton(self.centralwidget)
        self.koniecPrzycisk.setObjectName(u"koniecPrzycisk")
        self.koniecPrzycisk.setGeometry(QRect(540, 470, 141, 61))
        self.koniecPrzycisk.setFont(font2)
        self.koniecPrzycisk.setStyleSheet(u"")
        self.koniecPrzycisk.setCheckable(True)
        self.koniecPrzycisk.setChecked(False)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(280, 220, 661, 81))
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.helikopter = QLabel(self.centralwidget)
        self.helikopter.setObjectName(u"helikopter")
        self.helikopter.setGeometry(QRect(70, 310, 381, 321))
        self.helikopter.setStyleSheet(u"")
        self.helikopter.setPixmap(QPixmap(u":/Obrazy/images/helicopter-ga81252117_640.png"))
        self.helikopter.setScaledContents(True)
        EkranPoczatkowy.setCentralWidget(self.centralwidget)

        self.retranslateUi(EkranPoczatkowy)

        QMetaObject.connectSlotsByName(EkranPoczatkowy)
    # setupUi

    def retranslateUi(self, EkranPoczatkowy):
        EkranPoczatkowy.setWindowTitle(QCoreApplication.translate("EkranPoczatkowy", u"MainWindow", None))
        self.tytul.setText(QCoreApplication.translate("EkranPoczatkowy", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">HELIKOPTEROWY</span></p><p align=\"center\"><span style=\" font-weight:700;\">KOMIWOJA\u017bER</span></p></body></html>", None))
        self.tekstAutor.setHtml(QCoreApplication.translate("EkranPoczatkowy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Opracowanie:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0141ukasz Bladziak, PUT Teleinformatyka</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Promotor</span>:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\">dr in\u017c. Andrzej Urba\u0144ski</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Aplikacj\u0119 wykonano na potrzeby powstania pracy dyplomowej in\u017cynierskiej pt. &quot;Eksperymentalna analiza algoryt\u00f3w rozwi\u0105zuj\u0105cych problem komiwoja\u017cera w j\u0119zyku Python&quot;.</span></p></body></html>", None))
        self.tekstWersja.setText(QCoreApplication.translate("EkranPoczatkowy", u"Wersja aplikacji: 1.1", None))
        self.startPrzycisk.setText(QCoreApplication.translate("EkranPoczatkowy", u"START", None))
        self.koniecPrzycisk.setText(QCoreApplication.translate("EkranPoczatkowy", u"ZAKO\u0143CZ", None))
        self.textBrowser.setHtml(QCoreApplication.translate("EkranPoczatkowy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Od kilku dni panuje straszna ulewa, co skutkuje zalan\u0105 okolic\u0105.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Wykorzystuj\u0105c sw\u00f3j helikopter mo\u017cesz pom\u00f3c mieszka\u0144com, ale potrzebne s\u0105 do tego r\u00f3wnie\u017c du\u017ce zapasy paliwa.."
                        ".</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Skorzystaj z aplikacji &quot;Helikopterowy Komiwoja\u017cer&quot;, aby pom\u00f3c wszyskim potrzebuj\u0105cym w optymalny spos\u00f3b!</span></p></body></html>", None))
        self.helikopter.setText("")
    # retranslateUi

