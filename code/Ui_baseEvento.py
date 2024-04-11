# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'baseEvento.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 457)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Frame_base_evento = QFrame(self.centralwidget)
        self.Frame_base_evento.setObjectName(u"Frame_base_evento")
        self.Frame_base_evento.setMinimumSize(QSize(0, 0))
        self.Frame_base_evento.setMaximumSize(QSize(16777215, 16777215))
        self.Frame_base_evento.setAutoFillBackground(False)
        self.Frame_base_evento.setStyleSheet(u"")
        self.Frame_base_evento.setFrameShape(QFrame.StyledPanel)
        self.Frame_base_evento.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.Frame_base_evento)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.dia_evento = QLabel(self.Frame_base_evento)
        self.dia_evento.setObjectName(u"dia_evento")
        self.dia_evento.setMinimumSize(QSize(0, 100))
        self.dia_evento.setMaximumSize(QSize(16777215, 100))
        self.dia_evento.setStyleSheet(u"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente m\u00e1s grande */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: #333; /* Color de texto m\u00e1s oscuro */\n"
"}")

        self.gridLayout_7.addWidget(self.dia_evento, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.Frame_base_evento)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dia_evento.setText(QCoreApplication.translate("MainWindow", u"Lunes 1-4-23", None))
    # retranslateUi

