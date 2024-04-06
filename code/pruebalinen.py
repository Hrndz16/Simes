from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QPushButton,QLineEdit,QLabel,QWidget,QVBoxLayout
import sys
class main(QWidget):
    def __init__(self):
        super().__init__()
        self.l= QVBoxLayout(self)
        self.b = QPushButton(text = 'boton')
        self.line = QLineEdit()
        self.label = QLabel('si sabe')
        self.l.addWidget(self.b)
        self.l.addWidget(self.line)
        self.b.clicked.connect(lambda: self.p1(self.line))
        
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
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = main()
    ma.show()
    app.exec()