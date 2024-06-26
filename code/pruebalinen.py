
from PySide6.QtWidgets import QApplication, QLabel,QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget,QHBoxLayout
from PySide6.QtGui import QTextCharFormat, QFont
from usuarios import FrameUsuario as frame
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.h_layout = QVBoxLayout(self)
        self.frame1 = frame('frame')
        self.frame2 = frame('frame2')
        self.h_layout.insertWidget(0,self.frame1)
        self.h_layout.insertWidget(1,self.frame2)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

# import sys
# from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

# class MyDialog(QDialog):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Mi Diálogo")
#         layout = QVBoxLayout(self)

#         # Agregar etiquetas
#         label1 = QLabel("Nombre:", self)
#         layout.addWidget(label1)

#         # Agregar campo de entrada
#         line_edit1 = QLineEdit(self)
#         layout.addWidget(line_edit1)

#         # Agregar más etiquetas y campos de entrada si es necesario
#         # ...

#         # Agregar botón
#         button = QPushButton("Aceptar", self)
#         button.clicked.connect(self.accept)  # Cierra el cuadro de diálogo cuando se hace clic en el botón
#         layout.addWidget(button)

#         # Configurar el diseño del cuadro de diálogo
#         self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dialog = MyDialog()
#     dialog.exec()
#     sys.exit(app.exec())
###############################################################################
# from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
# from PySide6.QtGui import QTextCharFormat, QFont
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Creamos un QTextEdit y dos botones
#         self.textEdit = QTextEdit()
#         self.boldButton = QPushButton("Negrita")
#         self.italicButton = QPushButton("Cursiva")

#         # Conectamos los botones a sus respectivas funciones
#         self.boldButton.clicked.connect(self.makeBold)
#         self.italicButton.clicked.connect(self.makeItalic)

#         # Creamos un layout y añadimos los widgets
#         layout = QVBoxLayout()
#         layout.addWidget(self.textEdit)
#         layout.addWidget(self.boldButton)
#         layout.addWidget(self.italicButton)

#         # Creamos un widget central para la ventana
#         centralWidget = QWidget()
#         centralWidget.setLayout(layout)
#         self.setCentralWidget(centralWidget)

#     def makeBold(self):
#         # Esta función hace que el texto seleccionado se vuelva negrita
#         format = QTextCharFormat()
#         format.setFontWeight(QFont.Bold)

#         # Aplicamos el formato al texto seleccionado
#         self.textEdit.mergeCurrentCharFormat(format)

#     def makeItalic(self):
#         # Esta función hace que el texto seleccionado se vuelva cursiva
#         format = QTextCharFormat()
#         format.setFontItalic(True)

#         # Aplicamos el formato al texto seleccionado
#         self.textEdit.mergeCurrentCharFormat(format)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())

# import sys
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton


# class TableWithButtons(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Tabla con Botones")
#         self.setGeometry(100, 100, 600, 400)

#         layout = QVBoxLayout()
#         self.table = QTableWidget()

#         # Establecer el número de filas y columnas
#         self.table.setRowCount(3)
#         self.table.setColumnCount(2)

#         # Encabezados
#         self.table.setHorizontalHeaderLabels(["Nombre", "Acción"])

#         # Insertar botones en la tabla
#         self.insert_buttons()

#         layout.addWidget(self.table)
#         self.setLayout(layout)

#     def insert_buttons(self):
#         for row in range(self.table.rowCount()):
#             name_item = QTableWidgetItem(f"Item {row}")
#             self.table.setItem(row, 0, name_item)

#             button = QPushButton("Hacer algo")
#             button.clicked.connect(self.button_clicked)

#             self.table.setCellWidget(row, 1, button)

#     def button_clicked(self):
#         button = self.sender()
#         if button:
#             index = self.table.indexAt(button.pos())
#             if index.isValid():
#                 row = index.row()
#                 print(f"Botón en la fila {row} clickeado.")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = TableWithButtons()
#     window.show()
#     sys.exit(app.exec())
#################################################################################################################
# import sys
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem


# class UserAdmin(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Administrador de Usuarios")
#         self.setGeometry(100, 100, 600, 400)

#         self.init_ui()

#     def init_ui(self):
#         # Layout principal
#         main_layout = QVBoxLayout()

#         # Layout para agregar usuarios
#         add_user_layout = QHBoxLayout()
#         self.name_entry = QLineEdit()
#         self.add_button = QPushButton("Agregar")
#         add_user_layout.addWidget(QLabel("Nombre:"))
#         add_user_layout.addWidget(self.name_entry)
#         add_user_layout.addWidget(self.add_button)

#         # Tabla para mostrar usuarios
#         self.user_table = QTableWidget()
#         self.user_table.setColumnCount(2)
#         self.user_table.setHorizontalHeaderLabels(["ID", "Nombre"])
#         self.user_table.horizontalHeader().setStretchLastSection(True)
#         self.user_table.setEditTriggers(QTableWidget.NoEditTriggers)

#         # Botón para eliminar usuario
#         self.delete_button = QPushButton("Eliminar Usuario")

#         main_layout.addLayout(add_user_layout)
#         main_layout.addWidget(self.user_table)
#         main_layout.addWidget(self.delete_button)

#         self.setLayout(main_layout)

#         # Conectar señales
#         self.add_button.clicked.connect(self.add_user)
#         self.delete_button.clicked.connect(self.delete_user)

#     def add_user(self):
#         name = self.name_entry.text()
#         if name:
#             row_position = self.user_table.rowCount()
#             self.user_table.insertRow(row_position)
#             self.user_table.setItem(row_position, 0, QTableWidgetItem(str(row_position + 1)))
#             self.user_table.setItem(row_position, 1, QTableWidgetItem(name))
#             self.name_entry.clear()

#     def delete_user(self):
#         selected_row = self.user_table.currentRow()
#         if selected_row >= 0:
#             self.user_table.removeRow(selected_row)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = UserAdmin()
#     window.show()
#     sys.exit(app.exec())


############################################################################################################################

# import os,sys
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication,QPushButton,QLineEdit,QLabel,QWidget,QVBoxLayout
# from PySide6.QtGui import QPixmap
# class main(QWidget):
#     def __init__(self):
#         super().__init__()
#         latout = QVBoxLayout(self)
#         img = QPixmap(os.path.join(os.path.dirname(os.path.dirname(__file__)),"imgs","fondoInisioSesion.jpg"))
#         label = QLabel()
#         label.setPixmap(img)
        
#         latout.addWidget(label)
#         latout.minimumSize()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ma = main()
#     ma.show()
#     app.exec()
# from PySide6.QtCore import QTime
# hora1 = QTime(12,40).toString("h:mm AP")
# hora2 = QTime(13,40).toString("h:mm AP")
# print(hora1,hora2)
# if QTime.fromString(hora1,"h:mm AP") < QTime.fromString(hora2,"h:mm AP"):
#     print('Si se pudieron comparar')

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