# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(803, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Frame_menu = QFrame(self.centralwidget)
        self.Frame_menu.setObjectName(u"Frame_menu")
        self.Frame_menu.setMinimumSize(QSize(0, 0))
        self.Frame_menu.setMaximumSize(QSize(16777215, 76))
        self.Frame_menu.setStyleSheet(u"QFrame#Frame_menu{\n"
"background-color: rgb(65, 182, 255);\n"
"border-radius:2px\n"
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
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 5, -1, 1)
        self.Boton_inicio = QPushButton(self.Frame_menu)
        self.Boton_inicio.setObjectName(u"Boton_inicio")
        self.Boton_inicio.setMaximumSize(QSize(75, 52))
        self.Boton_inicio.setStyleSheet(u"QPushButton#Boton_inicio {\n"
"    font-weight: 400;\n"
"    color: #000; /* Color del texto */\n"
"    background-color: rgb(255, 255, 255); /* Color de fondo */\n"
"    border: 1px solid transparent;\n"
"    padding: 9px 18px; /* Padding */\n"
"    font-size: 8px; /* Tama\u00f1o de la fuente */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"}\n"
"\n"
"QPushButton#Boton_inicio:hover {\n"
"    color: #fff; /* Color del texto al pasar el cursor */\n"
"    background-color: rgb(150, 150, 150); /* Color de fondo al pasar el cursor */\n"
"    border-color: #0062cc; /* Color del borde al pasar el cursor */\n"
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
"    font-weight: 400;\n"
"    color: #000; /* Color del texto */\n"
"    background-color: rgb(217, 217, 217); /* Color de fondo */\n"
"    border: 1px solid transparent;\n"
"    padding: 9px 18px; /* Padding */\n"
"    font-size: 10px; /* Tama\u00f1o de la fuente */\n"
"    border-radius: 20px; /* Bordes redondeados */\n"
"}\n"
"\n"
"QPushButton#Boton_ingresar:hover {\n"
"    color: #fff; /* Color del texto al pasar el cursor */\n"
"    background-color: rgb(150, 150, 150); /* Color de fondo al pasar el cursor */\n"
"    border-color: #0062cc; /* Color del borde al pasar el cursor */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/icons8-usuario-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_ingresar.setIcon(icon1)
        self.Boton_ingresar.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.Boton_ingresar)


        self.verticalLayout.addWidget(self.Frame_menu)

        self.contenido = QFrame(self.centralwidget)
        self.contenido.setObjectName(u"contenido")
        self.contenido.setFrameShape(QFrame.StyledPanel)
        self.contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contenido)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_principal = QStackedWidget(self.contenido)
        self.stackedWidget_principal.setObjectName(u"stackedWidget_principal")
        self.stackedWidget_principal.setStyleSheet(u"background-color: rgb(198, 198, 198);")
        self.page_1_inicio = QWidget()
        self.page_1_inicio.setObjectName(u"page_1_inicio")
        self.horizontalLayout_3 = QHBoxLayout(self.page_1_inicio)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.Area_1 = QScrollArea(self.page_1_inicio)
        self.Area_1.setObjectName(u"Area_1")
        self.Area_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Area_1.setWidgetResizable(True)
        self.Contenido1 = QWidget()
        self.Contenido1.setObjectName(u"Contenido1")
        self.Contenido1.setGeometry(QRect(0, 0, 1275, 1055))
        self.verticalLayout_2 = QVBoxLayout(self.Contenido1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menudeslizante_frame = QFrame(self.Contenido1)
        self.menudeslizante_frame.setObjectName(u"menudeslizante_frame")
        self.menudeslizante_frame.setMaximumSize(QSize(16777215, 16777215))
        self.menudeslizante_frame.setFrameShape(QFrame.StyledPanel)
        self.menudeslizante_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menudeslizante_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.menuDeslizante = QStackedWidget(self.menudeslizante_frame)
        self.menuDeslizante.setObjectName(u"menuDeslizante")
        self.deslizante_1 = QWidget()
        self.deslizante_1.setObjectName(u"deslizante_1")
        self.verticalLayout_4 = QVBoxLayout(self.deslizante_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.imagen_4 = QLabel(self.deslizante_1)
        self.imagen_4.setObjectName(u"imagen_4")
        self.imagen_4.setMinimumSize(QSize(0, 164))
        self.imagen_4.setPixmap(QPixmap(u":/iconos/banner1.png"))
        self.imagen_4.setScaledContents(True)
        self.imagen_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.imagen_4)

        self.frame_botonesevento = QFrame(self.deslizante_1)
        self.frame_botonesevento.setObjectName(u"frame_botonesevento")
        self.frame_botonesevento.setMinimumSize(QSize(0, 50))
        self.frame_botonesevento.setFrameShape(QFrame.StyledPanel)
        self.frame_botonesevento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_botonesevento)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.Bonton_proxEvento = QPushButton(self.frame_botonesevento)
        self.Bonton_proxEvento.setObjectName(u"Bonton_proxEvento")
        self.Bonton_proxEvento.setMinimumSize(QSize(180, 40))
        self.Bonton_proxEvento.setMaximumSize(QSize(180, 60))
        self.Bonton_proxEvento.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50; /* Color de fondo */\n"
