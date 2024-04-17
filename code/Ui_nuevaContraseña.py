# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevaContraseña.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Recursos_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(340, 350)
        Dialog.setMaximumSize(QSize(350, 350))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0625 rgba(243, 135, 4, 255), stop:0.835227 rgba(252, 238, 151, 255));")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	color: rgb(109, 70, 3);\n"
"	background-color: rgba(188, 94, 0,100);\n"
"\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    color: #2c3e50; /* Color del texto */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"}\n"
"\n"
"/* Estilo para QPushButton */\n"
"QPushButton {\n"
"    border: 2px solid  rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    color: #ffffff; /* Color del texto */\n"
"    background-color:  rgb(109, 70, 3); /* Color de fondo */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando se presiona */\n"
"QPushButton:pressed {\n"
"    background-color:  rgb"
                        "a(109, 70, 3,200); /* Cambio de color al presionar */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QPushButton:hover {\n"
"    background-color: rgba(109, 70, 3,150); /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid  rgba(109, 70, 3,150); /* Cambio de borde al pasar el cursor */\n"
"}\n"
"\n"
"/* Estilo para QComboBox */\n"
"QComboBox {\n"
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    color: #2c3e50; /* Color del texto */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"}\n"
"\n"
"/* Estilo para QComboBox cuando se despliega */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    width: 20px; /* Ancho del bot\u00f3n desplegable */\n"
"    border-left-width: 0px; /* Sin borde a la"
                        " izquierda del bot\u00f3n */\n"
"    border-top-right-radius: 5px; /* Radio de borde superior derecho */\n"
"    border-bottom-right-radius: 5px; /* Radio de borde inferior derecho */\n"
"    background-color: rgb(109, 70, 3); /* Color de fondo del bot\u00f3n desplegable */\n"
"}\n"
"\n"
"/* Estilo para QComboBox cuando se despliega y se presiona */\n"
"QComboBox::down-arrow {\n"
"    width: 15px; /* Ancho del icono */\n"
"    height: 15px; /* Alto del icono */\n"
"    padding-right: 5px; /* Espaciado a la derecha del icono */\n"
"}\n"
"QLabel{\n"
"color: #2c3e50; /* Color del texto */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: transparent; /* Color de fondo */\n"
"\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"CONTRASE\u00d1A", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"NUEVA CONTRASE\u00d1A", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"VERIFICAR NUEVAMENTE LA CONTRASE\u00d1A", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
    # retranslateUi

