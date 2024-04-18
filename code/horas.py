from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from Ui_ItemHora import Ui_ItemHora  # Importa la clase generada por Qt Designer

class FrameHora(QFrame):
    button_clicked = Signal(int,QFrame)  # Señal que emite la ID del objeto cuando se hace clic en el botón

    def __init__(self, id, hora, descripcion, titulo):
        super().__init__()
        self.ui = Ui_ItemHora()  # Instancia de la interfaz de usuario generada por Qt Designer
        self.ui.setupUi(self)  # Configura la interfaz de usuario en este widget

        # Asigna los valores proporcionados
        self.ui.Hora.setText(hora)
        self.ui.Descripcion.setWordWrap(True)
        self.ui.Descripcion.setText(descripcion)
        self.ui.label.setText(titulo)
        self.id = id

        # Conecta la señal clicked del botón a la función que emitirá la señal personalizada
        self.ui.boton_sub.clicked.connect(self.emit_button_clicked)

    def emit_button_clicked(self):
        # Cuando se hace clic en el botón, emite la señal button_clicked con la ID del objeto
        self.button_clicked.emit(self.id,self)
        
        

    def obtenerHora(self):
        return self.base_horas_eventos