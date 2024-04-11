from PySide6.QtWidgets import QFrame, QVBoxLayout
from Ui_ItemHora import Ui_ItemHora  # Importa la clase generada por Qt Designer

class FrameHora(QFrame):
    def __init__(self, id, hora, descripcion,titulo):
        super().__init__()
        self.ui = Ui_ItemHora()  # Instancia de la interfaz de usuario generada por Qt Designer
        self.ui.setupUi(self)  # Configura la interfaz de usuario en este widget

        # Asigna los valores proporcionados
        self.ui.Hora.setText(hora)
        self.ui.Descripcion.setWordWrap(True)
        self.ui.Descripcion.setText(descripcion)
        self.ui.label.setText(titulo)

        self.id = id

        # Elimina la asignación de layout None
        # self.setLayout(None)

    def obtenerHora(self):
        return self.base_horas_eventos