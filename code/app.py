#Importaciones necesarias
import sys,os
ruta = os.path.dirname(os.path.dirname(__file__))
sys.path.append(f'{ruta}\\imgs')
from PySide6.QtWidgets import QMainWindow,QApplication,QSpacerItem,QMessageBox,QLineEdit,QFileDialog,QSizePolicy
from Ui_mainwindow import Ui_MainWindow as MW
from PySide6.QtCore import Qt,QDate,QTime
from PySide6.QtGui import QFont,QPixmap
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
        self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())#habilita el cambio de datos de perfil del usuario
        self.Boton_CambiarFoto.clicked.connect(lambda:self.abrir_dialogo_archivo())
        self.Boto_cerrarsesion.clicked.connect(lambda:self.cerrar_sesion())
        self.fechaEvento.setCalendarPopup(True)
        self.Boton_adminUsuarios.clicked.connect(lambda:self.mostrarTablaUsuarios()) # En la pagina del administrador muestra la pagina de administrar usuarios
        self.Boton_adminEventos.clicked.connect(lambda:self.mostrarPaginaAdministrareventos())# En la pagina del administrador muestra la pagina de los eventos 
        
        
    def botonIngresar(self):
        self.Correo_2.clear()
        self.password_2.clear()
        ## self.stackedWidget_principal.setCurrentIndex(1) if self.tipo_usuario == 0 else self.stackedWidget_principal.setCurrentIndex(4) #coloca en la ventana de ingreso o inicio de sesion  
        if self.tipo_usuario == 0:
            self.stackedWidget_principal.setCurrentIndex(1)
        else:
            self.stackedWidget_principal.setCurrentIndex(4)
            self.visible_us() 
            self.cargarFotoPerfil()
            
            
    def botonInicio(self):    
        if self.tipo_usuario == 0 or self.tipo_usuario==3 :
            self.stackedWidget_principal.setCurrentIndex(0) #coloca en la ventana de inicio segun el tipo de usuario 
         #coloca en la ventana de inicio segun el tipo de usuario
        else:
            self.stackedWidget_principal.setCurrentIndex(5)
            self.perfilAdministrador()# Aqui se inicializa la interfaz del perfil del administrador
    def botonRegistrarse(self):
        self.stackedWidget_principal.setCurrentIndex(3)#coloca en la ventana de registro
    def botonProxEvento(self):
        self.eliminar_widgets(self.verticalLayout_5)
        self.stackedWidget_principal.setCurrentIndex(2)#coloca en la ventana de proximo evento
        self.cargarEventos()
    def iniciarSesion(self):
        self.Usu_activo = correo=self.Correo_2.text()
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
                
    def habilitar_cambio_datos(self): 
        """Este metodo se encarga del proceso de cambar y guardar los datos de un Usuario"""
        self.Boton_EditarDatos.clicked.disconnect()
        self.Boton_EditarDatos.setText('Guardar Cambios')
        self.habilitar_o_deshabilitarDatos(False)
        self.guardarCambioDatos()
        return None
        
    def habilitar_o_deshabilitarDatos(self,b): ## Habilita o deshabilita los datos del stackedWidget Nro 4
        """Recibe un booleano y habilita(True) o deshabilita(False) los lineedits del stackedWidget Nro 4"""
        self.perfil_nombre.setReadOnly(b)
        self.perfil_correo.setReadOnly(b)
        self.perfil_apellido.setReadOnly(b)
        self.perfil_cedula.setReadOnly(b)
        self.visible_us()
                
    def guardarCambioDatos(self):
        ##tipoU = self.Line_tipoUsuario.text()
        self.Boton_EditarDatos.clicked.connect(lambda: self.obtenerDatos())     
        
    def obtenerDatos(self):
        self.Boton_EditarDatos.setText('Editar Datos')
        nombre = self.perfil_nombre.text()
        cc = self.perfil_cedula.text()
        apellido = self.perfil_apellido.text()
        correo = self.perfil_correo.text()
        lis = [cc,nombre,apellido,correo]
        if self.db.incertar_datos(self.Usu_activo,lis) == False:
            self.mensaje.setText('¡Correo o Cedula ya existen!\n Ingrese otros datos por favor')
            self.mensaje.exec_()
            self.limpiar_lineedits()
            self.Boton_EditarDatos.clicked.disconnect()
            self.habilitar_o_deshabilitarDatos(True)
            self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())
        else: 
            self.mensaje.setText('¡Los cambios se hicieron con exito!')
            self.mensaje.exec()
            self.cambiar_correo(correo)
            self.limpiar_lineedits()
            self.habilitar_o_deshabilitarDatos(True)
            self.Boton_EditarDatos.clicked.disconnect()
            self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())
            
    def cambiar_correo(self,correo):
        if correo != '':
            self.Usu_activo = correo
        
        
        # SE ACTUALIZA EL CORREO EN LA VARIABLE SELF.USU_ACTIVO
        
    def visible_us(self): # HACE VISIBLE LOS DATOS DEL stackedWidget Nro 4
        us = self.db.CosultarDatosU(self.Usu_activo)[0]
        self.Line_tipoUsuario.setPlaceholderText(self.db.tipoUsuario(us[2]))
        self.perfil_nombre.setPlaceholderText(us[3])
        self.perfil_cedula.setPlaceholderText(str(us[0]))
        self.perfil_apellido.setPlaceholderText(us[4])
        self.perfil_correo.setPlaceholderText(us[5])
        
        
    def abrir_dialogo_archivo(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.DontUseNativeDialog
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de imagen (*.png *.jpg *.jpeg *.gif);;Todos los archivos (*)", options=opciones)
        if archivo:
            print("Archivo seleccionado:", archivo)
            self.agregarFotoPerfil(archivo)
            self.db.rutaFotoUsuario(self.Usu_activo,archivo)
            
    def agregarFotoPerfil(self,ruta):
        foto = QPixmap(os.path.join(ruta))
        self.Foto_usuario.setPixmap(foto)
        
    def cargarFotoPerfil(self):
        us = self.db.CosultarDatosU(self.Usu_activo)
        if us[0][7] is not None:
            ruta = str(us[0][7])
            ruta = self.db.convertirByteaIMG(us[0][7],self.Usu_activo)
            self.agregarFotoPerfil(ruta)
            
    def cargarEventos(self):
       eventos=self.db.cargarEventos()
       i=0
       for evento in eventos:
           fecha=evento[0]
           item=FrameEvento(fecha)
           self.verticalLayout_5.insertWidget(i,item)
           i+=1
        
    def eliminar_widgets(self,layout):
        while layout.count() > 1:  # Deja al menos un widget en el layout
            widget = layout.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()
        
        
    def cerrar_sesion(self):
        self.tipo_usuario = 0
        self.Usu_activo = 0
        self.stackedWidget_principal.setCurrentIndex(0)
        self.Boton_ingresar.setText('INICIAR SESIÓN')
        pass        
            
    def perfilAdministrador(self):
        ## Aqui se establece la fecha minima 
        self.fechaEvento.setCalendarPopup(True)
        self.fechaEvento.setMinimumDate(QDate().currentDate())
        # Establecer la hora mínima a las 7 de la mañana
        self.inicioEvento.setMinimumTime(QTime(7, 0))
        # Establecer la hora maxima a las 8 de la noche 
        self.inicioEvento.setMaximumTime(QTime(20,0))
        # Se establece la hora minima para el final
        self.finEvento.setMinimumTime(QTime(7,20))
        # Se establece la hora maxima para la finalizacion del evento
        self.finEvento.setMaximumTime(QTime(21,0))
        # Se conecta el botón con la función guardar evento 
        self.Boton_guardarEvento.clicked.connect(lambda:self.guardarEvento())
        # Conectar el ComboBox con la lista de coordinadores
        corr = self.db.listaCoordinadores()
        self.combo_coordinadores.addItem('')
        for cor in corr:
            dat = f'{cor[0]}'+' '+cor[1]+' '+cor[2]
            self.combo_coordinadores.addItem(dat)
            
        # Conectar el botón guardar con el metodo
        self.Boton_guardarEvento.clicked.disconnect()
        self.Boton_guardarEvento.clicked.connect(lambda:self.guardarEvento())        
    
    def guardarEvento(self):
        nomevento = self.tituloEvento.text()
        encargado = self.combo_coordinadores.currentText().split(' ',1)
        fech = self.fechaEvento.date().toString("dd/MM/yyyy")# Esta linea recupera la fecha como QDate y la transforma en string 
        horainicio = self.inicioEvento.time().toString("h:mm AP")# Me devuelve la hora del evento en formato 'am' y 'pm'
        horafin = self.finEvento.time().toString("h:mm AP")
        descripcion = self.descripcionEvento.toPlainText()# Me devuelve el texto de la descripcion del evento
        encargado = self.validarDatosEvento(nomevento,encargado,horainicio,horafin) # Devuelve el nombre del coordinador como cadena de texto
        if encargado is not False: # Aqui se verifica si se cumple la condición de que todos los datos estan en orden
            # Se procede a guardar los datos 
            horaEvento = f'{horainicio}-{horafin}'
            self.db.guardar_evento(nomevento,fech,encargado,descripcion,horaEvento)
            self.mensaje.setText('¡El evento se guardo con exito!')
            self.mensaje.exec_()
            pass
        print(nomevento,encargado,fech,horainicio,horafin,descripcion)
    
    
    def validarDatosEvento(self,nomevento,encargado,horainicio,horafin):
        b = False
        # Validamos que el nomevento y el encargado no esten vacios
        if nomevento == '':
            self.mensaje.setText("¡El Título del evento es obligatorio!")
            self.mensaje.exec_()
            self.Boton_guardarEvento.clicked.disconnect()
            self.Boton_guardarEvento.clicked.connect(lambda:self.perfilAdministrador())
        elif encargado == '':
            self.mensaje.setText("¡El encargado del evento es obligatorio!")
            self.mensaje.exec_()
            self.Boton_guardarEvento.clicked.disconnect()
            self.Boton_guardarEvento.clicked.connect(lambda:self.perfilAdministrador())

        else: b = encargado[1]
            
        # Validamos que la hora de inicio no sea mayor o igual que la hora final
        inicio = QTime().fromString(horainicio,"h:mm AP")
        fin = QTime().fromString(horafin,"h:mm AP")
        if inicio >= fin:
            self.mensaje.setText("Horas incorrectas. Ingreselas de nuevo")
            self.mensaje.exec_()
            
        return b
        
    def mostrarTablaUsuarios(self):
        self.stackedWidget_admin.setCurrentIndex(1)
        
    def mostrarPaginaAdministrareventos(self):
        self.stackedWidget_admin.setCurrentIndex(0)
    
if __name__ == '__main__':#crea la ventana
    app = QApplication(sys.argv)
    window=MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
