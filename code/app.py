#Importaciones necesarias
import sys,os
ruta = os.path.dirname(os.path.dirname(__file__))
sys.path.append(f'{ruta}\\imgs')
from PySide6.QtWidgets import (QMainWindow,QApplication,QSpacerItem,
                               QMessageBox,QLineEdit,QFileDialog,
                               QSizePolicy,QDialog)
from Ui_mainwindow import Ui_MainWindow as MW
from PySide6.QtCore import Qt,QDate,QTime
from PySide6.QtGui import QFont,QPixmap
from eventos import FrameEvento
from database import DataBase
from Ui_nuevaContraseña import Ui_Dialog

class MainWindow(QMainWindow,MW):#Creacion de main Window
    def __init__(self):
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
        self.db=DataBase()
        self.tipo_usuario=0 #variable para saber que usuario esta activo acutalmente 0=Usuario sin cuenta 1=Administrador 2=Cordinador 3=Usuario con cuenta
        self.cedulaU = 0
        super().__init__()
        self.setupUi(self)#Carga el ui de qtdesigner
        self.stackedWidget_principal.setCurrentIndex(0)#pone la ventana principal
        self.Boton_ingresar.clicked.connect(lambda:self.botonIngresar())#configura el boton de inicio de sesion
        self.Boton_inicio.clicked.connect(lambda:self.botonInicio())#configura el boton de inicio(home)
        self.Registrarse.clicked.connect(lambda:self.botonRegistrarse())#configura el boton de Registarse
        self.Bonton_proxEvento.clicked.connect(lambda:self.botonProxEvento())#configura el boton de proximo evento
        self.acceder_2.clicked.connect(lambda:self.iniciarSesion())
        self.acceder.clicked.connect(lambda:self.RegistrarUsuario())

        self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())#habilita el cambio de datos de perfil del usuario
        self.Boton_CambiarFoto.clicked.connect(lambda:self.abrir_dialogo_archivo())
        self.Boto_cerrarsesion.clicked.connect(lambda:self.cerrar_sesion())
        self.fechaEvento.setCalendarPopup(True)
        self.Boton_adminEventos.clicked.connect(lambda:self.stackedWidget_admin.setCurrentIndex(0)) # En la pagina del administrador muestra la pagina de los eventos 
        self.Boton_cambiarContra.clicked.connect(lambda: self.cambiar_contraseña())# me conecta con el dialog de cambiar la contraseña
        self.Boton_ElaborarInforme.clicked.connect(lambda:self.stackedWidget_admin.setCurrentIndex(1))
        self.Boton_CoorEventos.clicked.connect(lambda:self.stackedWidget_admin.setCurrentIndex(0))
        self.boton_appendCoordinador.clicked.connect(lambda:self.stackedWidget_admin.setCurrentIndex(2))
        self.boton_CrearCoodinador.clicked.connect(lambda:self.crear_CuentaCoordinador())
        self.Boton_CambiarFoto_2.clicked.connect(lambda:self.agregarFotoCoodinador())
        self.Boton_objetos.clicked.connect(lambda:self.crear_LE())
        self.boton_prox_ev_LE.clicked.connect(lambda:self.botonProxEvento())
        self.Boton_adminUsuarios.clicked.connect(lambda:self.mostrar_coordinadores())        
        
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
        elif self.tipo_usuario == 1:
            self.stackedWidget_principal.setCurrentIndex(6)
            self.stackedWidget_admin.setCurrentIndex(0) # Lo posiciona en el stackedWidget de crear un evento
            self.stackedWidget_MenuAdCor.setCurrentIndex(0)# Lo posisiona en el menu del administrador
            self.perfilAdministrador()# Aqui se inicializa la interfaz del perfil del administrador
        else:
            self.stackedWidget_principal.setCurrentIndex(6)
            self.stackedWidget_admin.setCurrentIndex(0) 
            self.stackedWidget_MenuAdCor.setCurrentIndex(1)
            self.perfilAdministrador()# Aqui se inicializa la interfaz del perfil del administrador
            
    def botonRegistrarse(self):
        self.stackedWidget_principal.setCurrentIndex(3)#coloca en la ventana de registro
    def botonProxEvento(self):
        self.eliminar_widgets(self.verticalLayout_5,1)
        self.stackedWidget_principal.setCurrentIndex(2)#coloca en la ventana de proximo evento
        self.cargarEventos()
    def iniciarSesion(self):
        self.Usu_activo = correo=self.Correo_2.text()
        contraseña=self.password_2.text()
        
        if self.db.isExist('usuarios','correo',correo) and self.db.isExist('usuarios','contra',contraseña):
            self.tipo_usuario = self.db.consultarTipoU(correo)
            self.cedulaU=self.db.consultarCedula(correo)
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
        apellido=self.Apellido.text()
        correo=self.Correo.text()
        contra=self.password.text()
        cc=self.Cedula.text()
        lis = [cc,contra,nombre,tipoCC,apellido,correo]
        try:
            if bool(self.verificar_valoresObligatorios(lis)) == True:
                cc=int(cc) #Valida si la cedula es un entero
                self.guardarRegistrousuario(cc=cc,correo=correo,tipoCC=tipoCC,nombre=nombre,apellido=apellido,contra=contra)# Se validan los datos y se guarda el registro
            else: self.Box_mensaje('¡¡¡Todos los datos son obligatorios!!!')
        except ValueError:
            self.Box_mensaje('¡¡¡La cedula debe de ser un número!!!')
            self.Cedula.clear()
            pass
        
    def verificar_valoresObligatorios(self,lis):
        '''Me ayuda a comprobar que todos los datos en el registro de un nuevo usuario tengan algun valor'''
        b = True
        for line in lis:
            if line == '':
                b = False
                break
        return b
    
    def Box_mensaje(self,mensaje):
        '''Recibe un string y me arroja un mensaje en pantalla'''
        self.mensaje.setText(mensaje)
        self.mensaje.exec_()
        
    def guardarRegistrousuario(self,cc,correo,nombre,tipoCC,apellido,contra):
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
     
    def habilitar_o_deshabilitarDatos(self,b): ## Habilita o deshabilita los datos del stackedWidget Nro 4
        """Recibe un booleano y habilita(True) o deshabilita(False) los lineedits del stackedWidget Nro 4"""
        self.perfil_nombre.setReadOnly(b)
        self.perfil_correo.setReadOnly(b)
        self.perfil_apellido.setReadOnly(b)
        self.perfil_cedula.setReadOnly(b)
        self.visible_us() 
                
    def habilitar_cambio_datos(self): 
        """Este metodo se encarga del proceso de cambar y guardar los datos de un Usuario"""
        self.Boton_EditarDatos.clicked.disconnect()
        self.Boton_EditarDatos.setText('Guardar Cambios')
        self.habilitar_o_deshabilitarDatos(False)
        self.guardarCambioDatos()
        return None
        
                
    def guardarCambioDatos(self):
        ##tipoU = self.Line_tipoUsuario.text()
        self.Boton_EditarDatos.clicked.connect(lambda: self.obtenerDatos())     
        
    def obtenerDatos(self):
        self.Boton_EditarDatos.setText('Editar Datos')
        nombre = self.perfil_nombre.text()
        self.cedulaU = cc = self.perfil_cedula.text()
        apellido = self.perfil_apellido.text()
        correo = self.perfil_correo.text()
        cc = self.perfil_cedula.text()
        try:
            if cc != '':
                cc = int(cc)
            lis = [cc,nombre,apellido,correo]
            self.cambiar_datos(lis,correo)
        except ValueError: 
            self.Box_mensaje('¡La cedula debe de ser un número!')
            self.perfil_cedula.clear()
            self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())
        
    def cambiar_datos(self,lis,correo):#Este metodo termina de evaluar los datos y los guarda en el caso de que todo este correcto
        if self.verificar_none(lis):
            self.mensaje.setText('Casillas vacias')
            self.mensaje.exec_()
            self.Boton_EditarDatos.clicked.disconnect()
            self.habilitar_o_deshabilitarDatos(True)
            self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())
        elif self.db.incertar_datos(self.Usu_activo,lis) == False:
            self.mensaje.setText('¡Correo o Cedula ya existen!\nIngrese otros datos por favor')
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
            
    def verificar_none(self,lis):
        b = True
        for i in lis:
            if i is not None:
                b = False
                return b
    
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
            
    def agregarFotoCoodinador(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.DontUseNativeDialog
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de imagen (*.png *.jpg *.jpeg *.gif);;Todos los archivos (*)", options=opciones)
        if archivo:
            self.agregarFotoPerfilCoordinador(archivo)
            self.db.Perfil_cordinador(archivo)
            
    def agregarFotoPerfilCoordinador(self,ruta):
        foto = QPixmap(os.path.join(ruta))
        self.Foto_usuario_2.setPixmap(foto)
            
    def cargarEventos(self):
        eventos = self.db.cargarEventos()
        i = 0
        for evento in eventos:
            fecha = evento[0]
            item = FrameEvento(fecha, self.cedulaU)
            self.verticalLayout_5.insertWidget(i, item)
            i += 1
            

        

            
    def eliminar_widgets(self,layout,deja):
        while layout.count() > deja:  # Deja al menos un widget en el layout
            widget = layout.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()
        
        
    def cerrar_sesion(self):
        self.tipo_usuario = 0
        self.Usu_activo = 0
        self.cedulaU = 0
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
        
    def cambiar_contraseña(self):
        # Crear una instancia del diálogo
        self.dialog = QDialog()

        # Crear una instancia de la interfaz de usuario del diálogo
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.pushButton.clicked.connect(lambda:self.validarNuevacontraseña())
        self.ocultar_lines()## OCULTA LAS LOS VALORES DE LOS LINE EDITS
        self.ui.pushButton_2.pressed.connect(lambda:self.mostrar_lines()) # SE MUESTRAN LOS VALORES DE LOS LINE EDITS
        self.ui.pushButton_2.released.connect(lambda:self.ocultar_lines())

        # Mostrar el diálogo
        self.dialog.show()     
        
    def ocultar_lines(self):  
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_3.setEchoMode(QLineEdit.Password)
        
    def mostrar_lines(self):
        self.ui.lineEdit.setEchoMode(QLineEdit.Normal)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.ui.lineEdit_3.setEchoMode(QLineEdit.Normal)
    
    def validarNuevacontraseña(self):# En este metodo se validan todas la entradas para el cambio de contraseña
        
        Vcon = self.ui.lineEdit.text()
        Ncon = self.ui.lineEdit_2.text()
        Ncon2 = self.ui.lineEdit_3.text()
        if self.db.cambio_contraseña(Vcon) > 0:
            if Ncon == Ncon2:
                if Vcon != Ncon:
                    self.db.nueva_con(Ncon,self.Usu_activo)
                    self.mensaje.setText("Su cambio de contraseña se hizo con exito")
                    self.mensaje.exec_()
                else:
                    self.mensaje.setText("La nueva contraseña no puede ser igual a al anterior ")
                    self.mensaje.exec_()
            else:
                self.mensaje.setText("Contraseñar ")
                self.mensaje.exec_()
        else:
            self.mensaje.setText("Contraseña incorrecta")
            self.mensaje.exec_()
            
    def crear_CuentaCoordinador(self): 
        """Main para las funciones necesarias para crear el perfil del cordinador"""
        nombre = self.Nombre_Coordinador.text()
        apellido = self.Apellido_Coordinador.text()
        correo = self.Correo_Coordinador.text()
        cc = self.Cedula_Coordinador.text()
        contra = self.password_Coordinador.text()
        tpid = self.tipId_coordinador.currentText()
        # if cc != '':
        #         cc = int(cc)
        # lis = [cc,nombre,apellido,correo,contra,tpid]
        # self.datos_cuentaCoordinador(lis,correo,cc)
        try:
            if cc != '':
                cc = int(cc)
            lis = [cc,nombre,apellido,correo,contra,tpid]
            self.datos_cuentaCoordinador(lis,correo,cc)
        except ValueError: 
            self.Box_mensaje('¡La cedula debe de ser un número!')
            self.Cedula_Coordinador.clear()
        
    def datos_cuentaCoordinador(self,lis,correo,cc):#Este metodo termina de evaluar los datos y los guarda en el caso de que todo este correcto
        self.db.Perfil_cordinador()      
        if self.verificar_valoresObligatorios(lis) == False:
            self.mensaje.setText('¡Todos los datos son obligatorios!')
            self.mensaje.exec_()
        else:
            Cr = self.db.consultarPorcedula(cc)
            Concrr = self.db.CosultarDatosU(correo)
            if  Cr == [] and Concrr == []:
                self.db.incertar_Coordinador(False,lis[0],lis[1],lis[2],lis[3],lis[4],lis[5])
                self.Box_mensaje('Se creo un nuevo coordinador')
                self.limpiar_lineedits()
            else:
                if Cr[0] == Concrr[0]:
                    self.db.incertar_Coordinador(True,lis[0],lis[1],lis[2],lis[3],lis[4],lis[5])
                    self.Box_mensaje(f'EL usuario {Cr[0][3]} {Cr[0][4]} se ascendio a Coordinador')
                    self.limpiar_lineedits()
                else:
                    men = f"""El usuario coincide con dos registros\n1. CC:{Cr[0][0]} {Cr[0][3]} {Cr[4]} correo: {Cr[0][5]}
                    \n2.  CC:{Concrr[0][0]} {Concrr[0][3]} {Concrr[0][4]} correo: {Concrr[0][5]}
                    \nPara solucionarlo ingrese cedula y correo no reigistrados
                    \no elimine las cuentas que no le parecen necesarias en la seccion de
                    \nAdministrar usuarios"""
                    self.Box_mensaje(men)
    
    def crear_LE(self):
        self.eliminar_widgets(self.verticalLayout_12,2)
        self.stackedWidget_principal.setCurrentIndex(7)
        eventos = self.db.consultarEventosUsuario(self.cedulaU)
        i = 0
        if len(eventos)>0:
            
            self.label_lista_eventos.setVisible(False)
            for evento in eventos:
                fecha = evento[0]
                item = FrameEvento(fecha, self.cedulaU)
                self.verticalLayout_12.insertWidget(i, item)
                i += 1
        else:
            self.label_lista_eventos.setVisible(True)
        
        
                         
if __name__ == '__main__':#crea la ventana
    app = QApplication(sys.argv)
    window=MainWindow()
    window.showMaximized()
    sys.exit(app.exec()) 

#Importaciones necesarias
import sys,os
ruta = os.path.dirname(os.path.dirname(__file__))
sys.path.append(f'{ruta}\\imgs')
from PySide6.QtWidgets import (QMainWindow,QApplication,QSpacerItem,
                               QMessageBox,QLineEdit,QFileDialog,
                               QSizePolicy,QDialog)
from Ui_mainwindow import Ui_MainWindow as MW
from PySide6.QtCore import Qt,QDate,QTime
from PySide6.QtGui import QFont,QPixmap
from eventos import FrameEvento
from database import DataBase
from Ui_nuevaContraseña import Ui_Dialog
from usuarios import FrameUsuario

class MainWindow(QMainWindow,MW):#Creacion de main Window
    def __init__(self):
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
        self.db=DataBase()
        self.tipo_usuario=0 #variable para saber que usuario esta activo acutalmente 0=Usuario sin cuenta 1=Administrador 2=Cordinador 3=Usuario con cuenta
        self.cedulaU = 0
        super().__init__()
        self.setupUi(self)#Carga el ui de qtdesigner
        self.stackedWidget_principal.setCurrentIndex(0)#pone la ventana principal
        self.Boton_ingresar.clicked.connect(lambda:self.botonIngresar())#configura el boton de inicio de sesion
        self.Boton_inicio.clicked.connect(lambda:self.botonInicio())#configura el boton de inicio(home)
        self.Registrarse.clicked.connect(lambda:self.botonRegistrarse())#configura el boton de Registarse
        self.Bonton_proxEvento.clicked.connect(lambda:self.botonProxEvento())#configura el boton de proximo evento
        self.acceder_2.clicked.connect(lambda:self.iniciarSesion())
        self.acceder.clicked.connect(lambda:self.RegistrarUsuario())

        self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())#habilita el cambio de datos de perfil del usuario
        self.Boton_CambiarFoto.clicked.connect(lambda:self.abrir_dialogo_archivo())
        self.Boto_cerrarsesion.clicked.connect(lambda:self.cerrar_sesion())
        self.fechaEvento.setCalendarPopup(True)
        self.Boton_adminEventos.clicked.connect(lambda:self.stackedWidget_admin.setCurrentIndex(0)) # En la pagina del administrador muestra la pagina de los eventos 
        self.Boton_cambiarContra.clicked.connect(lambda: self.cambiar_contraseña())# me conecta con el dialog de cambiar la contraseña
        self.Boton_ElaborarInforme.clicked.connect(lambda:self.stackedWidget_admin.setCurrentIndex(1))
        self.Boton_CoorEventos.clicked.connect(lambda:self.stackedWidget_admin.setCurrentIndex(0))
        self.boton_appendCoordinador.clicked.connect(lambda:self.stackedWidget_admin.setCurrentIndex(2))
        self.boton_CrearCoodinador.clicked.connect(lambda:self.crear_CuentaCoordinador())
        self.Boton_CambiarFoto_2.clicked.connect(lambda:self.agregarFotoCoodinador())
        self.Boton_enviarInforme.clicked.connect(lambda:self.guardar_informe())
        self.Boton_adminUsuarios.clicked.connect(lambda:self.mostrar_coordinadores())# Coloca al perfil del administrador en la lista de cordinadores
                
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
        elif self.tipo_usuario == 1:
            self.stackedWidget_principal.setCurrentIndex(6)
            self.stackedWidget_admin.setCurrentIndex(0) # Lo posiciona en el stackedWidget de crear un evento
            self.stackedWidget_MenuAdCor.setCurrentIndex(0)# Lo posisiona en el menu del administrador
            self.perfilAdministrador()# Aqui se inicializa la interfaz del perfil del administrador
        else:
            self.stackedWidget_principal.setCurrentIndex(6)
            self.stackedWidget_admin.setCurrentIndex(0) 
            self.stackedWidget_MenuAdCor.setCurrentIndex(1)
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
            self.cedulaU=self.db.consultarCedula(correo)
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
        apellido=self.Apellido.text()
        correo=self.Correo.text()
        contra=self.password.text()
        cc=self.Cedula.text()
        lis = [cc,contra,nombre,tipoCC,apellido,correo]
        try:
            if bool(self.verificar_valoresObligatorios(lis)) == True:
                cc=int(cc) #Valida si la cedula es un entero
                self.guardarRegistrousuario(cc=cc,correo=correo,tipoCC=tipoCC,nombre=nombre,apellido=apellido,contra=contra)# Se validan los datos y se guarda el registro
            else: self.Box_mensaje('¡¡¡Todos los datos son obligatorios!!!')
        except ValueError:
            self.Box_mensaje('¡¡¡La cedula debe de ser un número!!!')
            self.Cedula.clear()
            pass
        
    def verificar_valoresObligatorios(self,lis):
        '''Me ayuda a comprobar que todos los datos en el registro de un nuevo usuario tengan algun valor'''
        b = True
        for line in lis:
            if line == '':
                b = False
                break
        return b
    
    def Box_mensaje(self,mensaje):
        '''Recibe un string y me arroja un mensaje en pantalla'''
        self.mensaje.setText(mensaje)
        self.mensaje.exec_()
        
    def guardarRegistrousuario(self,cc,correo,nombre,tipoCC,apellido,contra):
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
     
    def habilitar_o_deshabilitarDatos(self,b): ## Habilita o deshabilita los datos del stackedWidget Nro 4
        """Recibe un booleano y habilita(True) o deshabilita(False) los lineedits del stackedWidget Nro 4"""
        self.perfil_nombre.setReadOnly(b)
        self.perfil_correo.setReadOnly(b)
        self.perfil_apellido.setReadOnly(b)
        self.perfil_cedula.setReadOnly(b)
        self.visible_us() 
                
    def habilitar_cambio_datos(self): 
        """Este metodo se encarga del proceso de cambar y guardar los datos de un Usuario"""
        self.Boton_EditarDatos.clicked.disconnect()
        self.Boton_EditarDatos.setText('Guardar Cambios')
        self.habilitar_o_deshabilitarDatos(False)
        self.guardarCambioDatos()
        return None
        
                
    def guardarCambioDatos(self):
        ##tipoU = self.Line_tipoUsuario.text()
        self.Boton_EditarDatos.clicked.connect(lambda: self.obtenerDatos())     
        
    def obtenerDatos(self):
        self.Boton_EditarDatos.setText('Editar Datos')
        nombre = self.perfil_nombre.text()
        self.cedulaU = cc = self.perfil_cedula.text()
        apellido = self.perfil_apellido.text()
        correo = self.perfil_correo.text()
        cc = self.perfil_cedula.text()
        try:
            if cc != '':
                cc = int(cc)
            lis = [cc,nombre,apellido,correo]
            self.cambiar_datos(lis,correo)
        except ValueError: 
            self.Box_mensaje('¡La cedula debe de ser un número!')
            self.perfil_cedula.clear()
            self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())
        
    def cambiar_datos(self,lis,correo):#Este metodo termina de evaluar los datos y los guarda en el caso de que todo este correcto
        if self.verificar_none(lis):
            self.mensaje.setText('Casillas vacias')
            self.mensaje.exec_()
            self.Boton_EditarDatos.clicked.disconnect()
            self.habilitar_o_deshabilitarDatos(True)
            self.Boton_EditarDatos.clicked.connect(lambda: self.habilitar_cambio_datos())
        elif self.db.incertar_datos(self.Usu_activo,lis) == False:
            self.mensaje.setText('¡Correo o Cedula ya existen!\nIngrese otros datos por favor')
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
            
    def verificar_none(self,lis):
        b = True
        for i in lis:
            if i is not None:
                b = False
                return b
    
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
            
    def agregarFotoCoodinador(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.DontUseNativeDialog
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de imagen (*.png *.jpg *.jpeg *.gif);;Todos los archivos (*)", options=opciones)
        if archivo:
            self.agregarFotoPerfilCoordinador(archivo)
            self.db.Perfil_cordinador(archivo)
            
    def agregarFotoPerfilCoordinador(self,ruta):
        foto = QPixmap(os.path.join(ruta))
        self.Foto_usuario_2.setPixmap(foto)
            
    def cargarEventos(self):
        eventos = self.db.cargarEventos()
        i = 0
        for evento in eventos:
            fecha = evento[0]
            item = FrameEvento(fecha, self.cedulaU)
            self.verticalLayout_5.insertWidget(i, item)
            i += 1
            
            
    def eliminar_widgets(self,layout):
        while layout.count() > 1:  # Deja al menos un widget en el layout
            widget = layout.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()
        
        
    def cerrar_sesion(self):
        self.tipo_usuario = 0
        self.Usu_activo = 0
        self.cedulaU = 0
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
        
    def cambiar_contraseña(self):
        # Crear una instancia del diálogo
        self.dialog = QDialog()

        # Crear una instancia de la interfaz de usuario del diálogo
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.pushButton.clicked.connect(lambda:self.validarNuevacontraseña())
        self.ocultar_lines()## OCULTA LAS LOS VALORES DE LOS LINE EDITS
        self.ui.pushButton_2.pressed.connect(lambda:self.mostrar_lines()) # SE MUESTRAN LOS VALORES DE LOS LINE EDITS
        self.ui.pushButton_2.released.connect(lambda:self.ocultar_lines())

        # Mostrar el diálogo
        self.dialog.show()     
        
    def ocultar_lines(self):  
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_3.setEchoMode(QLineEdit.Password)
        
    def mostrar_lines(self):
        self.ui.lineEdit.setEchoMode(QLineEdit.Normal)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.ui.lineEdit_3.setEchoMode(QLineEdit.Normal)
    
    def validarNuevacontraseña(self):# En este metodo se validan todas la entradas para el cambio de contraseña
        
        Vcon = self.ui.lineEdit.text()
        Ncon = self.ui.lineEdit_2.text()
        Ncon2 = self.ui.lineEdit_3.text()
        if self.db.cambio_contraseña(Vcon) > 0:
            if Ncon == Ncon2:
                if Vcon != Ncon:
                    self.db.nueva_con(Ncon,self.Usu_activo)
                    self.mensaje.setText("Su cambio de contraseña se hizo con exito")
                    self.mensaje.exec_()
                else:
                    self.mensaje.setText("La nueva contraseña no puede ser igual a al anterior ")
                    self.mensaje.exec_()
            else:
                self.mensaje.setText("Contraseñar ")
                self.mensaje.exec_()
        else:
            self.mensaje.setText("Contraseña incorrecta")
            self.mensaje.exec_()
            
    def crear_CuentaCoordinador(self): 
        """Main para las funciones necesarias para crear el perfil del cordinador"""
        nombre = self.Nombre_Coordinador.text()
        apellido = self.Apellido_Coordinador.text()
        correo = self.Correo_Coordinador.text()
        cc = self.Cedula_Coordinador.text()
        contra = self.password_Coordinador.text()
        tpid = self.tipId_coordinador.currentText()
        # if cc != '':
        #         cc = int(cc)
        # lis = [cc,nombre,apellido,correo,contra,tpid]
        # self.datos_cuentaCoordinador(lis,correo,cc)
        try:
            if cc != '':
                cc = int(cc)
            lis = [cc,nombre,apellido,correo,contra,tpid]
            self.datos_cuentaCoordinador(lis,correo,cc)
        except ValueError: 
            self.Box_mensaje('¡La cedula debe de ser un número!')
            self.Cedula_Coordinador.clear()
        
    def datos_cuentaCoordinador(self,lis,correo,cc):#Este metodo termina de evaluar los datos y los guarda en el caso de que todo este correcto
        self.db.Perfil_cordinador()      
        if self.verificar_valoresObligatorios(lis) == False:
            self.mensaje.setText('¡Todos los datos son obligatorios!')
            self.mensaje.exec_()
        else:
            Cr = self.db.consultarPorcedula(cc)
            Concrr = self.db.CosultarDatosU(correo)
            if  Cr == [] and Concrr == []:
                self.db.incertar_Coordinador(False,lis[0],lis[1],lis[2],lis[3],lis[4],lis[5])
                self.Box_mensaje('Se creo un nuevo coordinador')
                self.limpiar_lineedits()
            else:
                if Cr[0] == Concrr[0]:
                    self.db.incertar_Coordinador(True,lis[0],lis[1],lis[2],lis[3],lis[4],lis[5])
                    self.Box_mensaje(f'EL usuario {Cr[0][3]} {Cr[0][4]} se ascendio a Coordinador')
                    self.limpiar_lineedits()
                else:
                    men = f"""El usuario coincide con dos registros\n1. CC:{Cr[0][0]} {Cr[0][3]} {Cr[4]} correo: {Cr[0][5]}
                    \n2.  CC:{Concrr[0][0]} {Concrr[0][3]} {Concrr[0][4]} correo: {Concrr[0][5]}
                    \nPara solucionarlo ingrese cedula y correo no reigistrados
                    \no elimine las cuentas que no le parecen necesarias en la seccion de
                    \nAdministrar usuarios"""
                    self.Box_mensaje(men)
                         
    def guardar_informe(self):
        #1 se recopilan los datos en variables
        print('si llego') 
        asunto = self.AsuntoEvento.text()
        texto = self.textoInforme.toPlainText()
        encargado = self.Usu_activo
        if asunto != '' and texto != '':
            self.db.guardar_informe(asunto,texto,encargado)
            self.Box_mensaje('¡Se envio con exito!')
        else:
            self.Box_mensaje('¡En el informe todos los datos son necesarios!')
            
    def mostrar_coordinadores(self):
        self.stackedWidget_admin.setCurrentIndex(3)
        lis_coordinadores = self.db.listaCoordinadores('Si')
        print(lis_coordinadores)
        i = 0
        if lis_coordinadores != []:
            for registro in lis_coordinadores:
                item = FrameUsuario(registro[0],registro[1],registro[2],registro[3],registro[4])
                self.verticalLayout_Lis_Coordinadores.insertWidget(i,item)
                i = i + 1
            
            
if __name__ == '__main__':#crea la ventana
    app = QApplication(sys.argv)
    window=MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
