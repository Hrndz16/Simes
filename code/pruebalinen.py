from PySide6.QtCore import QTime
hora1 = QTime(12,40).toString("h:mm AP")
hora2 = QTime(13,40).toString("h:mm AP")
print(hora1,hora2)
if QTime.fromString(hora1,"h:mm AP") < QTime.fromString(hora2,"h:mm AP"):
    print('Si se pudieron comparar')

#######################################################################################################################################

# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication,QPushButton,QLineEdit,QLabel,QWidget,QVBoxLayout
# from PySide6.QtGui import QPixmap
# import sys,os,psycopg2
# class main(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.l= QVBoxLayout(self)
#         self.b = QPushButton(text = 'boton')
#         self.line = QLineEdit()
#         self.label = QLabel('si sabe')
#         self.l.addWidget(self.b)
#         self.l.addWidget(self.line)
#         self.l.addWidget(self.label)
#         self.b.clicked.connect(lambda: self.imagenBite())
#         self.coneccion = psycopg2.connect(user='postgres',password = 'POSTGRES1',host='127.0.0.1', port='5432', database='db_Simes')
#         self.cur = self.coneccion.cursor()
        
        
#     def imagenBite(self):
#         img = 'D:\\DELL\\Downloads\\SSIMES\\Simes\\imgsperfil\\img2002.jpg'
#         with open (img,'rb') as img:
#             bite = img.read()
#             print(bite)
#             self.reescribir_imagen(bite)
#             img.close()
            
#     def reescribir_imagen(self,img):
#         ruta = rutaFoto = os.path.dirname(os.path.dirname(__file__))+f'\\imgsperfil\\imgzzzz.jpg'

#         with open(ruta,'wb') as lec:
#             lec.write(img)
            
        
#     def p1(self,line):
#         self.l.addWidget(self.label)
#         line.setText('texo ')
#         self.b.clicked.disconnect()
#         self.b.clicked.connect(lambda: self.otra())      
        
          
#     def otra(self):
#         self.line.setPlaceholderText('mmmmmm')
#         texto = self.line.text()
#         self.label.setText(texto)
#         print(type(texto))
#         self.rororor()
        
#     def rororor(self):
#         self.b.clicked.disconnect()
#         self.b.clicked.connect(lambda:print('si master '))
        
#     def agregar_foto(self,label):
#         fot = QPixmap(os.path.join(os.path.dirname(os.path.dirname(__file__)),"imgs","cartel2.png"))
#         label.setPixmap(fot)
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ma = main()
#     ma.show()
#     app.exec()

#############################################################################################################################
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication,QPushButton,QLineEdit,QLabel,QWidget,QVBoxLayout
# from PySide6.QtGui import QPixmap
# import sys,os,psycopg2
# class main(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.l= QVBoxLayout(self)
#         self.b = QPushButton(text = 'boton')
#         self.line = QLineEdit()
#         self.label = QLabel('si sabe')
#         self.l.addWidget(self.b)
#         self.l.addWidget(self.line)
#         self.l.addWidget(self.label)
#         self.b.clicked.connect(lambda: self.imagenBite())
#         self.coneccion = psycopg2.connect(user='postgres',password = 'POSTGRES1',host='127.0.0.1', port='5432', database='db_Simes')
#         self.cur = self.coneccion.cursor()
        
        
#     def imagenBite(self):
#         img = 'D:\\DELL\\Downloads\\SSIMES\\Simes\\imgsperfil\\img2002.jpg'
#         with open (img,'rb') as img:
#             bite = img.read()
#             print(bite)
#             self.reescribir_imagen(bite)
#             img.close()
            
#     def reescribir_imagen(self,img):
#         ruta = rutaFoto = os.path.dirname(os.path.dirname(__file__))+f'\\imgsperfil\\imgzzzz.jpg'

#         with open(ruta,'wb') as lec:
#             lec.write(img)
            
        
#     def p1(self,line):
#         self.l.addWidget(self.label)
#         line.setText('texo ')
#         self.b.clicked.disconnect()
#         self.b.clicked.connect(lambda: self.otra())      
        
          
#     def otra(self):
#         self.line.setPlaceholderText('mmmmmm')
#         texto = self.line.text()
#         self.label.setText(texto)
#         print(type(texto))
#         self.rororor()
        
#     def rororor(self):
#         self.b.clicked.disconnect()
#         self.b.clicked.connect(lambda:print('si master '))
        
#     def agregar_foto(self,label):
#         fot = QPixmap(os.path.join(os.path.dirname(os.path.dirname(__file__)),"imgs","cartel2.png"))
#         label.setPixmap(fot)
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ma = main()
#     ma.show()
#     app.exec()