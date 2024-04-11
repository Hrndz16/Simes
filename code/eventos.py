from Ui_baseEvento import Ui_MainWindow as frame
from PySide6.QtWidgets import QMainWindow
from horas import FrameHora
from database import DataBase
from datetime import datetime
import locale
class FrameEvento(frame,QMainWindow):
    def __init__(self,fecha):
        # Configura el idioma a español
        locale.setlocale(locale.LC_TIME,'')
        self.datab=DataBase()
        super().__init__()
        self.setupUi(self)
        fecha_proporcionada = fecha
        dia= fecha_proporcionada.strftime("%A")
        fecha_f = fecha_proporcionada.strftime("%d-%m-%y")
        self.dia_evento.setText(f'{dia}, {fecha_f}')
        
        self.agregaritem(fecha)
        self.obtenerEvento()
    def agregaritem(self,fecha):
        horas=self.datab.consultarHoras(fecha)
        i=1
        for hora in horas:
            widget=FrameHora(hora[0],hora[1],hora[2],hora[3])
            self.gridLayout_7.addWidget(widget,i,0,1,2)
            i+=1
    def obtenerEvento(self):
        return self.Frame_base_evento

    
    