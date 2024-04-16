# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTimeEdit, QToolButton,
    QVBoxLayout, QWidget)
import Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(871, 661)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.198864 rgba(0, 79, 129, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"/*background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.198864 rgba(0, 4, 75, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"/*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.278409 rgba(243, 135, 4, 255), stop:0.835227 rgba(252, 249, 173, 255));*/\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0625 rgba(243, 135, 4, 255), stop:0.835227 rgba(252, 238, 151, 255));")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Frame_menu = QFrame(self.centralwidget)
        self.Frame_menu.setObjectName(u"Frame_menu")
        self.Frame_menu.setMinimumSize(QSize(0, 0))
        self.Frame_menu.setMaximumSize(QSize(16777215, 76))
        self.Frame_menu.setStyleSheet(u"QFrame#Frame_menu{\n"
"\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.198864 rgba(0, 79, 129, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgba(0,0,0,0);\n"
"\n"
"/*border-radius:30px*/\n"
"}\n"
"QPushButton{\n"
"background-color: white;\n"
"    border: solid 5px black;\n"
"    border-radius: 50%;\n"
"}\n"
"")
        self.Frame_menu.setFrameShape(QFrame.StyledPanel)
        self.Frame_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Boton_inicio = QPushButton(self.Frame_menu)
        self.Boton_inicio.setObjectName(u"Boton_inicio")
        self.Boton_inicio.setMaximumSize(QSize(75, 52))
        self.Boton_inicio.setStyleSheet(u"QPushButton#Boton_inicio {\n"
"	background-color: rgb(207, 118, 7);\n"
"    font-weight: 400;\n"
"    color: #000; /* Color del texto */\n"
"    border: 1px solid transparent;\n"
"    padding: 9px 18px; /* Padding */\n"
"    font-size: 8px; /* Tama\u00f1o de la fuente */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"}\n"
"\n"
"QPushButton#Boton_inicio:hover {\n"
"    color: #fff; /* Color del texto al pasar el cursor */\n"
"    background-color:#f49011 ;/* Cambiar el color de fondo al pasar el mouse */\n"
"    border-color:#f49011;/* Cambiar el color del borde al pasar el mouse */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/iconos/icons8-casa-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_inicio.setIcon(icon)
        self.Boton_inicio.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.Boton_inicio)

        self.horizontalSpacer = QSpacerItem(650, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Boton_ingresar = QPushButton(self.Frame_menu)
        self.Boton_ingresar.setObjectName(u"Boton_ingresar")
        self.Boton_ingresar.setBaseSize(QSize(0, 6))
        font = QFont()
        font.setBold(False)
        self.Boton_ingresar.setFont(font)
        self.Boton_ingresar.setStyleSheet(u"QPushButton#Boton_ingresar {\n"
"	background-color: #c57007;/* Color de fondo */\n"
"    font-weight: 400;\n"
"    color: #000; /* Color del texto */\n"
"    border: 1px solid transparent;\n"
"    padding: 9px 18px; /* Padding */\n"
"    font-size: 10px; /* Tama\u00f1o de la fuente */\n"
"    border-radius: 20px; /* Bordes redondeados */\n"
"}\n"
"\n"
"QPushButton#Boton_ingresar:hover {\n"
"    color: #fff; /* Color del texto al pasar el cursor */\n"
"    background-color:#f49011 ;/* Cambiar el color de fondo al pasar el mouse */\n"
"    border-color:#f49011;/* Cambiar el color del borde al pasar el mouse */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/icons8-usuario-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_ingresar.setIcon(icon1)
        self.Boton_ingresar.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.Boton_ingresar)


        self.verticalLayout.addWidget(self.Frame_menu)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(243, 135, 4);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.contenido = QFrame(self.centralwidget)
        self.contenido.setObjectName(u"contenido")
        self.contenido.setStyleSheet(u"background-color: rgba(149, 39, 39,0);")
        self.contenido.setFrameShape(QFrame.StyledPanel)
        self.contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contenido)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_principal = QStackedWidget(self.contenido)
        self.stackedWidget_principal.setObjectName(u"stackedWidget_principal")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_principal.sizePolicy().hasHeightForWidth())
        self.stackedWidget_principal.setSizePolicy(sizePolicy)
        self.stackedWidget_principal.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget_principal.setAutoFillBackground(False)
        self.stackedWidget_principal.setStyleSheet(u"background-color:transparent;\n"
"border-color:transparent;")
        self.stackedWidget_principal.setLocale(QLocale(QLocale.Swahili, QLocale.Tanzania))
        self.stackedWidget_principal.setLineWidth(1)
        self.page_1_inicio = QWidget()
        self.page_1_inicio.setObjectName(u"page_1_inicio")
        self.page_1_inicio.setStyleSheet(u"QFrame#Frame_menu{\n"
"	background-color:transparent;\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.page_1_inicio)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 6)
        self.Area_1 = QScrollArea(self.page_1_inicio)
        self.Area_1.setObjectName(u"Area_1")
        self.Area_1.setStyleSheet(u"/*background-color: rgb(255, 225, 225);*/\n"
"background-color: rgba(255, 255, 255,0);")
        self.Area_1.setWidgetResizable(True)
        self.Contenido1 = QWidget()
        self.Contenido1.setObjectName(u"Contenido1")
        self.Contenido1.setGeometry(QRect(0, 0, 1122, 886))
        self.verticalLayout_2 = QVBoxLayout(self.Contenido1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menudeslizante_frame = QFrame(self.Contenido1)
        self.menudeslizante_frame.setObjectName(u"menudeslizante_frame")
        self.menudeslizante_frame.setMaximumSize(QSize(16777215, 16777215))
        self.menudeslizante_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.menudeslizante_frame.setFrameShape(QFrame.StyledPanel)
        self.menudeslizante_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menudeslizante_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.informaciones = QFrame(self.menudeslizante_frame)
        self.informaciones.setObjectName(u"informaciones")
        self.informaciones.setStyleSheet(u"")
        self.informaciones.setFrameShape(QFrame.StyledPanel)
        self.informaciones.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.informaciones)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 5, 5)
        self.frame = QFrame(self.informaciones)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(12, 26, 27,40);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.general = QFrame(self.frame)
        self.general.setObjectName(u"general")
        self.general.setMaximumSize(QSize(300, 377))
        self.general.setStyleSheet(u"QLabel{\n"
"background-color:transparent;\n"
"}\n"
"QFrame{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.general.setFrameShape(QFrame.StyledPanel)
        self.general.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.general)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.general)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:transparent;\n"
