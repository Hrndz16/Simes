# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frameUsuario.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)
import Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 218)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.usuario_frame = QFrame(self.centralwidget)
        self.usuario_frame.setObjectName(u"usuario_frame")
        self.usuario_frame.setMinimumSize(QSize(0, 200))
        self.usuario_frame.setStyleSheet(u"")
        self.usuario_frame.setFrameShape(QFrame.StyledPanel)
        self.usuario_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.usuario_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(self.usuario_frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color:rgb(151, 101, 27);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame = QFrame(self.usuario_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 170))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_perfil = QLabel(self.frame)
        self.img_perfil.setObjectName(u"img_perfil")
        self.img_perfil.setMinimumSize(QSize(150, 150))
        self.img_perfil.setMaximumSize(QSize(150, 150))
        self.img_perfil.setStyleSheet(u"image: url(:/iconos/icons8-nombre-100.png);")
        self.img_perfil.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img_perfil)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color:rgb(151, 101, 27);")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.label_nombre = QLabel(self.frame_3)
        self.label_nombre.setObjectName(u"label_nombre")

        self.gridLayout_2.addWidget(self.label_nombre, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.label_tipoU = QLabel(self.frame_3)
        self.label_tipoU.setObjectName(u"label_tipoU")

        self.gridLayout_2.addWidget(self.label_tipoU, 3, 0, 1, 1)

        self.label_correo = QLabel(self.frame_3)
        self.label_correo.setObjectName(u"label_correo")

        self.gridLayout_2.addWidget(self.label_correo, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color:rgb(151, 101, 27);")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Boton_eliminar = QPushButton(self.frame)
        self.Boton_eliminar.setObjectName(u"Boton_eliminar")
        self.Boton_eliminar.setMaximumSize(QSize(100, 70))
        self.Boton_eliminar.setStyleSheet(u"/* Estilo para QPushButton */\n"
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

        self.horizontalLayout.addWidget(self.Boton_eliminar)


        self.verticalLayout.addWidget(self.frame)

        self.line_2 = QFrame(self.usuario_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color:rgb(151, 101, 27);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)


        self.verticalLayout_2.addWidget(self.usuario_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_perfil.setText("")
        self.label_nombre.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_tipoU.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_correo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Boton_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

