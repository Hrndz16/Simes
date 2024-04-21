# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ItemHora.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ItemHora(object):
    def setupUi(self, ItemHora):
        if not ItemHora.objectName():
            ItemHora.setObjectName(u"ItemHora")
        ItemHora.resize(751, 190)
        ItemHora.setMinimumSize(QSize(0, 190))
        ItemHora.setMaximumSize(QSize(16777215, 190))
        self.verticalLayout = QVBoxLayout(ItemHora)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(ItemHora)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.base_horas_eventos = QFrame(ItemHora)
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
        self.Hora.setMaximumSize(QSize(114, 100))
        self.Hora.setStyleSheet(u".QLabel {\n"
"    font-size: 14px; /* Tama\u00f1o de fuente normal */\n"
"    color: #666; /* Color de texto m\u00e1s claro */\n"
"}")

        self.horizontalLayout_7.addWidget(self.Hora)

        self.line_4 = QFrame(self.base_horas_eventos)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 16777215))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_4)

        self.frame = QFrame(self.base_horas_eventos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        font.setBold(False)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.Descripcion = QLabel(self.frame)
        self.Descripcion.setObjectName(u"Descripcion")
        self.Descripcion.setMinimumSize(QSize(0, 100))
        self.Descripcion.setMaximumSize(QSize(16777215, 100))
        self.Descripcion.setStyleSheet(u".QLabel{\n"
"    font-size: 14px; /* Tama\u00f1o de fuente normal */\n"
"    color: #666; /* Color de texto m\u00e1s claro */\n"
"}")

        self.verticalLayout_2.addWidget(self.Descripcion)


        self.horizontalLayout_7.addWidget(self.frame)

        self.line_5 = QFrame(self.base_horas_eventos)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_5)

        self.boton_sub = QPushButton(self.base_horas_eventos)
        self.boton_sub.setObjectName(u"boton_sub")
        self.boton_sub.setMaximumSize(QSize(120, 100))
        self.boton_sub.setBaseSize(QSize(0, 0))
        self.boton_sub.setStyleSheet(u"/* Estilo para QPushButton */\n"
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

        self.horizontalLayout_7.addWidget(self.boton_sub)


        self.verticalLayout.addWidget(self.base_horas_eventos)

        self.line_2 = QFrame(ItemHora)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)


        self.retranslateUi(ItemHora)

        QMetaObject.connectSlotsByName(ItemHora)
    # setupUi

    def retranslateUi(self, ItemHora):
        ItemHora.setWindowTitle(QCoreApplication.translate("ItemHora", u"Form", None))
        self.Hora.setText(QCoreApplication.translate("ItemHora", u"1-4pm", None))
        self.label.setText(QCoreApplication.translate("ItemHora", u"Corona de oro", None))
        self.Descripcion.setText(QCoreApplication.translate("ItemHora", u"Exposicion de la corona de oro", None))
        self.boton_sub.setText(QCoreApplication.translate("ItemHora", u"Suscribirse", None))
    # retranslateUi