"    color: white; /* Color del texto */\n"
"    border-style: solid; /* Estilo del borde */\n"
"    border-width: 2px; /* Ancho del borde */\n"
"    border-color: #4CAF50; /* Color del borde */\n"
"    border-radius: 5px; /* Radio de borde para esquinas redondeadas */\n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Peso de la fuente */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Cambiar el color de fondo al pasar el mouse */\n"
"    border-color: #45a049; /* Cambiar el color del borde al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #357a38; /* Cambiar el color de fondo al hacer clic */\n"
"    border-color: #357a38; /* Cambiar el color del borde al hacer clic */\n"
"}")

        self.horizontalLayout_5.addWidget(self.Bonton_proxEvento, 0, Qt.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.Boton_objetos = QPushButton(self.frame_botonesevento)
        self.Boton_objetos.setObjectName(u"Boton_objetos")
        self.Boton_objetos.setMinimumSize(QSize(180, 40))
        self.Boton_objetos.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50; /* Color de fondo */\n"
"    color: white; /* Color del texto */\n"
"    border-style: solid; /* Estilo del borde */\n"
"    border-width: 2px; /* Ancho del borde */\n"
"    border-color: #4CAF50; /* Color del borde */\n"
"    border-radius: 5px; /* Radio de borde para esquinas redondeadas */\n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Peso de la fuente */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Cambiar el color de fondo al pasar el mouse */\n"
"    border-color: #45a049; /* Cambiar el color del borde al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #357a38; /* Cambiar el color de fondo al hacer clic */\n"
"    border-color: #357a38; /* Cambiar el color del borde al hacer clic */\n"
"}")

        self.horizontalLayout_5.addWidget(self.Boton_objetos, 0, Qt.AlignRight)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)


        self.verticalLayout_4.addWidget(self.frame_botonesevento)

        self.menuDeslizante.addWidget(self.deslizante_1)

        self.horizontalLayout_4.addWidget(self.menuDeslizante)


        self.verticalLayout_2.addWidget(self.menudeslizante_frame)

        self.informaciones = QFrame(self.Contenido1)
        self.informaciones.setObjectName(u"informaciones")
        self.informaciones.setStyleSheet(u"QFrame#informaciones{\n"
"background-color: rgb(241, 241, 241);\n"
"alternate-background-color: rgb(255, 162, 115);\n"
"}")
        self.informaciones.setFrameShape(QFrame.StyledPanel)
        self.informaciones.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.informaciones)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(15, 8, 5, 5)
        self.frame = QFrame(self.informaciones)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"border-radius: 8px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.general = QFrame(self.frame)
        self.general.setObjectName(u"general")
        self.general.setMaximumSize(QSize(300, 377))
        self.general.setStyleSheet(u"QFrame#general{\n"
"background-color: rgb(0, 85, 127);\n"
"}\n"
"")
        self.general.setFrameShape(QFrame.StyledPanel)
        self.general.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.general)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.general)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 50))
        self.label_9.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setPixmap(QPixmap(u":/iconos/icons8-reloj-96.png"))
        self.label_9.setScaledContents(True)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.general)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)

        self.label_24 = QLabel(self.general)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(45, 45))
        self.label_24.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_24.setTextFormat(Qt.AutoText)
        self.label_24.setPixmap(QPixmap(u":/iconos/icons8-mail-50.png"))
        self.label_24.setScaledContents(True)

        self.gridLayout.addWidget(self.label_24, 9, 0, 1, 1)

        self.label_11 = QLabel(self.general)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)

        self.label_12 = QLabel(self.general)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_12, 5, 1, 1, 1)

        self.label_14 = QLabel(self.general)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_14, 6, 1, 1, 1)

        self.label_13 = QLabel(self.general)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_13, 7, 1, 1, 1)

        self.label_8 = QLabel(self.general)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_19 = QLabel(self.general)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_19, 12, 1, 1, 1)

        self.label_21 = QLabel(self.general)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_21, 10, 1, 1, 1)

        self.label_23 = QLabel(self.general)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_23, 8, 1, 1, 1)

        self.label_20 = QLabel(self.general)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_20, 11, 1, 1, 1)

        self.label_22 = QLabel(self.general)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_22, 9, 1, 1, 1)

        self.label_18 = QLabel(self.general)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"QLabel{\n"
