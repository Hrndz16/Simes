from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QWidget
from Ui_base_mensaje import Ui_Form as ui
from PySide6.QtCore import Signal

class frameMensaje(ui,QFrame):
    clicked = Signal(QFrame)
    def __init__(self,de,asunto,desc):
        super().__init__()
        self.setupUi(self)
        self.de_label.setText(de)
        self.asunto_label.setText(asunto)
        self.desc=desc
        self.obtenerMensaje()
    
    def mousePressEvent(self, event):
        self.clicked.emit(self)
        QFrame.mousePressEvent(self, event)
    
    def obtenerMensaje(self):
        return self.frame
        
    
     