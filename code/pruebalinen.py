from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QPushButton,QLineEdit,QLabel,QWidget,QVBoxLayout
from PySide6.QtGui import QPixmap
import sys,os
class main(QWidget):
    def __init__(self):
        super().__init__()
        self.l= QVBoxLayout(self)
        self.b = QPushButton(text = 'boton')
        self.line = QLineEdit()
        self.label = QLabel('si sabe')
        self.l.addWidget(self.b)
        self.l.addWidget(self.line)
        self.l.addWidget(self.label)
        self.b.clicked.connect(lambda: self.agregar_foto(self.label))
        
    def p1(self,line):
        self.l.addWidget(self.label)
        line.setText('texo ')
        self.b.clicked.disconnect()
        self.b.clicked.connect(lambda: self.otra())      
        
          
    def otra(self):
        self.line.setPlaceholderText('mmmmmm')
        texto = self.line.text()
        self.label.setText(texto)
        print(type(texto))
        self.rororor()
        
    def rororor(self):
        self.b.clicked.disconnect()
        self.b.clicked.connect(lambda:print('si master '))
        
    def agregar_foto(self,label):
        fot = QPixmap(os.path.join(os.path.dirname(os.path.dirname(__file__)),"imgs","cartel2.png"))
        label.setPixmap(fot)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = main()
    ma.show()
    app.exec()