"}")

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_18 = QLabel(self.general)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_18, 13, 1, 1, 1)

        self.label_13 = QLabel(self.general)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_13, 7, 1, 1, 1)

        self.label_12 = QLabel(self.general)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_12, 5, 1, 1, 1)

        self.label_11 = QLabel(self.general)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)

        self.label_9 = QLabel(self.general)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 50))
        self.label_9.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setPixmap(QPixmap(u":/iconos/icons8-reloj-96.png"))
        self.label_9.setScaledContents(True)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_22 = QLabel(self.general)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_22, 9, 1, 1, 1)

        self.label_24 = QLabel(self.general)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(45, 45))
        self.label_24.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_24.setTextFormat(Qt.AutoText)
        self.label_24.setPixmap(QPixmap(u":/iconos/icons8-mail-50.png"))
        self.label_24.setScaledContents(True)

        self.gridLayout.addWidget(self.label_24, 9, 0, 1, 1)

        self.label_23 = QLabel(self.general)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_23, 8, 1, 1, 1)

        self.label_10 = QLabel(self.general)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"background-color:rgba(0,0,0,0,)\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)

        self.label_19 = QLabel(self.general)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_19, 12, 1, 1, 1)

        self.label_17 = QLabel(self.general)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_17, 14, 1, 1, 1)

        self.label_21 = QLabel(self.general)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_21, 10, 1, 1, 1)

        self.label_14 = QLabel(self.general)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_14, 6, 1, 1, 1)

        self.label_20 = QLabel(self.general)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_20, 11, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.general)


        self.horizontalLayout_8.addWidget(self.frame)

        self.Cartelera = QFrame(self.informaciones)
        self.Cartelera.setObjectName(u"Cartelera")
        self.Cartelera.setMaximumSize(QSize(16777215, 16777215))
        self.Cartelera.setStyleSheet(u"QFrame#titulo_cartel_1,#titulo_cartel_2,#titulo_cartel_3{\n"
"font: 75 18pt \"MS Serif\";\n"
"\n"
"}\n"
"QFrame#cuerpo_cartel_1,#cuerpo_cartel_2,#cuerpo_cartel_3{\n"
"font: italic 12pt \"Sitka\";\n"
"\n"
"}\n"
"QFrame{\n"
"	background-color: rgba(243, 221, 171,70);\n"
"}")
        self.Cartelera.setFrameShape(QFrame.StyledPanel)
        self.Cartelera.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Cartelera)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, -1, -1)
        self.frame_10 = QFrame(self.Cartelera)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 70))
        self.frame_10.setStyleSheet(u"background-color:transparent;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Bonton_proxEvento = QPushButton(self.frame_10)
        self.Bonton_proxEvento.setObjectName(u"Bonton_proxEvento")
        self.Bonton_proxEvento.setMinimumSize(QSize(180, 40))
        self.Bonton_proxEvento.setMaximumSize(QSize(180, 40))
        self.Bonton_proxEvento.setStyleSheet(u"QPushButton {\n"
"	color: rgb(244, 144, 17);\n"
"	\n"
"	background-color: rgb(207, 118, 7); /* Color de fondo */\n"
"    color: white; /* Color del texto */\n"
"    border: solid transparent;\n"
"    border-color:rgb(168, 13, 13);  /* Color del borde */\n"
"    border-radius: 10px; /* Radio de borde para esquinas redondeadas */\n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Peso de la fuente */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#f49011 ;/* Cambiar el color de fondo al pasar el mouse */\n"
"    border-color:#f49011;/* Cambiar el color del borde al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f38704; /* Cambiar el color de fondo al hacer clic */\n"
"    border-color:#f38704;/* Cambiar el color del borde al hacer clic */\n"
"}")

        self.horizontalLayout_5.addWidget(self.Bonton_proxEvento)

        self.horizontalSpacer_25 = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_25)

        self.Boton_objetos = QPushButton(self.frame_10)
        self.Boton_objetos.setObjectName(u"Boton_objetos")
        self.Boton_objetos.setMinimumSize(QSize(180, 40))
        self.Boton_objetos.setMaximumSize(QSize(180, 16777215))
        self.Boton_objetos.setStyleSheet(u"QPushButton {\n"
"	background-color: #cf7607;  /* Color de fondo */\n"
"    color: white; /* Color del texto */\n"
"    border: 1px solid transparent;\n"
"    border-color: transparent;\n"
"    border-radius: 10px; /* Radio de borde para esquinas redondeadas */\n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Peso de la fuente */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#f49011 ;/* Cambiar el color de fondo al pasar el mouse */\n"
"    border-color:#f49011;/* Cambiar el color del borde al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f38704; /* Cambiar el color de fondo al hacer clic */\n"
"    border-color:#f38704;/* Cambiar el color del borde al hacer clic */\n"
"}")

        self.horizontalLayout_5.addWidget(self.Boton_objetos)

        self.horizontalSpacer_4 = QSpacerItem(320, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.cartel_1 = QFrame(self.Cartelera)
        self.cartel_1.setObjectName(u"cartel_1")
        self.cartel_1.setMinimumSize(QSize(0, 250))
        self.cartel_1.setMaximumSize(QSize(16777215, 16777215))
        self.cartel_1.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	/*background-color: rgba(168, 168, 168,70);*/\n"
"	/*background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.198864 rgba(0, 79, 129, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"border-radius: 13px \n"
"}\n"
"")
        self.cartel_1.setFrameShape(QFrame.StyledPanel)
        self.cartel_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.cartel_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.titulo_cartel_1 = QLabel(self.cartel_1)
        self.titulo_cartel_1.setObjectName(u"titulo_cartel_1")
        self.titulo_cartel_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.titulo_cartel_1, 2, 0, 1, 1)

        self.imagen_cartel_1 = QLabel(self.cartel_1)
        self.imagen_cartel_1.setObjectName(u"imagen_cartel_1")
        self.imagen_cartel_1.setStyleSheet(u"border-radius: 20px ")
        self.imagen_cartel_1.setTextFormat(Qt.RichText)
        self.imagen_cartel_1.setPixmap(QPixmap(u":/Carteles/cartel1.png"))
        self.imagen_cartel_1.setScaledContents(True)
        self.imagen_cartel_1.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.imagen_cartel_1.setWordWrap(False)

        self.gridLayout_2.addWidget(self.imagen_cartel_1, 2, 1, 4, 1)

        self.cuerpo_cartel_1 = QLabel(self.cartel_1)
        self.cuerpo_cartel_1.setObjectName(u"cuerpo_cartel_1")
        self.cuerpo_cartel_1.setMinimumSize(QSize(300, 0))
        self.cuerpo_cartel_1.setTextFormat(Qt.PlainText)
        self.cuerpo_cartel_1.setScaledContents(True)
        self.cuerpo_cartel_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.cuerpo_cartel_1, 4, 0, 2, 1)


        self.verticalLayout_3.addWidget(self.cartel_1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_16)

        self.verticalSpacer_18 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_18)

        self.cartel_2 = QFrame(self.Cartelera)
        self.cartel_2.setObjectName(u"cartel_2")
        self.cartel_2.setMinimumSize(QSize(0, 250))
        self.cartel_2.setStyleSheet(u"background-color:transparent;")
        self.cartel_2.setFrameShape(QFrame.StyledPanel)
        self.cartel_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.cartel_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cuerpo_cartel_2 = QLabel(self.cartel_2)
        self.cuerpo_cartel_2.setObjectName(u"cuerpo_cartel_2")
        self.cuerpo_cartel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.cuerpo_cartel_2, 1, 2, 1, 1)

        self.imagen_cartel_2 = QLabel(self.cartel_2)
        self.imagen_cartel_2.setObjectName(u"imagen_cartel_2")
        self.imagen_cartel_2.setPixmap(QPixmap(u":/Carteles/cartel2.png"))
        self.imagen_cartel_2.setScaledContents(False)

        self.gridLayout_3.addWidget(self.imagen_cartel_2, 0, 1, 2, 1)

        self.titulo_cartel_2 = QLabel(self.cartel_2)
        self.titulo_cartel_2.setObjectName(u"titulo_cartel_2")
        self.titulo_cartel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.titulo_cartel_2, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.cartel_2)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_17)

        self.cartel_3 = QFrame(self.Cartelera)
        self.cartel_3.setObjectName(u"cartel_3")
        self.cartel_3.setMinimumSize(QSize(0, 250))
        self.cartel_3.setStyleSheet(u"background-color:transparent;")
        self.cartel_3.setFrameShape(QFrame.StyledPanel)
        self.cartel_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.cartel_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.imagen_cartel_3 = QLabel(self.cartel_3)
        self.imagen_cartel_3.setObjectName(u"imagen_cartel_3")
        self.imagen_cartel_3.setPixmap(QPixmap(u":/Carteles/cartel3.png"))

        self.gridLayout_4.addWidget(self.imagen_cartel_3, 1, 1, 2, 1)

        self.cuerpo_cartel_3 = QLabel(self.cartel_3)
        self.cuerpo_cartel_3.setObjectName(u"cuerpo_cartel_3")
        self.cuerpo_cartel_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.cuerpo_cartel_3, 2, 0, 1, 1)

        self.titulo_cartel_3 = QLabel(self.cartel_3)
        self.titulo_cartel_3.setObjectName(u"titulo_cartel_3")
        self.titulo_cartel_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.titulo_cartel_3, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.cartel_3)


        self.horizontalLayout_8.addWidget(self.Cartelera)


        self.horizontalLayout_4.addWidget(self.informaciones)


        self.verticalLayout_2.addWidget(self.menudeslizante_frame)

        self.Area_1.setWidget(self.Contenido1)

        self.horizontalLayout_3.addWidget(self.Area_1)

        self.stackedWidget_principal.addWidget(self.page_1_inicio)
        self.page_inicioSesion = QWidget()
        self.page_inicioSesion.setObjectName(u"page_inicioSesion")
        self.page_inicioSesion.setStyleSheet(u"QWidget{\n"
"background-color: rgba(255, 225, 225,0);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.page_inicioSesion)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_8 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 0, 3, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(222, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_22, 1, 0, 1, 1)

        self.contenido_Inicio = QFrame(self.page_inicioSesion)
        self.contenido_Inicio.setObjectName(u"contenido_Inicio")
        self.contenido_Inicio.setMinimumSize(QSize(300, 460))
        self.contenido_Inicio.setStyleSheet(u"QFrame{\n"
"\n"
"	color: rgb(109, 70, 3);\n"
"	background-color: rgba(188, 94, 0,100);\n"
"border-radius: 18px;\n"
"\n"
"	/*background-color: rgba(168, 168, 168,70);*/\n"
"	/*background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.198864 rgba(0, 79, 129, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"\n"
"border-radius: 18px;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid  rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 15px; /* Radio de borde */\n"
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
"    font-family"
                        ": Arial, sans-serif; /* Fuente */\n"
"    color: #ffffff; /* Color del texto */\n"
"    background-color:  rgb(109, 70, 3); /* Color de fondo */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando se presiona */\n"
"QPushButton:pressed {\n"
"    background-color:  rgba(109, 70, 3,180); /* Cambio de color al presionar */\n"
"	border-radious:15 px\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QPushButton:hover {\n"
"    background-color: rgba(109, 70, 3,150); /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid rgba(109, 70, 3,150); /* Cambio de borde al pasar el cursor */\n"
"}")
        self.contenido_Inicio.setFrameShape(QFrame.StyledPanel)
        self.contenido_Inicio.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.contenido_Inicio)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Registrarse = QPushButton(self.contenido_Inicio)
        self.Registrarse.setObjectName(u"Registrarse")
        self.Registrarse.setStyleSheet(u"QPushButton#Registrarse {\n"
"    border: none; /* Sin borde */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    ; /* Color del texto */\n"
"	color:  rgb(109, 70, 3);\n"
"    background-color: transparent; /* Fondo transparente */\n"
"}\n"
"\n"
"/* Estilo para el bot\u00f3n cuando el cursor est\u00e1 encima */\n"
"QPushButton#Registrarse:hover {\n"
"     /* Cambio de color de letra al pasar el cursor */\n"
"	color: rgba(109, 70, 3,150);\n"
"}\n"
"\n"
"/* Estilo para el bot\u00f3n cuando se presiona */\n"
"QPushButton#Registrarse:pressed {\n"
"    color:  rgba(109, 70, 3,200); /* Cambio de color de letra al presionar */\n"
"}")

        self.gridLayout_9.addWidget(self.Registrarse, 8, 0, 1, 1)

        self.password_2 = QLineEdit(self.contenido_Inicio)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setMaximumSize(QSize(16777215, 32))
        self.password_2.setEchoMode(QLineEdit.Password)

        self.gridLayout_9.addWidget(self.password_2, 5, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_6)

        self.label_titulo_2 = QLabel(self.contenido_Inicio)
        self.label_titulo_2.setObjectName(u"label_titulo_2")
        self.label_titulo_2.setMinimumSize(QSize(0, 100))
        self.label_titulo_2.setMaximumSize(QSize(500, 600))
        font1 = QFont()
        font1.setFamilies([u"Lucida Console"])
        font1.setPointSize(24)
        font1.setItalic(False)
        self.label_titulo_2.setFont(font1)
        self.label_titulo_2.setStyleSheet(u"color: #000; /* Color del texto */\n"
"padding: 10px; /* Padding */\n"
"border-radius: 10px; /* Bordes redondeados */\n"
"background-color: transparent;\n"
"border-color: rgb(170, 170, 255);")
        self.label_titulo_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_titulo_2)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_21)


        self.gridLayout_9.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_correo_2 = QLabel(self.contenido_Inicio)
        self.label_correo_2.setObjectName(u"label_correo_2")
        self.label_correo_2.setMinimumSize(QSize(0, 0))
        self.label_correo_2.setMaximumSize(QSize(100, 32))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(True)
        self.label_correo_2.setFont(font2)
        self.label_correo_2.setLayoutDirection(Qt.RightToLeft)
        self.label_correo_2.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"background-color: rgb(48, 86, 148);\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid  rgb(109, 70, 3) ;/* Borde */\n"
