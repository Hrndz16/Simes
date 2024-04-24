# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CancelarEvento.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 213)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_cancelacionEvento = QFrame(self.centralwidget)
        self.frame_cancelacionEvento.setObjectName(u"frame_cancelacionEvento")
        self.frame_cancelacionEvento.setFrameShape(QFrame.StyledPanel)
        self.frame_cancelacionEvento.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_cancelacionEvento)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.base_horas_eventos = QFrame(self.frame_cancelacionEvento)
        self.base_horas_eventos.setObjectName(u"base_horas_eventos")
        self.base_horas_eventos.setMaximumSize(QSize(16777215, 200))
        self.base_horas_eventos.setFrameShape(QFrame.StyledPanel)
        self.base_horas_eventos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.base_horas_eventos)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(7, 0, 9, 0)
        self.frame_3 = QFrame(self.base_horas_eventos)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setMaximumSize(QSize(250, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_fecha = QLabel(self.frame_3)
        self.label_fecha.setObjectName(u"label_fecha")

        self.verticalLayout.addWidget(self.label_fecha)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_hora = QLabel(self.frame_3)
        self.label_hora.setObjectName(u"label_hora")

        self.verticalLayout.addWidget(self.label_hora)


        self.horizontalLayout_7.addWidget(self.frame_3)

        self.line_4 = QFrame(self.base_horas_eventos)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 16777215))
        self.line_4.setStyleSheet(u"background-color: rgb(178, 121, 36);")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_4)

        self.frame_2 = QFrame(self.base_horas_eventos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_titulo = QLabel(self.frame_2)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(22)
        font.setBold(False)
        self.label_titulo.setFont(font)

        self.verticalLayout_2.addWidget(self.label_titulo)

        self.label_descripcion = QLabel(self.frame_2)
        self.label_descripcion.setObjectName(u"label_descripcion")
        self.label_descripcion.setMinimumSize(QSize(0, 100))
        self.label_descripcion.setMaximumSize(QSize(16777215, 100))
        self.label_descripcion.setStyleSheet(u".QLabel{\n"
"    font-size: 14px; /* Tama\u00f1o de fuente normal */\n"
"    color: #666; /* Color de texto m\u00e1s claro */\n"
"}")

        self.verticalLayout_2.addWidget(self.label_descripcion)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.line_5 = QFrame(self.base_horas_eventos)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(178, 121, 36);")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_5)

        self.boton_CancelarEvento = QPushButton(self.base_horas_eventos)
        self.boton_CancelarEvento.setObjectName(u"boton_CancelarEvento")
        self.boton_CancelarEvento.setMaximumSize(QSize(120, 100))
        self.boton_CancelarEvento.setBaseSize(QSize(0, 0))
        self.boton_CancelarEvento.setStyleSheet(u"/* Estilo para QPushButton */\n"
".QPushButton {\n"
"    background-color: #c57007; /* Color de fondo */\n"
"    color: white; /* Color de texto */\n"
"    border: none; /* Sin borde */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"     color: #fff; /* Color del texto al pasar el cursor */\n"
"    background-color:#f49011 ;/* Cambiar el color de fondo al pasar el mouse */\n"
"    border-color:#f49011;/* Cambia el color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:presset{\n"
"	 background-color: #c57007;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.boton_CancelarEvento)


        self.gridLayout_2.addWidget(self.base_horas_eventos, 1, 0, 1, 1)

        self.line = QFrame(self.frame_cancelacionEvento)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(178, 121, 36);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_cancelacionEvento, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_fecha.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hora: ", None))
        self.label_hora.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"Corona de oro", None))
        self.label_descripcion.setText(QCoreApplication.translate("MainWindow", u"Exposicion de la corona de oro", None))
        self.boton_CancelarEvento.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

