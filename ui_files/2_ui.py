# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '2.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Recursos_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(811, 0)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(174, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(427, 641))
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 441, 541))
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 50, 371, 471))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgba(255, 225, 225,0);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 5px; /* Radio de borde */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    color: #2c3e50; /* Color del texto */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"}\n"
"\n"
"/* Estilo para QPushButton */\n"
"QPushButton {\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 5px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    color: #ffffff; /* Color del texto */\n"
"    background-color: #3498db; /* Color de fondo */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando se presiona */\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9; /* Cambio de color al presionar *"
                        "/\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid #2980b9; /* Cambio de borde al pasar el cursor */\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 8, 0, 1, 1)

        self.Correo_3 = QLineEdit(self.frame_2)
        self.Correo_3.setObjectName(u"Correo_3")

        self.gridLayout_2.addWidget(self.Correo_3, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_correo_3 = QLabel(self.frame_2)
        self.label_correo_3.setObjectName(u"label_correo_3")
        self.label_correo_3.setMinimumSize(QSize(0, 0))
        self.label_correo_3.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.label_correo_3.setFont(font)
        self.label_correo_3.setLayoutDirection(Qt.RightToLeft)
        self.label_correo_3.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_correo_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_correo_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.Registrarse_2 = QPushButton(self.frame_2)
        self.Registrarse_2.setObjectName(u"Registrarse_2")
        self.Registrarse_2.setStyleSheet(u"QPushButton#Registrarse {\n"
"    border: none; /* Sin borde */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    ; /* Color del texto */\n"
"	color: #3498db;\n"
"    background-color: transparent; /* Fondo transparente */\n"
"}\n"
"\n"
"/* Estilo para el bot\u00f3n cuando el cursor est\u00e1 encima */\n"
"QPushButton#Registrarse:hover {\n"
"     /* Cambio de color de letra al pasar el cursor */\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"/* Estilo para el bot\u00f3n cuando se presiona */\n"
"QPushButton#Registrarse:pressed {\n"
"    color: #2c3e50; /* Cambio de color de letra al presionar */\n"
"}")

        self.gridLayout_2.addWidget(self.Registrarse_2, 10, 0, 1, 1)

        self.acceder_3 = QPushButton(self.frame_2)
        self.acceder_3.setObjectName(u"acceder_3")

        self.gridLayout_2.addWidget(self.acceder_3, 9, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_password_3 = QLabel(self.frame_2)
        self.label_password_3.setObjectName(u"label_password_3")
        self.label_password_3.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_password_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_password_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        self.password_3 = QLineEdit(self.frame_2)
        self.password_3.setObjectName(u"password_3")
        self.password_3.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.password_3, 7, 0, 1, 1)

        self.label_titulo_3 = QLabel(self.frame_2)
        self.label_titulo_3.setObjectName(u"label_titulo_3")
        self.label_titulo_3.setMinimumSize(QSize(300, 100))
        self.label_titulo_3.setMaximumSize(QSize(500, 600))
        font1 = QFont()
        font1.setFamilies([u"Lucida Console"])
        font1.setPointSize(24)
        font1.setItalic(False)
        self.label_titulo_3.setFont(font1)
        self.label_titulo_3.setStyleSheet(u"	color: #000; /* Color del texto */\n"
"    padding: 10px; /* Padding */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"background-color: rgba(144, 238, 144, 0.5);\n"
"border-color: rgb(170, 170, 255);")
        self.label_titulo_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_titulo_3, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 2, 1)

        self.horizontalSpacer = QSpacerItem(174, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/fondos/fondoInisioSesion.jpg\"/></p></body></html>", None))
        self.Correo_3.setInputMask("")
        self.Correo_3.setPlaceholderText(QCoreApplication.translate("Form", u"example@email.com", None))
        self.label_correo_3.setText(QCoreApplication.translate("Form", u"Correo:", None))
        self.Registrarse_2.setText(QCoreApplication.translate("Form", u"\u00bfNo tienes una cuenta?", None))
        self.acceder_3.setText(QCoreApplication.translate("Form", u"ACCEDER", None))
        self.label_password_3.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a:", None))
        self.password_3.setPlaceholderText(QCoreApplication.translate("Form", u"************", None))
        self.label_titulo_3.setText(QCoreApplication.translate("Form", u"INICIO DE SESION", None))
    # retranslateUi