"    border-radius: 15px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_correo_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_correo_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)


        self.gridLayout_9.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.Correo_2 = QLineEdit(self.contenido_Inicio)
        self.Correo_2.setObjectName(u"Correo_2")
        self.Correo_2.setMaximumSize(QSize(16777215, 32))

        self.gridLayout_9.addWidget(self.Correo_2, 2, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_password_2 = QLabel(self.contenido_Inicio)
        self.label_password_2.setObjectName(u"label_password_2")
        self.label_password_2.setMaximumSize(QSize(16777215, 32))
        self.label_password_2.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 15px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_password_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_password_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.gridLayout_9.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_5, 6, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(48, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.acceder_2 = QPushButton(self.contenido_Inicio)
        self.acceder_2.setObjectName(u"acceder_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.acceder_2.sizePolicy().hasHeightForWidth())
        self.acceder_2.setSizePolicy(sizePolicy1)
        self.acceder_2.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_18.addWidget(self.acceder_2)


        self.gridLayout_9.addLayout(self.horizontalLayout_18, 7, 0, 1, 1)


        self.gridLayout_6.addWidget(self.contenido_Inicio, 1, 1, 2, 3)

        self.horizontalSpacer_23 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_23, 2, 4, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_20, 3, 2, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_19, 4, 1, 1, 1)

        self.stackedWidget_principal.addWidget(self.page_inicioSesion)
        self.pageeventos = QWidget()
        self.pageeventos.setObjectName(u"pageeventos")
        self.pageeventos.setStyleSheet(u"background-color: rgb(198, 198, 198);")
        self.horizontalLayout_6 = QHBoxLayout(self.pageeventos)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.pageeventos)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"alternate-background-color: rgb(255, 162, 115);")
        self.scrollArea.setWidgetResizable(True)
        self.Area_eventos = QWidget()
        self.Area_eventos.setObjectName(u"Area_eventos")
        self.Area_eventos.setGeometry(QRect(0, 0, 837, 569))
        self.Area_eventos.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"alternate-background-color: rgb(255, 162, 115);")
        self.verticalLayout_5 = QVBoxLayout(self.Area_eventos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_12)

        self.scrollArea.setWidget(self.Area_eventos)

        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.stackedWidget_principal.addWidget(self.pageeventos)
        self.registro = QWidget()
        self.registro.setObjectName(u"registro")
        self.registro.setStyleSheet(u"QWidget{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}")
        self.gridLayout_10 = QGridLayout(self.registro)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(202, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.contenido_registro = QFrame(self.registro)
        self.contenido_registro.setObjectName(u"contenido_registro")
        self.contenido_registro.setMinimumSize(QSize(400, 300))
        self.contenido_registro.setSizeIncrement(QSize(129, 90))
        self.contenido_registro.setStyleSheet(u"QFrame{\n"
"	color: rgb(109, 70, 3);\n"
"	background-color: rgba(188, 94, 0,100);\n"
"border-radius: 18px;\n"
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
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
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
"    bac"
                        "kground-color: #2980b9; /* Cambio de color al presionar */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid #2980b9; /* Cambio de borde al pasar el cursor */\n"
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
"    border-left-width: 0px; /* Sin borde a la izquierda del bot\u00f3"
                        "n */\n"
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
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"}\n"
"")
        self.contenido_registro.setFrameShape(QFrame.StyledPanel)
        self.contenido_registro.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.contenido_registro)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_correo = QLabel(self.contenido_registro)
        self.label_correo.setObjectName(u"label_correo")
        self.label_correo.setMinimumSize(QSize(0, 0))
        self.label_correo.setMaximumSize(QSize(16777215, 16777215))
        self.label_correo.setFont(font2)
        self.label_correo.setLayoutDirection(Qt.RightToLeft)
        self.label_correo.setStyleSheet(u"")
        self.label_correo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_correo, 3, 0, 1, 1)

        self.label_correo_3 = QLabel(self.contenido_registro)
        self.label_correo_3.setObjectName(u"label_correo_3")
        self.label_correo_3.setMinimumSize(QSize(0, 0))
        self.label_correo_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_correo_3.setFont(font2)
        self.label_correo_3.setLayoutDirection(Qt.RightToLeft)
        self.label_correo_3.setStyleSheet(u"")
        self.label_correo_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_correo_3, 0, 0, 1, 1)

        self.Nombre = QLineEdit(self.contenido_registro)
        self.Nombre.setObjectName(u"Nombre")

        self.gridLayout_5.addWidget(self.Nombre, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.contenido_registro)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_5.addWidget(self.comboBox, 2, 0, 1, 1)

        self.Cedula = QLineEdit(self.contenido_registro)
        self.Cedula.setObjectName(u"Cedula")

        self.gridLayout_5.addWidget(self.Cedula, 2, 1, 1, 1)

        self.Correo = QLineEdit(self.contenido_registro)
        self.Correo.setObjectName(u"Correo")

        self.gridLayout_5.addWidget(self.Correo, 3, 1, 1, 1)

        self.label = QLabel(self.contenido_registro)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.label_password = QLabel(self.contenido_registro)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"")
        self.label_password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_password, 4, 0, 1, 1)

        self.password = QLineEdit(self.contenido_registro)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout_5.addWidget(self.password, 4, 1, 1, 1)

        self.acceder = QPushButton(self.contenido_registro)
        self.acceder.setObjectName(u"acceder")

        self.gridLayout_5.addWidget(self.acceder, 5, 1, 1, 1)

        self.Apellido = QLineEdit(self.contenido_registro)
        self.Apellido.setObjectName(u"Apellido")

        self.gridLayout_5.addWidget(self.Apellido, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.contenido_registro, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(201, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 119, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.stackedWidget_principal.addWidget(self.registro)
        self.page_perfil = QWidget()
        self.page_perfil.setObjectName(u"page_perfil")
        self.page_perfil.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.page_perfil)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.contenido_registro_2 = QFrame(self.page_perfil)
        self.contenido_registro_2.setObjectName(u"contenido_registro_2")
        self.contenido_registro_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(243, 226, 188,70);\n"
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
"    background-color: #4CAF50; /* Color de fondo */\n"
"    color: white; /* Color del texto */\n"
"    border: none; /* Sin borde */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando se presiona */\n"
"QPushButton:pressed {\n"
"   background-color: #357a38; /* Cambio de color al presionar */\n"
""
                        "}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QPushButton:hover {\n"
"background-color: #45a049;\n"
" /* Cambio de borde al pasar el cursor */\n"
"}\n"
"\n"
"/* Estilo para QComboBox */\n"
"QComboBox {\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 5px; /* Radio de borde */\n"
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
"    border-left-width: 0px; /* Sin borde a la izquierda del bot\u00f3n */\n"
"    border-top-right-radius: 5px; /* Radio de borde superior derecho */\n"
"    border-bottom-right-radius: 5px; /* Radio de borde infer"
                        "ior derecho */\n"
"    background-color: #3498db; /* Color de fondo del bot\u00f3n desplegable */\n"
"}\n"
"\n"
"/* Estilo para QComboBox cuando se despliega y se presiona */\n"
"QComboBox::down-arrow {\n"
"    width: 15px; /* Ancho del icono */\n"
"    height: 15px; /* Alto del icono */\n"
"    padding-right: 5px; /* Espaciado a la derecha del icono */\n"
"}\n"
"QToolButton {\n"
"    background-color: #4CAF50; /* Color de fondo */\n"
"    color: white; /* Color del texto */\n"
"    border: none; /* Sin borde */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #45a049; /* Cambia el color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #357a38; /* Cambia el color de fondo al hacer clic */\n"
"}\n"
"\n"
"/* Estilos para QRadioButton */\n"
"QRadioButt"
                        "on {\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Altura del indicador */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #0078D4; /* Color de fondo para el estado seleccionado */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: white; /* Color de fondo para el estado no seleccionado */\n"
"    border: 1px solid #999; /* Borde para el estado no seleccionado */\n"
"}")
        self.contenido_registro_2.setFrameShape(QFrame.StyledPanel)
        self.contenido_registro_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.contenido_registro_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_6 = QFrame(self.contenido_registro_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 180))
        self.frame_6.setStyleSheet(u"background-color:transparent;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_12 = QSpacerItem(273, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_12)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(240, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.Foto_usuario = QLabel(self.frame_9)
        self.Foto_usuario.setObjectName(u"Foto_usuario")
        self.Foto_usuario.setGeometry(QRect(0, 0, 150, 150))
        self.Foto_usuario.setMinimumSize(QSize(150, 150))
        self.Foto_usuario.setMaximumSize(QSize(150, 150))
        self.Foto_usuario.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 75px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.Foto_usuario.setPixmap(QPixmap(u":/iconos/icons8-nombre-100.png"))
        self.Foto_usuario.setScaledContents(True)
        self.Boton_CambiarFoto = QToolButton(self.frame_9)
        self.Boton_CambiarFoto.setObjectName(u"Boton_CambiarFoto")
        self.Boton_CambiarFoto.setGeometry(QRect(180, 100, 54, 40))
        self.Boton_CambiarFoto.setMinimumSize(QSize(54, 40))
        self.Boton_CambiarFoto.setStyleSheet(u"/* Estilo para QPushButton */\n"
"QToolButton {\n"
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
"QToolButton:pressed {\n"
"    background-color:  rgba(109, 70, 3,200); /* Cambio de color al presionar */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QToolButton:hover {\n"
"    background-color: rgba(109, 70, 3,150); /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid  rgba(109, 70, 3,150); /* Cambio de borde al pasar el cursor */\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/icons8-imagen-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_CambiarFoto.setIcon(icon2)
        self.Boton_CambiarFoto.setIconSize(QSize(20, 20))

        self.horizontalLayout_21.addWidget(self.frame_9)

        self.horizontalSpacer_24 = QSpacerItem(272, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_24)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.contenido_registro_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color:transparent")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_9 = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)

        self.frame_4 = QFrame(self.frame_8)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(370, 0))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    color: #2c3e50; /* Color del texto */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"}\n"
"QLabel{\n"
"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid rgb(109, 70, 3,); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"}\n"
"/* Estilo para QComboBox */\n"
"QComboBox {\n"
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px; /* Esp"
                        "aciado interno */\n"
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
"    border-left-width: 0px; /* Sin borde a la izquierda del bot\u00f3n */\n"
"    border-top-right-radius: 5px; /* Radio de borde superior derecho */\n"
"    border-bottom-right-radius: 5px; /* Radio de borde inferior derecho */\n"
"    background-color: rgb(109, 70, 3); /* Color de fondo del bot\u00f3n desplegable */\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 3, -1, -1)
        self.Boton_EditarDatos = QToolButton(self.frame_5)
        self.Boton_EditarDatos.setObjectName(u"Boton_EditarDatos")
        self.Boton_EditarDatos.setStyleSheet(u"/* Estilo para QPushButton */\n"
"QToolButton {\n"
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    color: #ffffff; /* Color del texto */\n"
"    background-color: rgb(109, 70, 3); /* Color de fondo */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando se presiona */\n"
"QToolButton:pressed {\n"
"    background-color: rgba(109, 70, 3,150); /* Cambio de color al presionar */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QToolButton:hover {\n"
"    background-color: rgba(109, 70, 3,200); /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid rgba(109, 70, 3,200); /* Cambio de borde al pasar el cursor */\n"
"}")

        self.horizontalLayout_10.addWidget(self.Boton_EditarDatos)


        self.gridLayout_7.addWidget(self.frame_5, 5, 1, 1, 1)

        self.Label_usuario = QLabel(self.frame_4)
        self.Label_usuario.setObjectName(u"Label_usuario")
        self.Label_usuario.setMinimumSize(QSize(142, 35))
        self.Label_usuario.setMaximumSize(QSize(142, 35))
        self.Label_usuario.setLayoutDirection(Qt.LeftToRight)
        self.Label_usuario.setStyleSheet(u"")
        self.Label_usuario.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.Label_usuario, 0, 0, 1, 1)

        self.label_correo_4 = QLabel(self.frame_4)
        self.label_correo_4.setObjectName(u"label_correo_4")
        self.label_correo_4.setMinimumSize(QSize(142, 35))
        self.label_correo_4.setMaximumSize(QSize(142, 35))
        self.label_correo_4.setFont(font2)
        self.label_correo_4.setLayoutDirection(Qt.LeftToRight)
        self.label_correo_4.setStyleSheet(u"")
        self.label_correo_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_correo_4, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(142, 35))
        self.label_2.setMaximumSize(QSize(142, 35))
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_2, 2, 0, 1, 1)

        self.perfil_nombre = QLineEdit(self.frame_4)
        self.perfil_nombre.setObjectName(u"perfil_nombre")
        self.perfil_nombre.setReadOnly(True)

        self.gridLayout_7.addWidget(self.perfil_nombre, 1, 1, 1, 1)

        self.perfil_cedula = QLineEdit(self.frame_4)
        self.perfil_cedula.setObjectName(u"perfil_cedula")
        self.perfil_cedula.setReadOnly(True)

        self.gridLayout_7.addWidget(self.perfil_cedula, 3, 1, 1, 1)

        self.label_correo_5 = QLabel(self.frame_4)
        self.label_correo_5.setObjectName(u"label_correo_5")
        self.label_correo_5.setMinimumSize(QSize(142, 35))
        self.label_correo_5.setMaximumSize(QSize(142, 35))
        self.label_correo_5.setFont(font2)
        self.label_correo_5.setLayoutDirection(Qt.RightToLeft)
        self.label_correo_5.setStyleSheet(u"")
        self.label_correo_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_correo_5, 4, 0, 1, 1)

        self.perfil_correo = QLineEdit(self.frame_4)
        self.perfil_correo.setObjectName(u"perfil_correo")
        self.perfil_correo.setReadOnly(True)

        self.gridLayout_7.addWidget(self.perfil_correo, 4, 1, 1, 1)

        self.perfil_apellido = QLineEdit(self.frame_4)
        self.perfil_apellido.setObjectName(u"perfil_apellido")
        self.perfil_apellido.setReadOnly(True)

        self.gridLayout_7.addWidget(self.perfil_apellido, 2, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(142, 35))
        self.comboBox_2.setMaximumSize(QSize(142, 35))
        self.comboBox_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_7.addWidget(self.comboBox_2, 3, 0, 1, 1)

        self.Line_tipoUsuario = QLineEdit(self.frame_4)
        self.Line_tipoUsuario.setObjectName(u"Line_tipoUsuario")
        self.Line_tipoUsuario.setReadOnly(True)

        self.gridLayout_7.addWidget(self.Line_tipoUsuario, 0, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_4)

        self.horizontalSpacer_10 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.contenido_registro_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"}\n"
