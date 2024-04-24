#Importaciones necesarias
import sys,os
ruta = os.path.dirname(os.path.dirname(__file__))
sys.path.append(f'{ruta}\\imgs')
from Ui_frameUsuario import Ui_MainWindow as frame
from PySide6.QtWidgets import QMainWindow, QMessageBox,QFrame,QWidget
from PySide6.QtCore import Qt, Signal
from database import DataBase
import locale
from PySide6.QtGui import QPixmap

class FrameUsuario(frame,QMainWindow):
    button_clicked = Signal(str,QFrame)  # Señal que emite la ID del objeto cuando se hace clic en el botón

    def __init__(self,tipou,nombre,apellido,correo,foto):
        self.mensaje = QMessageBox()
        self.mensaje.setStyleSheet("""
                QMessageBox {
                    background-color: #f0f0f0;
                    border: 2px solid darkgray;
                    border-radius: 100%;
                }
                QMessageBox QLabel {
                    color: #333;
                }
                QMessageBox QPushButton {
                    background-color: #c57007;
                    color: white;
                    border-radius: 5px;
                    padding: 5px 10px;
                }
                QMessageBox QPushButton:hover {
                    background-color:#f49011;
                }
            """)
        
        self.mensaje.setStandardButtons(QMessageBox.Ok)
        self.mensaje.setWindowFlags(Qt.FramelessWindowHint)
        self.mensaje2 = QMessageBox()
        self.mensaje2.setStyleSheet("""
                QMessageBox {
                    background-color: #f0f0f0;
                    border: 2px solid darkgray;
                    border-radius: 100%;
                }
                QMessageBox QLabel {
                    color: #333;
                }
                QMessageBox QPushButton {
                    background-color: #c57007;
                    color: white;
                    border-radius: 5px;
                    padding: 5px 10px;
                }
                QMessageBox QPushButton:hover {
                    background-color:#f49011;
                }
            """)
    
        self.mensaje2.addButton(QMessageBox.Yes)
        self.mensaje2.addButton(QMessageBox.No)
        self.mensaje2.setWindowFlags(Qt.FramelessWindowHint)
        # Configura el idioma a español
        locale.setlocale(locale.LC_TIME,'')
        self.datab=DataBase()
        super().__init__()
        self.setupUi(self)
        self.llenar_frame(tipou,nombre,apellido,correo,foto)
        self.obtenerUsuario()
        
        self.Boton_eliminar.clicked.connect(self.emit_button_clicked)
        self.id = str(correo)

    def emit_button_clicked(self):
        # Cuando se hace clic en el botón, emite la señal button_clicked con la ID del objeto
        self.button_clicked.emit(self.id,self)
    
            
    
    def obtenerUsuario(self):
        return self.usuario_frame
    
    def llenar_frame (self,tipou,nombre,apellido,correo,foto):
        nom = f'{nombre} {apellido}'
        self.label_correo.setText(correo)
        self.label_nombre.setText(nom)
        self.label_tipoU.setText(self.tipoUsuario(tipou))
        self.agregarFotoPerfil_listaCoordinadores(foto)
        
          
    def tipoUsuario(self,tipo): 
        """Clasifica el tipo usuario en un strig 1 = "administrador", 2 = "Coordinador" 3 = "Visitante" """
        tipo = int(tipo)
        match tipo:
            case  1:
                return 'Administrador'
            case 2:
                return 'Coordinador'
            case 3:
                return 'Visitante'
            
    def agregarFotoPerfil_listaCoordinadores(self,ruta):
        if ruta is not None:
            foto = QPixmap(os.path.join(ruta))
            self.img_perfil.setPixmap(foto)
        
        