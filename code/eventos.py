from Ui_baseEvento import Ui_MainWindow as frame
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from horas import FrameHora
from database import DataBase
import locale
class FrameEvento(frame,QMainWindow):
    def __init__(self,fecha,cedula):
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
        fecha_proporcionada = fecha
        dia= fecha_proporcionada.strftime("%A")
        fecha_f = fecha_proporcionada.strftime("%d-%m-%y")
        self.dia_evento.setText(f'{dia}, {fecha_f}')
        self.cedula=cedula
        self.agregaritem(fecha)
        
         # Conecta la señal button_clicked de cada FrameHora a la función handle_button_clicked
        for i in range(self.gridLayout_7.count()):
            widget = self.gridLayout_7.itemAt(i).widget()
            if isinstance(widget, FrameHora):
                widget.button_clicked.connect(self.handle_button_clicked)
        
        self.obtenerEvento()

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
            
    
    def agregaritem(self,fecha):
        horas=self.datab.consultarHoras(fecha)
        i=1
        if self.cedula != 0 and self.datab.consultarusuarioRegistro(self.cedula):
            eventos = self.datab.consultarRegistros(self.cedula)
            for hora in horas:
                widget=FrameHora(hora[0],hora[1],hora[2],hora[3])
                for evento in eventos:
                    if widget.id==evento[1]:
                        widget.ui.boton_sub.setText('Cancelar')
                self.gridLayout_7.addWidget(widget,i,0,1,2)
                i+=1
        else:
            for hora in horas:
                widget=FrameHora(hora[0],hora[1],hora[2],hora[3])
                self.gridLayout_7.addWidget(widget,i,0,1,2)
                i+=1
    def obtenerEvento(self):
        return self.Frame_base_evento

    
    