"/* Estilo para QPushButton */\n"
"QPushButton {\n"
"    border: 2px solid rgb(109, 70, 3); /* Borde */\n"
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
"    background-color: #2980b9; /* Cambio de color al presionar */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid #2980b9; /* Cambio de borde al pasar el cursor */\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.Boto_cerrarsesion = QPushButton(self.frame_7)
        self.Boto_cerrarsesion.setObjectName(u"Boto_cerrarsesion")
        self.Boto_cerrarsesion.setStyleSheet(u"/* Estilo para QPushButton */\n"
"QToolButton {\n"
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
"QToolButton:pressed {\n"
"    background-color:  rgba(109, 70, 3,200); /* Cambio de color al presionar */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QToolButton:hover {\n"
"    background-color: rgba(109, 70, 3,150); /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid  rgba(109, 70, 3,150); /* Cambio de borde al pasar el cursor */\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/icons8-salida-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boto_cerrarsesion.setIcon(icon3)
        self.Boto_cerrarsesion.setIconSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.Boto_cerrarsesion)

        self.Boton_cambiarContra = QToolButton(self.frame_7)
        self.Boton_cambiarContra.setObjectName(u"Boton_cambiarContra")
        self.Boton_cambiarContra.setStyleSheet(u"/* Estilo para QPushButton */\n"
"QToolButton {\n"
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
"QToolButton:pressed {\n"
"    background-color:  rgba(109, 70, 3,200); /* Cambio de color al presionar */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QToolButton:hover {\n"
"    background-color: rgba(109, 70, 3,150); /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid  rgba(109, 70, 3,150); /* Cambio de borde al pasar el cursor */\n"
"}")

        self.horizontalLayout_19.addWidget(self.Boton_cambiarContra)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)


        self.verticalLayout_9.addWidget(self.frame_7)


        self.horizontalLayout_7.addWidget(self.contenido_registro_2)

        self.stackedWidget_principal.addWidget(self.page_perfil)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.page_admin.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.page_admin)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_admin)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(280, 16777215))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(12, 26, 27,40);\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(178, 121, 36);/* Color de fondo */\n"
