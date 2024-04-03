#Importaciones necesarias
import sys,os
ruta = os.path.dirname(os.path.dirname(__file__))
sys.path.append(f'{ruta}\\imgs')
from PySide6.QtWidgets import QMainWindow,QApplication,QVBoxLayout,QMessageBox,QLineEdit
from Ui_mainwindow import Ui_MainWindow as MW
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from eventos import FrameEvento
from database import DataBase



class MainWindow(QMainWindow,MW):#Creacion de main Window
    def __init__(self):
        self.mensaje = QMessageBox()
        self.mensaje.setStyleSheet("""
                QMessageBox {
                    background-color: #f0f0f0;
                    border: 2px solid darkgray;
                    border-radius: 10px;
                }
                QMessageBox QLabel {
                    color: #333;
                }
                QMessageBox QPushButton {
                    background-color: #007bff;
                    color: white;
                    border-radius: 5px;
                    padding: 5px 10px;
                }
                QMessageBox QPushButton:hover {
                    background-color: #0056b3;
                }
            """)
        self.db=DataBase()
        self.tipo_usuario=0#variable para saber que usuario esta activo acutalmente 0=Usuario sin cuenta 1=Administrador 2=Cordinador 3=Usuario con cuenta
        super().__init__()
        self.setupUi(self)#Carga el ui de qtdesigner
        self.stackedWidget_principal.setCurrentIndex(0)#pone la ventana principal
        self.Boton_ingresar.clicked.connect(lambda:self.botonIngresar())#configura el boton de inicio de sesion
        self.Boton_inicio.clicked.connect(lambda:self.botonInicio())#configura el boton de inicio(home)
        self.Registrarse.clicked.connect(lambda:self.botonRegistrarse())#configura el boton de Registarse
        self.Bonton_proxEvento.clicked.connect(lambda:self.botonProxEvento())#configura el boton de proximo evento
        self.acceder_2.clicked.connect(lambda:self.iniciarSesion())
        self.acceder.clicked.connect(lambda:self.RegistrarUsuario())
        self.mensaje.setIcon(QMessageBox.Information)
        self.mensaje.setStandardButtons(QMessageBox.Ok)
        self.mensaje.setWindowFlags(Qt.FramelessWindowHint)
        
    
    def botonIngresar(self):
        self.Correo_2.clear()
        self.password_2.clear()
        self.stackedWidget_principal.setCurrentIndex(1) if self.tipo_usuario == 0 else self.stackedWidget_principal.setCurrentIndex(4) #coloca en la ventana de ingreso o inicio de sesion   
    def botonInicio(self):    
        if self.tipo_usuario == 0 or self.tipo_usuario==3 :
            self.stackedWidget_principal.setCurrentIndex(0) #coloca en la ventana de inicio segun el tipo de usuario 
         #coloca en la ventana de inicio segun el tipo de usuario
        else:
            self.stackedWidget_principal.setCurrentIndex(5)
    def botonRegistrarse(self):
        self.stackedWidget_principal.setCurrentIndex(3)#coloca en la ventana de registro
    def botonProxEvento(self):
        self.stackedWidget_principal.setCurrentIndex(2)#coloca en la ventana de proximo evento
    def iniciarSesion(self):
        correo=self.Correo_2.text()
        contraseña=self.password_2.text()
        if self.db.isExist('usuarios','correo',correo) and self.db.isExist('usuarios','contra',contraseña):
            self.tipo_usuario = self.db.consultarTipoU(correo)
            self.botonInicio()
            self.Boton_ingresar.setText('  MI PERFIL') #INICIAR SESION\n           O\n  REGISTRARSE
            self.Boton_ingresar.setFont(QFont('Arial Narrow', 15))
        else:
            self.mensaje.setText("Correo o Contraseña incorrectos.")   
            self.mensaje.exec_()
            self.password_2.clear()
            
    def RegistrarUsuario(self):
        nombre=self.Nombre.text()
        tipoCC=self.comboBox.currentText()
        cc=int(self.Cedula.text())
        apellido=self.Apellido.text()
        correo=self.Correo.text()
        contra=self.password.text()
        if self.db.isExist('usuarios','id',cc)==False:
            if self.db.isExist('usuarios','correo',correo)==False:
                self.db.registarUsuario(nombre,tipoCC,cc,apellido,correo,contra)
                self.mensaje.setText("El usuario ha sido registrado!!")
                self.mensaje.exec_()
                self.botonIngresar()
                self.limpiar_lineedits()
            else:
                self.mensaje.setText("Error el correo ya ha sido registrado")
                self.mensaje.exec_()
        else:
            self.mensaje.setText("Error el usuario ya tiene una cuenta")
            self.mensaje.exec_()
            self.limpiar_lineedits()
    
    def limpiar_lineedits(self):
        # Recorremos todos los widgets hijos del frame
        for widget in self.findChildren(QLineEdit):
            # Verificamos si el widget es un QLineEdit
            if isinstance(widget, QLineEdit):
                # Limpiamos el texto del QLineEdit
                widget.clear()
        
if __name__ == '__main__':#crea la ventana
    app = QApplication(sys.argv)
    window=MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
