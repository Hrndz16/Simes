# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base_mensaje.ui'
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
    QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 394)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 180))
        self.frame.setMaximumSize(QSize(16777215, 180))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(0, 0, 0);\n"
"}\n"
"QFrame#frame::hover{\n"
"background-color: rgb(240, 241, 241);\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"QLabel{\n"
"background-color: transparent;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(35, 16777215))
        self.label.setSizeIncrement(QSize(30, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.de_label = QLabel(self.frame)
        self.de_label.setObjectName(u"de_label")
        self.de_label.setFont(font)

        self.gridLayout.addWidget(self.de_label, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.asunto_label = QLabel(self.frame)
        self.asunto_label.setObjectName(u"asunto_label")
        self.asunto_label.setFont(font1)
        self.asunto_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.asunto_label, 3, 1, 1, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Raised)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_3, 0, 0, 1, 2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"De:", None))
        self.de_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Asunto:", None))
        self.asunto_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

