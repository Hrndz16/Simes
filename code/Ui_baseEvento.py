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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
        self.line_6 = QFrame(self.Frame_base_evento)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_6, 4, 0, 1, 2)

        self.line_3 = QFrame(self.Frame_base_evento)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_3, 2, 0, 1, 2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)

        self.Titulo_evento = QLabel(self.Frame_base_evento)
        self.Titulo_evento.setObjectName(u"Titulo_evento")
        self.Titulo_evento.setMinimumSize(QSize(0, 100))
        self.Titulo_evento.setMaximumSize(QSize(16777215, 100))
        self.Titulo_evento.setStyleSheet(u"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente m\u00e1s grande */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: #333; /* Color de texto m\u00e1s oscuro */\n"
"}")

        self.gridLayout_7.addWidget(self.Titulo_evento, 0, 0, 1, 1)

        self.base_horas_eventos = QFrame(self.Frame_base_evento)
        self.base_horas_eventos.setObjectName(u"base_horas_eventos")
        self.base_horas_eventos.setMaximumSize(QSize(16777215, 200))
        self.base_horas_eventos.setFrameShape(QFrame.StyledPanel)
        self.base_horas_eventos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.base_horas_eventos)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(7, 0, 9, 0)
        self.Hora = QLabel(self.base_horas_eventos)
        self.Hora.setObjectName(u"Hora")
        self.Hora.setMinimumSize(QSize(0, 100))
        self.Hora.setMaximumSize(QSize(100, 100))
        self.Hora.setStyleSheet(u".QLabel {\n"
"    font-size: 14px; /* Tama\u00f1o de fuente normal */\n"
"    color: #666; /* Color de texto m\u00e1s claro */\n"
"}")

        self.horizontalLayout_7.addWidget(self.Hora)

        self.line_4 = QFrame(self.base_horas_eventos)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 100))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_4)

        self.Descripcion = QLabel(self.base_horas_eventos)
        self.Descripcion.setObjectName(u"Descripcion")
        self.Descripcion.setMinimumSize(QSize(0, 100))
        self.Descripcion.setMaximumSize(QSize(16777215, 100))
        self.Descripcion.setStyleSheet(u".QLabel{\n"
"    font-size: 14px; /* Tama\u00f1o de fuente normal */\n"
"    color: #666; /* Color de texto m\u00e1s claro */\n"
"}")

        self.horizontalLayout_7.addWidget(self.Descripcion)

        self.line_5 = QFrame(self.base_horas_eventos)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_5)

        self.pushButton = QPushButton(self.base_horas_eventos)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(120, 100))
        self.pushButton.setBaseSize(QSize(0, 0))
        self.pushButton.setStyleSheet(u"/* Estilo para QPushButton */\n"
".QPushButton {\n"
"    background-color: #0078D4; /* Color de fondo */\n"
"    color: white; /* Color de texto */\n"
"    border: none; /* Sin borde */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: #005499; /* Cambia el color de fondo al pasar el mouse */\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #003366; /* Cambia el color de fondo al hacer clic */\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.gridLayout_7.addWidget(self.base_horas_eventos, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 5, 0, 1, 1)


        self.verticalLayout.addWidget(self.Frame_base_evento)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo_evento.setText(QCoreApplication.translate("MainWindow", u"Lunes 1-4-23", None))
        self.Hora.setText(QCoreApplication.translate("MainWindow", u"1-4pm", None))
        self.Descripcion.setText(QCoreApplication.translate("MainWindow", u"Exposicion de la corona de oro", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Suscribirse", None))
    # retranslateUi

