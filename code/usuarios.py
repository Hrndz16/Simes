#Importaciones necesarias
import sys,os
ruta = os.path.dirname(os.path.dirname(__file__))
sys.path.append(f'{ruta}\\imgs')
from Ui_frameUsuario import Ui_MainWindow as frame
from PySide6.QtWidgets import QMainWindow, QMessageBox,QFrame
from PySide6.QtCore import Qt
from database import DataBase
import locale

class FrameUsuario(frame,QMainWindow):
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
        

    def handle_button_clicked(self, id , frame):
            if self.cedula == 0:
                self.mensaje.setText('Se necesita estar registrado para hacer esto')
                self.mensaje.exec()
            elif self.datab.consultarRegistro(self.cedula,id):
                self.mensaje2.setText('Estas seguro de que quieres cancelar tu asistencia')
                
                resultado = self.mensaje2.exec_()
                if resultado == QMessageBox.Yes:
                    self.datab.eliminarRegistro(self.cedula,id)
                    self.mensaje.setText('Se ha cancelado tu asistencia')
                    self.mensaje.exec()
                    frame.ui.boton_sub.setText('Suscribirse')
                    
            else:
                self.datab.registrarEvento(self.cedula, id)
                self.mensaje.setText('Se ha registrado su asistencia')
                self.mensaje.exec()
                frame.ui.boton_sub.setText('Cancelar')
            
    
    def obtenerUsuario(self):
        return self.usuario_frame
    
    def llenar_frame (self,tipou,nombre,apellido,correo,foto):
        nom = f'{nombre} {apellido}'
        self.label_correo.setText(correo)
        self.label_nombre.setText(nom)
        self.label_tipoU.setText(self.tipoUsuario(tipou))
        
        
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
        
        