"    font-weight: 400;\n"
"    color: #000; /* Color del texto */\n"
"    border: 1px solid transparent;\n"
"    padding: 9px 18px; /* Padding */\n"
"    font-size: 10px; /* Tama\u00f1o de la fuente */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #fff; /* Color del texto al pasar el cursor */\n"
"    background-color: rgba(178, 121, 36,80); /* Cambiar el color de fondo al pasar el mouse */\n"
"    border-color:rgba(178, 121, 36,80);/* Cambiar el color del borde al pasar el mouse */\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 3, 0, 0)
        self.Boton_adminUsuarios = QPushButton(self.frame_2)
        self.Boton_adminUsuarios.setObjectName(u"Boton_adminUsuarios")
        self.Boton_adminUsuarios.setMinimumSize(QSize(0, 50))
        self.Boton_adminUsuarios.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.Boton_adminUsuarios)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.Boton_adminEventos = QPushButton(self.frame_2)
        self.Boton_adminEventos.setObjectName(u"Boton_adminEventos")
        self.Boton_adminEventos.setMinimumSize(QSize(0, 50))
        self.Boton_adminEventos.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.Boton_adminEventos)

        self.botonAdmEvento = QFrame(self.frame_2)
        self.botonAdmEvento.setObjectName(u"botonAdmEvento")
        self.botonAdmEvento.setFrameShape(QFrame.HLine)
        self.botonAdmEvento.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.botonAdmEvento)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.line_6 = QFrame(self.frame_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_6)


        self.horizontalLayout_12.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_admin)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(243, 221, 171,70);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_admin = QStackedWidget(self.frame_3)
        self.stackedWidget_admin.setObjectName(u"stackedWidget_admin")
        sizePolicy.setHeightForWidth(self.stackedWidget_admin.sizePolicy().hasHeightForWidth())
        self.stackedWidget_admin.setSizePolicy(sizePolicy)
        self.stackedWidget_admin.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QFrame{\n"
"background-color: rgba(243, 226, 188,70);\n"
"}\n"
" QPushButton {\n"
"			background-color: rgb(178, 121, 36);;/* Color de fondo */\n"
"            border-style: outset; /* Estilo del borde (puede ser outset, inset, solid, dashed, dotted, none) */\n"
"            border-width: 2px; /* Ancho del borde */\n"
"            border-color: rgb(232, 232, 200); /* Color del borde */\n"
"            border-radius: 8px; /* Radio de borde */\n"
"            padding: 6px; /* Espaciado interno */\n"
"            color: black; /* Color del texto */\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color: rgba(178, 121, 36,150); /* Cambio de color de fondo al pasar el mouse */\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:color: rgba(178, 121, 36,70);/* Cambio de color de fondo al presionar el bot\u00f3n */\n"
"	\n"
"        }\n"
"QDateEdit{\n"
"background-color: rgb(236, 240, 241);\n"
"}\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_11)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(13)
        self.verticalSpacer_13 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_13, 2, 1, 1, 1)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)

        self.combo_coordinadores = QComboBox(self.page)
        self.combo_coordinadores.setObjectName(u"combo_coordinadores")
        self.combo_coordinadores.setMinimumSize(QSize(0, 30))
        self.combo_coordinadores.setStyleSheet(u"/* Estilo para QComboBox */\n"
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
"    border-left-width: 0px; /* Sin borde a la izquierda del bot\u00f3n */\n"
"    border-top-right-radius: 5px; /* Radio de borde superior derecho */\n"
"    border-bottom-right-radius: 5px; /* Radio de borde inferior derecho */\n"
"    background-color: rgb(109, 70, 3); /* Color de fondo del bot\u00f3n desplegable */\n"
"}")

        self.gridLayout_8.addWidget(self.combo_coordinadores, 3, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(30, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_14, 7, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 1, 3, 1, 1)

        self.tituloEvento = QLineEdit(self.page)
        self.tituloEvento.setObjectName(u"tituloEvento")
        self.tituloEvento.setMinimumSize(QSize(0, 30))
        self.tituloEvento.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(109, 70, 3); /* Borde */\n"
"    border-radius: 13px; /* Radio de borde */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    color: #2c3e50; /* Color del texto */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"}")

        self.gridLayout_8.addWidget(self.tituloEvento, 1, 1, 1, 1)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_8.addWidget(self.label_6, 3, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_18 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)

        self.label_15 = QLabel(self.page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color:transparent;")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.fechaEvento = QDateEdit(self.page)
        self.fechaEvento.setObjectName(u"fechaEvento")
        self.fechaEvento.setMinimumSize(QSize(150, 30))
        self.fechaEvento.setMaximumSize(QSize(250, 16777215))
        self.fechaEvento.setStyleSheet(u"QDateEdit{\n"
"background-color: rgb(236, 240, 241);\n"
"border:2px solid #a77c32;\n"
"border-radius:13px;\n"
"width:13px;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"	image: url(:/iconos/calendario.jpg);  /* Cambia esto a la ruta de tu imagen */\n"
"    width: 25px; /* Ajusta el ancho seg\u00fan sea necesario */\n"
"    height: 25px; /* Ajusta la altura seg\u00fan sea necesario */\n"
"}")

        self.horizontalLayout_13.addWidget(self.fechaEvento)

        self.horizontalSpacer_16 = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.label_16 = QLabel(self.page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color:transparent;")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.inicioEvento = QTimeEdit(self.page)
        self.inicioEvento.setObjectName(u"inicioEvento")
        self.inicioEvento.setMinimumSize(QSize(80, 30))
        self.inicioEvento.setMaximumSize(QSize(200, 16777215))
        self.inicioEvento.setStyleSheet(u"QTimeEdit{\n"
"background-color: rgb(236, 240, 241);\n"
"border:2px solid #a77c32;\n"
"border-radius:13px;\n"
"width:13px;\n"
"}\n"
"QTimeEdit::down-button {\n"
"	border-radius:3px;/* Cambia esto a la ruta de tu imagen */\n"
"	background-color: rgb(109, 70, 3);\n"
"    width: 25px; /* Ajusta el ancho seg\u00fan sea necesario */\n"
"    height: 12px; /* Ajusta la altura seg\u00fan sea necesario */\n"
"}\n"
"QTimeEdit::up-button {\n"
"	border-radius:3px;/* Cambia esto a la ruta de tu imagen */\n"
"	background-color: rgb(109, 70, 3);\n"
"    width: 25px; /* Ajusta el ancho seg\u00fan sea necesario */\n"
"    height: 12px; /* Ajusta la altura seg\u00fan sea necesario */\n"
"}")

        self.horizontalLayout_13.addWidget(self.inicioEvento)

        self.horizontalSpacer_17 = QSpacerItem(80, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_19 = QSpacerItem(350, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)

        self.label_26 = QLabel(self.page)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"background-color:transparent;")

        self.horizontalLayout_16.addWidget(self.label_26)

        self.finEvento = QTimeEdit(self.page)
        self.finEvento.setObjectName(u"finEvento")
        self.finEvento.setMinimumSize(QSize(80, 30))
        self.finEvento.setMaximumSize(QSize(200, 16777215))
        self.finEvento.setStyleSheet(u"QTimeEdit{\n"
"background-color: rgb(236, 240, 241);\n"
"border:2px solid #a77c32;\n"
"border-radius:13px;\n"
"width:13px;\n"
"}\n"
"QTimeEdit::down-button {\n"
"	border-radius:3px;/* Cambia esto a la ruta de tu imagen */\n"
"	background-color: rgb(109, 70, 3);\n"
"    width: 25px; /* Ajusta el ancho seg\u00fan sea necesario */\n"
"    height: 12px; /* Ajusta la altura seg\u00fan sea necesario */\n"
"}\n"
"QTimeEdit::up-button {\n"
"	border-radius:3px;/* Cambia esto a la ruta de tu imagen */\n"
"	background-color: rgb(109, 70, 3);\n"
"    width: 25px; /* Ajusta el ancho seg\u00fan sea necesario */\n"
"    height: 12px; /* Ajusta la altura seg\u00fan sea necesario */\n"
"}")

        self.horizontalLayout_16.addWidget(self.finEvento)

        self.horizontalSpacer_20 = QSpacerItem(80, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_20)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_121 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_121)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_8.addWidget(self.label_5)

        self.descripcionEvento = QPlainTextEdit(self.page)
        self.descripcionEvento.setObjectName(u"descripcionEvento")
        self.descripcionEvento.setMinimumSize(QSize(0, 90))
        self.descripcionEvento.setMaximumSize(QSize(660, 90))
        self.descripcionEvento.setStyleSheet(u"QPlainTextEdit {\n"
"            border-style: outset; /* Estilo del borde (puede ser outset, inset, solid, dashed, dotted, none) */\n"
"            border-width: 1px; /* Ancho del borde */\n"
"            border-color: rgb(0,0,0); /* Color del borde */\n"
"            border-radius: 8px; /* Radio de borde */\n"
"            padding: 6px; /* Espaciado interno */\n"
"            color: black; /* Color del texto */\n"
"        }")

        self.verticalLayout_8.addWidget(self.descripcionEvento)

        self.verticalSpacer_15 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_14 = QSpacerItem(260, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)

        self.Boton_guardarEvento = QPushButton(self.page)
        self.Boton_guardarEvento.setObjectName(u"Boton_guardarEvento")
        self.Boton_guardarEvento.setMinimumSize(QSize(130, 30))
        self.Boton_guardarEvento.setMaximumSize(QSize(180, 40))
        self.Boton_guardarEvento.setSizeIncrement(QSize(0, 0))
        self.Boton_guardarEvento.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.Boton_guardarEvento)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.stackedWidget_admin.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_11 = QGridLayout(self.page_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setVerticalSpacing(9)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 9)
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_11)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.DiagCrossPattern)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 471, 251))
        self.tableWidget.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_11.addWidget(self.frame_11, 0, 0, 1, 1)

        self.stackedWidget_admin.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.stackedWidget_admin)


        self.horizontalLayout_12.addWidget(self.frame_3)

        self.stackedWidget_principal.addWidget(self.page_admin)

        self.horizontalLayout_2.addWidget(self.stackedWidget_principal)


        self.verticalLayout.addWidget(self.contenido)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_principal.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Boton_inicio.setText("")
        self.Boton_ingresar.setText(QCoreApplication.translate("MainWindow", u"INICIAR SESION\n"
"           O\n"
"  REGISTRARSE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Horarios", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"pueden cambiar sin previo aviso. ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Domingo: Cerrado", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Martes - S\u00e1bado: 10:00 a. m. - 5:00 p. m.", None))
        self.label_9.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Contacto", None))
        self.label_24.setText("")
        self.label_23.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lunes: Cerrado", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"601 343 2222", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Cra. 6 #15-88", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"wmuseo@banrep.gov.co", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ten en cuenta que nuestros horarios", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.Bonton_proxEvento.setText(QCoreApplication.translate("MainWindow", u"Proximos eventos", None))
        self.Boton_objetos.setText(QCoreApplication.translate("MainWindow", u"Objetos del museo", None))
        self.titulo_cartel_1.setText(QCoreApplication.translate("MainWindow", u"Programa tu visita al museo", None))
        self.imagen_cartel_1.setText("")
        self.cuerpo_cartel_1.setText(QCoreApplication.translate("MainWindow", u"El Museo del Oro del Banco de la Rep\u00fablica \n"
"preserva colecciones arqueol\u00f3gicas \n"
"que son un patrimonio y un orgullo de \n"
"todos los colombianos.", None))
        self.cuerpo_cartel_2.setText(QCoreApplication.translate("MainWindow", u"\u00bfCoronas de plumas, \n"
"maguar\u00e9s, trajes de corteza \n"
"de \u00e1rbol para las celebraciones \n"
"de enmascarados?", None))
        self.imagen_cartel_2.setText("")
        self.titulo_cartel_2.setText(QCoreApplication.translate("MainWindow", u"Palabras de vida", None))
        self.imagen_cartel_3.setText("")
        self.cuerpo_cartel_3.setText(QCoreApplication.translate("MainWindow", u"Materiales did\u00e1cticos, ll\u00fadicos e interactivos \n"
"de pr\u00e9stamo gratuito sobre el patrimonio y \n"
"la identidad cultural, la diversidad y la convivencia.", None))
        self.titulo_cartel_3.setText(QCoreApplication.translate("MainWindow", u"Maletas didacticas \n"
"del museo de oro", None))
        self.Registrarse.setText(QCoreApplication.translate("MainWindow", u"\u00bfNo tienes una cuenta?", None))
        self.password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"************", None))
        self.label_titulo_2.setText(QCoreApplication.translate("MainWindow", u"INICIO DE SESION", None))
        self.label_correo_2.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.Correo_2.setInputMask("")
        self.Correo_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@email.com", None))
        self.label_password_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.acceder_2.setText(QCoreApplication.translate("MainWindow", u"ACCEDER", None))
        self.label_correo.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.label_correo_3.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.Nombre.setInputMask("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CC", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CE", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"RC", None))

        self.Cedula.setInputMask("")
        self.Cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123456789", None))
        self.Correo.setInputMask("")
        self.Correo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@email.com", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"************", None))
        self.acceder.setText(QCoreApplication.translate("MainWindow", u"CREAR CUENTA", None))
        self.Apellido.setInputMask("")
        self.Apellido.setText("")
        self.Boton_CambiarFoto.setText(QCoreApplication.translate("MainWindow", u"Cambiar imagen", None))
        self.Boton_EditarDatos.setText(QCoreApplication.translate("MainWindow", u"Editar Datos", None))
        self.Label_usuario.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.label_correo_4.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.perfil_nombre.setInputMask("")
        self.perfil_cedula.setInputMask("")
        self.label_correo_5.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.perfil_correo.setInputMask("")
        self.perfil_apellido.setInputMask("")
        self.perfil_apellido.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"CC", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"CE", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"RC", None))

        self.Boto_cerrarsesion.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESION", None))
#if QT_CONFIG(shortcut)
        self.Boto_cerrarsesion.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.Boton_cambiarContra.setText(QCoreApplication.translate("MainWindow", u"Cambiar Contase\u00f1a", None))
        self.Boton_adminUsuarios.setText(QCoreApplication.translate("MainWindow", u"ADMINISTAR USUARIOS", None))
        self.Boton_adminEventos.setText(QCoreApplication.translate("MainWindow", u"ADMINISTAR EVENTOS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">T\u00edtulo del evento:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Encargado del evento:</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Fecha:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hora inicio:</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Finalizaci\u00f3n:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Descripci\u00f3n:</span></p></body></html>", None))
        self.Boton_guardarEvento.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

