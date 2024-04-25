import sys,os
ruta = os.path.dirname(os.path.dirname(__file__))
sys.path.append(f'{ruta}\\imgs')
from Ui_Evento_aceptar_rechazar import Ui_MainWindow as frame
from PySide6.QtWidgets import QMainWindow, QMessageBox,QFrame,QWidget
from PySide6.QtCore import Qt, Signal
from database import DataBase
import locale
from PySide6.QtGui import QPixmap

class FrameCancelarEvento(frame,QMainWindow):
    button_clicked = Signal(str,QFrame)  # Señal que emite la ID del objeto cuando se hace clic en el botón
    button_clickedRechazar = Signal(str,QFrame)

    def __init__(self,id,fecha,hora,descripcion, titulo):
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
        self.llenar_frame(id,fecha,hora,descripcion,titulo)
        self.obtenerEvento()
        
        self.boton_CancelarEvento.clicked.connect(self.emit_button_clicked)
        self.Boton_rechazarCancelacion.clicked.connect(self.emit_button_clicked2)

    def emit_button_clicked(self):
        # Cuando se hace clic en el botón, emite la señal button_clicked con la ID del objeto
        self.button_clicked.emit(self.id,self)
        
    
    def emit_button_clicked2(self):
        # Cuando se hace clic en el botón, emite la señal button_clicked con la ID del objeto
        self.button_clickedRechazar.emit(self.id,self)

    
            
    
    def obtenerEvento(self):
        return self.frame_cancelacionEvento
    
    def llenar_frame (self,id,fecha,hora,descripcion,titulo):
        self.id = str(id)
        self.label_fecha.setText(str(fecha))
        self.label_hora.setText(str(hora))
        self.label_descripcion.setText(descripcion)
        self.label_titulo.setText(titulo)
    