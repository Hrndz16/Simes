from Ui_baseEvento import Ui_MainWindow as frame
from PySide6.QtWidgets import QMainWindow

class FrameEvento(frame,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.obtenerEvento()
        
    def obtenerEvento(self):
        return self.Frame_base_evento

    
    