"font: 15pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_18, 13, 1, 1, 1)

        self.label_17 = QLabel(self.general)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLabel{\n"
"font: 10pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 85, 127);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_17, 14, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.general)


        self.horizontalLayout_8.addWidget(self.frame)

        self.Cartelera = QFrame(self.informaciones)
        self.Cartelera.setObjectName(u"Cartelera")
        self.Cartelera.setMaximumSize(QSize(16777215, 16777215))
        self.Cartelera.setStyleSheet(u"QFrame#Cartelera{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QFrame#titulo_cartel_1,#titulo_cartel_2,#titulo_cartel_3{\n"
"font: 75 18pt \"MS Serif\";\n"
"\n"
"}\n"
"QFrame#cuerpo_cartel_1,#cuerpo_cartel_2,#cuerpo_cartel_3{\n"
"font: italic 12pt \"Sitka\";\n"
"\n"
"}")
        self.Cartelera.setFrameShape(QFrame.StyledPanel)
        self.Cartelera.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Cartelera)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cartel_1 = QFrame(self.Cartelera)
        self.cartel_1.setObjectName(u"cartel_1")
        self.cartel_1.setMinimumSize(QSize(0, 250))
        self.cartel_1.setMaximumSize(QSize(16777215, 16777215))
        self.cartel_1.setFrameShape(QFrame.StyledPanel)
        self.cartel_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.cartel_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.titulo_cartel_1 = QLabel(self.cartel_1)
        self.titulo_cartel_1.setObjectName(u"titulo_cartel_1")
        self.titulo_cartel_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.titulo_cartel_1, 0, 0, 1, 1)

        self.imagen_cartel_1 = QLabel(self.cartel_1)
        self.imagen_cartel_1.setObjectName(u"imagen_cartel_1")
        self.imagen_cartel_1.setTextFormat(Qt.RichText)
        self.imagen_cartel_1.setPixmap(QPixmap(u":/Carteles/cartel1.png"))
        self.imagen_cartel_1.setScaledContents(True)
        self.imagen_cartel_1.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.imagen_cartel_1.setWordWrap(False)

        self.gridLayout_2.addWidget(self.imagen_cartel_1, 0, 1, 3, 1)

        self.cuerpo_cartel_1 = QLabel(self.cartel_1)
        self.cuerpo_cartel_1.setObjectName(u"cuerpo_cartel_1")
        self.cuerpo_cartel_1.setMinimumSize(QSize(300, 0))
        self.cuerpo_cartel_1.setTextFormat(Qt.PlainText)
        self.cuerpo_cartel_1.setScaledContents(True)
        self.cuerpo_cartel_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.cuerpo_cartel_1, 1, 0, 2, 1)


        self.verticalLayout_3.addWidget(self.cartel_1)

        self.line = QFrame(self.Cartelera)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.cartel_2 = QFrame(self.Cartelera)
        self.cartel_2.setObjectName(u"cartel_2")
        self.cartel_2.setMinimumSize(QSize(0, 250))
        self.cartel_2.setFrameShape(QFrame.StyledPanel)
        self.cartel_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.cartel_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.imagen_cartel_2 = QLabel(self.cartel_2)
        self.imagen_cartel_2.setObjectName(u"imagen_cartel_2")
        self.imagen_cartel_2.setPixmap(QPixmap(u":/Carteles/cartel2.png"))
        self.imagen_cartel_2.setScaledContents(False)

        self.gridLayout_3.addWidget(self.imagen_cartel_2, 0, 1, 2, 1)

        self.titulo_cartel_2 = QLabel(self.cartel_2)
        self.titulo_cartel_2.setObjectName(u"titulo_cartel_2")
        self.titulo_cartel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.titulo_cartel_2, 0, 2, 1, 1)

        self.cuerpo_cartel_2 = QLabel(self.cartel_2)
        self.cuerpo_cartel_2.setObjectName(u"cuerpo_cartel_2")
        self.cuerpo_cartel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.cuerpo_cartel_2, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.cartel_2)

        self.line_2 = QFrame(self.Cartelera)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.cartel_3 = QFrame(self.Cartelera)
        self.cartel_3.setObjectName(u"cartel_3")
        self.cartel_3.setMinimumSize(QSize(0, 250))
        self.cartel_3.setFrameShape(QFrame.StyledPanel)
        self.cartel_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.cartel_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.titulo_cartel_3 = QLabel(self.cartel_3)
        self.titulo_cartel_3.setObjectName(u"titulo_cartel_3")
        self.titulo_cartel_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.titulo_cartel_3, 1, 0, 1, 1)

        self.cuerpo_cartel_3 = QLabel(self.cartel_3)
        self.cuerpo_cartel_3.setObjectName(u"cuerpo_cartel_3")
        self.cuerpo_cartel_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.cuerpo_cartel_3, 2, 0, 1, 1)

        self.imagen_cartel_3 = QLabel(self.cartel_3)
        self.imagen_cartel_3.setObjectName(u"imagen_cartel_3")
        self.imagen_cartel_3.setPixmap(QPixmap(u":/Carteles/cartel3.png"))

        self.gridLayout_4.addWidget(self.imagen_cartel_3, 1, 1, 2, 1)


        self.verticalLayout_3.addWidget(self.cartel_3)


        self.horizontalLayout_8.addWidget(self.Cartelera)


        self.verticalLayout_2.addWidget(self.informaciones)

        self.Area_1.setWidget(self.Contenido1)

        self.horizontalLayout_3.addWidget(self.Area_1)

        self.stackedWidget_principal.addWidget(self.page_1_inicio)
        self.page_inicioSesion = QWidget()
        self.page_inicioSesion.setObjectName(u"page_inicioSesion")
        self.page_inicioSesion.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.page_inicioSesion)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.contenido_Inicio = QFrame(self.page_inicioSesion)
        self.contenido_Inicio.setObjectName(u"contenido_Inicio")
        self.contenido_Inicio.setStyleSheet(u"QFrame{\n"
"background-color: rgba(173, 216, 230, 0.5);\n"
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
"    background-color: #2980b9; /* Cambio de color al presiona"
                        "r */\n"
"}\n"
"\n"
"/* Estilo para QPushButton cuando el cursor est\u00e1 encima */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Cambio de color al pasar el cursor */\n"
"    border: 2px solid #2980b9; /* Cambio de borde al pasar el cursor */\n"
"}")
        self.contenido_Inicio.setFrameShape(QFrame.StyledPanel)
        self.contenido_Inicio.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.contenido_Inicio)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Correo_2 = QLineEdit(self.contenido_Inicio)
        self.Correo_2.setObjectName(u"Correo_2")

        self.gridLayout_6.addWidget(self.Correo_2, 3, 2, 1, 1)

        self.label_titulo_2 = QLabel(self.contenido_Inicio)
        self.label_titulo_2.setObjectName(u"label_titulo_2")
        self.label_titulo_2.setMinimumSize(QSize(500, 100))
        self.label_titulo_2.setMaximumSize(QSize(500, 600))
        font1 = QFont()
        font1.setFamilies([u"Lucida Console"])
        font1.setPointSize(24)
        font1.setItalic(False)
        self.label_titulo_2.setFont(font1)
        self.label_titulo_2.setStyleSheet(u"	color: #000; /* Color del texto */\n"
"    padding: 10px; /* Padding */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"background-color: rgba(144, 238, 144, 0.5);\n"
"border-color: rgb(170, 170, 255);")
        self.label_titulo_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_titulo_2, 1, 2, 1, 1, Qt.AlignHCenter)

        self.acceder_2 = QPushButton(self.contenido_Inicio)
        self.acceder_2.setObjectName(u"acceder_2")

        self.gridLayout_6.addWidget(self.acceder_2, 6, 2, 1, 1)

        self.label_password_2 = QLabel(self.contenido_Inicio)
        self.label_password_2.setObjectName(u"label_password_2")
        self.label_password_2.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_password_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_password_2, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 5, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 3, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 0, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 8, 2, 1, 1)

        self.password_2 = QLineEdit(self.contenido_Inicio)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setEchoMode(QLineEdit.Password)

        self.gridLayout_6.addWidget(self.password_2, 4, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 2, 2, 1, 1)

        self.label_correo_2 = QLabel(self.contenido_Inicio)
        self.label_correo_2.setObjectName(u"label_correo_2")
        self.label_correo_2.setMinimumSize(QSize(142, 0))
        self.label_correo_2.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Arial,sans-serif"])
        font2.setBold(True)
        self.label_correo_2.setFont(font2)
        self.label_correo_2.setLayoutDirection(Qt.RightToLeft)
        self.label_correo_2.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_correo_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_correo_2, 3, 1, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 3, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 4, 3, 1, 1)

        self.Registrarse = QPushButton(self.contenido_Inicio)
        self.Registrarse.setObjectName(u"Registrarse")
        self.Registrarse.setStyleSheet(u"QPushButton#Registrarse {\n"
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

        self.gridLayout_6.addWidget(self.Registrarse, 7, 2, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_11.addWidget(self.contenido_Inicio)

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
        self.Area_eventos.setGeometry(QRect(0, 0, 98, 28))
        self.Area_eventos.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"alternate-background-color: rgb(255, 162, 115);")
        self.verticalLayout_5 = QVBoxLayout(self.Area_eventos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea.setWidget(self.Area_eventos)

        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.stackedWidget_principal.addWidget(self.pageeventos)
        self.registro = QWidget()
        self.registro.setObjectName(u"registro")
        self.registro.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.registro)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, -1, -1)
        self.contenido_registro = QFrame(self.registro)
        self.contenido_registro.setObjectName(u"contenido_registro")
        self.contenido_registro.setStyleSheet(u"QFrame{\n"
"background-color: rgba(173, 216, 230, 0.5);\n"
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
"    background-color: #2980b9; /* Cambio de color al presiona"
                        "r */\n"
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
"    border-top-right-radius: 5px; /* Radio de borde "
                        "superior derecho */\n"
"    border-bottom-right-radius: 5px; /* Radio de borde inferior derecho */\n"
"    background-color: #3498db; /* Color de fondo del bot\u00f3n desplegable */\n"
"}\n"
"\n"
"/* Estilo para QComboBox cuando se despliega y se presiona */\n"
"QComboBox::down-arrow {\n"
"    width: 15px; /* Ancho del icono */\n"
"    height: 15px; /* Alto del icono */\n"
"    padding-right: 5px; /* Espaciado a la derecha del icono */\n"
"}")
        self.contenido_registro.setFrameShape(QFrame.StyledPanel)
        self.contenido_registro.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.contenido_registro)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Nombre = QLineEdit(self.contenido_registro)
        self.Nombre.setObjectName(u"Nombre")

        self.gridLayout_5.addWidget(self.Nombre, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.contenido_registro)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_5.addWidget(self.comboBox, 3, 1, 1, 1)

        self.label_password = QLabel(self.contenido_registro)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_password, 7, 1, 1, 1)

        self.label_correo = QLabel(self.contenido_registro)
        self.label_correo.setObjectName(u"label_correo")
        self.label_correo.setMinimumSize(QSize(142, 0))
        self.label_correo.setMaximumSize(QSize(100, 16777215))
        self.label_correo.setFont(font2)
        self.label_correo.setLayoutDirection(Qt.RightToLeft)
        self.label_correo.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_correo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_correo, 6, 1, 1, 1, Qt.AlignRight)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 5, 1, 1)

        self.Cedula = QLineEdit(self.contenido_registro)
        self.Cedula.setObjectName(u"Cedula")

        self.gridLayout_5.addWidget(self.Cedula, 3, 3, 1, 1)

        self.Correo = QLineEdit(self.contenido_registro)
        self.Correo.setObjectName(u"Correo")

        self.gridLayout_5.addWidget(self.Correo, 6, 3, 1, 1)

        self.password = QLineEdit(self.contenido_registro)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout_5.addWidget(self.password, 7, 3, 1, 1)

        self.acceder = QPushButton(self.contenido_registro)
        self.acceder.setObjectName(u"acceder")

        self.gridLayout_5.addWidget(self.acceder, 8, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 9, 3, 1, 1)

        self.label_correo_3 = QLabel(self.contenido_registro)
        self.label_correo_3.setObjectName(u"label_correo_3")
        self.label_correo_3.setMinimumSize(QSize(142, 0))
        self.label_correo_3.setMaximumSize(QSize(100, 16777215))
        self.label_correo_3.setFont(font2)
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

        self.gridLayout_5.addWidget(self.label_correo_3, 1, 1, 1, 1, Qt.AlignRight)

        self.label = QLabel(self.contenido_registro)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label, 2, 1, 1, 1)

        self.Apellido = QLineEdit(self.contenido_registro)
        self.Apellido.setObjectName(u"Apellido")

        self.gridLayout_5.addWidget(self.Apellido, 2, 3, 1, 1)


        self.horizontalLayout_10.addWidget(self.contenido_registro)

        self.stackedWidget_principal.addWidget(self.registro)
        self.page_perfil = QWidget()
        self.page_perfil.setObjectName(u"page_perfil")
        self.page_perfil.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.page_perfil)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.contenido_registro_2 = QFrame(self.page_perfil)
        self.contenido_registro_2.setObjectName(u"contenido_registro_2")
        self.contenido_registro_2.setStyleSheet(u"QFrame{\n"
"background-color: rgba(173, 216, 230, 0.5);\n"
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
        self.gridLayout_7 = QGridLayout(self.contenido_registro_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Boto_cerrarsesion = QPushButton(self.contenido_registro_2)
        self.Boto_cerrarsesion.setObjectName(u"Boto_cerrarsesion")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/icons8-salida-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boto_cerrarsesion.setIcon(icon2)
        self.Boto_cerrarsesion.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.Boto_cerrarsesion, 10, 4, 1, 2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_12, 2, 4, 1, 1)

        self.perfil_correo = QLineEdit(self.contenido_registro_2)
        self.perfil_correo.setObjectName(u"perfil_correo")
        self.perfil_correo.setReadOnly(True)

        self.gridLayout_7.addWidget(self.perfil_correo, 9, 3, 1, 1, Qt.AlignTop)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 0, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 10, 1, 1, 1)

        self.label_correo_5 = QLabel(self.contenido_registro_2)
        self.label_correo_5.setObjectName(u"label_correo_5")
        self.label_correo_5.setMinimumSize(QSize(142, 35))
        self.label_correo_5.setMaximumSize(QSize(142, 35))
        self.label_correo_5.setFont(font2)
        self.label_correo_5.setLayoutDirection(Qt.RightToLeft)
        self.label_correo_5.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_correo_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_correo_5, 8, 1, 2, 1, Qt.AlignRight)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 1, 6, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)

        self.Foto_usuario = QLabel(self.contenido_registro_2)
        self.Foto_usuario.setObjectName(u"Foto_usuario")
        self.Foto_usuario.setMinimumSize(QSize(150, 150))
        self.Foto_usuario.setMaximumSize(QSize(150, 150))
        self.Foto_usuario.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.Foto_usuario.setPixmap(QPixmap(u":/iconos/icons8-nombre-100.png"))
        self.Foto_usuario.setScaledContents(True)

        self.gridLayout_7.addWidget(self.Foto_usuario, 1, 5, 4, 1)

        self.Boton_cambiarContra = QToolButton(self.contenido_registro_2)
        self.Boton_cambiarContra.setObjectName(u"Boton_cambiarContra")

        self.gridLayout_7.addWidget(self.Boton_cambiarContra, 9, 5, 1, 1)

        self.Boton_EditarDatos = QToolButton(self.contenido_registro_2)
        self.Boton_EditarDatos.setObjectName(u"Boton_EditarDatos")

        self.gridLayout_7.addWidget(self.Boton_EditarDatos, 9, 4, 1, 1, Qt.AlignRight)

        self.Boton_CambiarFoto = QToolButton(self.contenido_registro_2)
        self.Boton_CambiarFoto.setObjectName(u"Boton_CambiarFoto")
        self.Boton_CambiarFoto.setStyleSheet(u"# Estilos para QToolButton\n"
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
"}")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/icons8-imagen-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Boton_CambiarFoto.setIcon(icon3)
        self.Boton_CambiarFoto.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.Boton_CambiarFoto, 7, 5, 1, 2)

        self.comboBox_2 = QComboBox(self.contenido_registro_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(142, 35))
        self.comboBox_2.setMaximumSize(QSize(142, 35))
        self.comboBox_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_7.addWidget(self.comboBox_2, 7, 1, 1, 1)

        self.perfil_cedula = QLineEdit(self.contenido_registro_2)
        self.perfil_cedula.setObjectName(u"perfil_cedula")
        self.perfil_cedula.setReadOnly(True)

        self.gridLayout_7.addWidget(self.perfil_cedula, 7, 3, 1, 1)

        self.label_2 = QLabel(self.contenido_registro_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(142, 35))
        self.label_2.setMaximumSize(QSize(142, 35))
        self.label_2.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_2, 4, 1, 1, 1)

        self.perfil_apellido = QLineEdit(self.contenido_registro_2)
        self.perfil_apellido.setObjectName(u"perfil_apellido")
        self.perfil_apellido.setReadOnly(True)

        self.gridLayout_7.addWidget(self.perfil_apellido, 4, 3, 1, 1)

        self.label_correo_4 = QLabel(self.contenido_registro_2)
        self.label_correo_4.setObjectName(u"label_correo_4")
        self.label_correo_4.setMinimumSize(QSize(142, 35))
        self.label_correo_4.setMaximumSize(QSize(142, 35))
        self.label_correo_4.setFont(font2)
        self.label_correo_4.setLayoutDirection(Qt.LeftToRight)
        self.label_correo_4.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.label_correo_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_correo_4, 3, 1, 1, 1)

        self.perfil_nombre = QLineEdit(self.contenido_registro_2)
        self.perfil_nombre.setObjectName(u"perfil_nombre")
        self.perfil_nombre.setReadOnly(True)

        self.gridLayout_7.addWidget(self.perfil_nombre, 3, 3, 1, 1)

        self.Label_usuario = QLabel(self.contenido_registro_2)
        self.Label_usuario.setObjectName(u"Label_usuario")
        self.Label_usuario.setMinimumSize(QSize(142, 35))
        self.Label_usuario.setMaximumSize(QSize(142, 35))
        self.Label_usuario.setLayoutDirection(Qt.LeftToRight)
        self.Label_usuario.setStyleSheet(u"color: #2c3e50; /* Color del texto */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Negrita */\n"
"    font-family: Arial, sans-serif; /* Fuente */\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 2px solid #3498db; /* Borde */\n"
"    border-radius: 10px; /* Radio de borde */\n"
"    padding: 5px 10px; /* Espaciado interno */")
        self.Label_usuario.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.Label_usuario, 2, 1, 1, 1)

        self.Line_tipoUsuario = QLineEdit(self.contenido_registro_2)
        self.Line_tipoUsuario.setObjectName(u"Line_tipoUsuario")
        self.Line_tipoUsuario.setReadOnly(True)

        self.gridLayout_7.addWidget(self.Line_tipoUsuario, 2, 3, 1, 1)

        self.label_correo_5.raise_()
        self.perfil_correo.raise_()
        self.Boton_CambiarFoto.raise_()
        self.Foto_usuario.raise_()
        self.Boto_cerrarsesion.raise_()
        self.Boton_cambiarContra.raise_()
        self.Boton_EditarDatos.raise_()
        self.comboBox_2.raise_()
        self.perfil_cedula.raise_()
        self.label_2.raise_()
        self.perfil_apellido.raise_()
        self.label_correo_4.raise_()
        self.perfil_nombre.raise_()
        self.Label_usuario.raise_()
        self.Line_tipoUsuario.raise_()

        self.horizontalLayout_7.addWidget(self.contenido_registro_2)

        self.stackedWidget_principal.addWidget(self.page_perfil)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.page_admin.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.page_admin)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_admin)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: rgb(177, 103, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border-top-left-radius: 2px;\n"
"border-bottom-left-radius: 2px;\n"
"padding:2px;\n"
"border-bottom-color:white;\n"
"gridline-color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Arial Narrow\";\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color:rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"padding:2px;\n"
"border-bottom-color:white;\n"
"gridline-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"padding:2px;\n"
"border-bottom-color:white;\n"
"gridline-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 3, 0, 0)
        self.botonAdmUsuarios = QPushButton(self.frame_2)
        self.botonAdmUsuarios.setObjectName(u"botonAdmUsuarios")
        self.botonAdmUsuarios.setMinimumSize(QSize(0, 50))
        self.botonAdmUsuarios.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.botonAdmUsuarios)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.pushButton_2)

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
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_3)

        self.stackedWidget_principal.addWidget(self.page_admin)

        self.horizontalLayout_2.addWidget(self.stackedWidget_principal)


        self.verticalLayout.addWidget(self.contenido)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_principal.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Boton_inicio.setText("")
        self.Boton_ingresar.setText(QCoreApplication.translate("MainWindow", u"INICIAR SESION\n"
"           O\n"
"  REGISTRARSE", None))
        self.imagen_4.setText("")
        self.Bonton_proxEvento.setText(QCoreApplication.translate("MainWindow", u"Proximos eventos", None))
        self.Boton_objetos.setText(QCoreApplication.translate("MainWindow", u"Objetos del museo", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lunes: Cerrado", None))
        self.label_24.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Martes - S\u00e1bado: 10:00 a. m. - 5:00 p. m.", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Domingo: Cerrado", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ten en cuenta que nuestros horarios", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"pueden cambiar sin previo aviso. ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Horarios", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"601 343 2222", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"wmuseo@banrep.gov.co", None))
        self.label_23.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Contacto", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Cra. 6 #15-88", None))
        self.titulo_cartel_1.setText(QCoreApplication.translate("MainWindow", u"Programa tu visita al museo", None))
        self.imagen_cartel_1.setText("")
        self.cuerpo_cartel_1.setText(QCoreApplication.translate("MainWindow", u"El Museo del Oro del Banco de la Rep\u00fablica \n"
"preserva colecciones arqueol\u00f3gicas \n"
"que son un patrimonio y un orgullo de \n"
"todos los colombianos.", None))
        self.imagen_cartel_2.setText("")
        self.titulo_cartel_2.setText(QCoreApplication.translate("MainWindow", u"Palabras de vida", None))
        self.cuerpo_cartel_2.setText(QCoreApplication.translate("MainWindow", u"\u00bfCoronas de plumas, \n"
"maguar\u00e9s, trajes de corteza \n"
"de \u00e1rbol para las celebraciones \n"
"de enmascarados?", None))
        self.titulo_cartel_3.setText(QCoreApplication.translate("MainWindow", u"Maletas didacticas \n"
"del museo de oro", None))
        self.cuerpo_cartel_3.setText(QCoreApplication.translate("MainWindow", u"Materiales did\u00e1cticos, ll\u00fadicos e interactivos \n"
"de pr\u00e9stamo gratuito sobre el patrimonio y \n"
"la identidad cultural, la diversidad y la convivencia.", None))
        self.imagen_cartel_3.setText("")
        self.Correo_2.setInputMask("")
        self.Correo_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@email.com", None))
        self.label_titulo_2.setText(QCoreApplication.translate("MainWindow", u"INICIO DE SESION", None))
        self.acceder_2.setText(QCoreApplication.translate("MainWindow", u"ACCEDER", None))
        self.label_password_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"************", None))
        self.label_correo_2.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.Registrarse.setText(QCoreApplication.translate("MainWindow", u"\u00bfNo tienes una cuenta?", None))
        self.Nombre.setInputMask("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CC", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CE", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"RC", None))

        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.label_correo.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.Cedula.setInputMask("")
        self.Cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123456789", None))
        self.Correo.setInputMask("")
        self.Correo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@email.com", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"************", None))
        self.acceder.setText(QCoreApplication.translate("MainWindow", u"CREAR CUENTA", None))
        self.label_correo_3.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.Apellido.setInputMask("")
        self.Apellido.setText("")
        self.Boto_cerrarsesion.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESION", None))
#if QT_CONFIG(shortcut)
        self.Boto_cerrarsesion.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.perfil_correo.setInputMask("")
        self.label_correo_5.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.Boton_cambiarContra.setText(QCoreApplication.translate("MainWindow", u"Cambiar Contase\u00f1a", None))
        self.Boton_EditarDatos.setText(QCoreApplication.translate("MainWindow", u"Editar Datos", None))
        self.Boton_CambiarFoto.setText(QCoreApplication.translate("MainWindow", u"Cambiar imagen", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"CC", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"TI", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"CE", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"RC", None))

        self.perfil_cedula.setInputMask("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.perfil_apellido.setInputMask("")
        self.perfil_apellido.setText("")
        self.label_correo_4.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.perfil_nombre.setInputMask("")
        self.Label_usuario.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.botonAdmUsuarios.setText(QCoreApplication.translate("MainWindow", u"ADMINISTAR USUARIOS", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"ADMINISTAR EVENTOS", None))
    # retranslateUi

