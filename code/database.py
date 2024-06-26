#importacion del modulo
import psycopg2,os
class DataBase():
    def __init__(self) -> None:
        # Conexion a base de datos
        self.conn = psycopg2.connect(user='postgres',host='127.0.0.1', password =  'POSTGRES1',port='5432', database='db_Simes')
        # Utilizar cursor
        self.cur = self.conn.cursor()

    def __del__(self):
        # Cerrar el cursor y la conexión
        self.cur.close()
        self.conn.close()

    
    def isExist(self, tabla, col, datos):
        consulta = f'SELECT COUNT(*) FROM {tabla} WHERE {col}{tabla[:-1]} = %s'
        self.cur.execute(consulta, (datos,))
        resultado = self.cur.fetchone()[0]
        return resultado > 0
    
    def consultarTipoU(self, correo):
        consulta = 'SELECT tipousuario FROM usuarios WHERE correousuario = %s'
        self.cur.execute(consulta, (correo,))
        resultado=self.cur.fetchone()[0]
        return resultado

    def registarUsuario(self, nombre,tipocc,cedula,apellido,correo,contra):
        
        consulta = '''INSERT INTO usuarios (idusuario,tipoid,tipousuario,nomusuario,apeusuario,correousuario,contrausuario) 
              VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        datos=(cedula,tipocc,3,nombre.capitalize(),apellido.capitalize(),correo.lower(),contra)
        self.cur.execute(consulta,datos)
        self.conn.commit()
        
    def CosultarDatosU(self,correo):
        """Retorna todo el registro del usuario y lo sonsulta por el correo"""
        consulta = 'select * from usuarios where correousuario = %s'
        self.cur.execute(consulta,(correo,))
        us = self.cur.fetchall()
        return us
    
    def consultarPorcedula(self,cedula):
        """Retorna todo el registro del usuario y lo sonsulta por el correo"""
        consulta = 'select * from usuarios where idusuario = %s'
        self.cur.execute(consulta,(cedula,))
        us = self.cur.fetchall()
        return us
    
    def tipoUsuario(self,tipo): 
        """Clasifica el tipo usuario en un strig 1 = "administrador", 2 = "Coordinador" 3 = "Visitante" """
        tipo = int(tipo)
        match tipo:
            case  1:
                return 'Administrador'
            case 2:
                return 'Coordinador'
            case 3:
                return 'Visitante'
            
    def buscarRegistros(self,cc = 0,correo = 0):
        """Busca el registro del usuario por idusuario y su correo, retornando una lista con el numero de registros en la base de datos"""

        lis2 = []
        if cc != '':
            con = f"select count(*) from usuarios where idusuario = '{cc}'"
            self.cur.execute(con)
            conteo = self.cur.fetchall()
            lis2.append(int(conteo[0][0]))
        else:lis2.append(0)

        con = f"select count(*) from usuarios where correousuario = '{correo}'"
        self.cur.execute(con)
        conteo = self.cur.fetchall()
        lis2.append(int(conteo[0][0]))
        return lis2
        

    def incertar_datos(self,correo,lista_datos):
        """Metodo para cambiar los datos del usuario en la base de datos"""
        b = True
        # VALIDAR QUE EL CORREO Y LA CEDULA SON UNICAS
        if self.validarCedula(lista_datos[0],correo=correo): 
            if self.validarCorreo(lista_datos[3],correo):
                registros = self.buscarRegistros(lista_datos[0],lista_datos[3])
                atributos = ['idusuario','nomusuario','apeusuario','correousuario']
                if registros[0]<=1 and registros[1]<=1:
                    for i in range(len(lista_datos)):
                        if lista_datos[i] != '':
                            con = f"""UPDATE usuarios SET {atributos[i]} = '{lista_datos[i]}' WHERE correousuario = '{correo}'"""
                            self.cur.execute(con)
                            self.conn.commit()     
                else: 
                    b = False
            else:b = False
        else : b = False
        return b
    
    def validarCedula(self,cedula,correo):
        registro = []
        b = True
        if cedula != '':
            con = f"""select * from usuarios where idusuario = '{cedula}'"""
            self.cur.execute(con)
            r = self.cur.fetchall()
            try:
                registro.append(r[0])
                if registro[0][5] != None and registro[0][5] != correo:
                    b = False
            except IndexError:pass
        return b
    
    def validarCorreo(self,correoN,correoV):
        registro = []
        b = True
        try:
            if correoN != '':
                con = f"""select * from usuarios where correousuario = '{correoV}'"""
                self.cur.execute(con)
                registro.append(self.cur.fetchall()[0])
                con = f"""select * from usuarios where correousuario = '{correoN}'"""
                self.cur.execute(con)
                registro.append(self.cur.fetchall()[0])
                if registro[0][0] != registro[1][0]:
                    b = False
        except IndexError: pass
        return b

    def rutaFotoUsuario(self,correo,ruta):
        ruta = self.imgBite(ruta)
        d = (ruta,correo)
        con = f"""UPDATE usuarios SET fotousuario = %s WHERE correousuario = %s"""
        self.cur.execute(con,d)
        self.conn.commit()
        
    def imgBite(self,ruta):
        with open(ruta,'rb') as img:
            ima = img.read()
            return ima
    
    def convertirByteaIMG(self,ruta,correo):
        ruta = bytes(ruta)
        id = self.CosultarDatosU(correo)[0][0]
        rutaFoto = os.path.dirname(os.path.dirname(__file__))+f'\\imgsperfil\\img{id}.jpg'
        with open(rutaFoto,'wb') as img:
            img.write(ruta)
            img.close()
        return rutaFoto
    
    def listaCoordinadores(self,conCorreo=None):
        if conCorreo == None:
            """Retorna la lista de Coordinadores"""
            consulta = f"""select idusuario,nomusuario,apeusuario from usuarios where tipousuario = '2' and estado_usuario = 'A'"""
            self.cur.execute(consulta)
            coordinadores = self.cur.fetchall()
        else:
            """Retorna la lista de Coordinadores"""
            consulta = f"""select tipousuario,nomusuario,apeusuario,correousuario,fotousuario,estado_usuario from usuarios where tipousuario = '2'"""
            self.cur.execute(consulta)
            coordinadores = self.cur.fetchall()            
        return coordinadores
    
    def cargarEventos(self):
        consulta =f'select distinct fechevento from eventos'
        self.cur.execute(consulta)
        evento = self.cur.fetchall()
        return evento
    
    def consultarEventosUsuario(self,cedula):
        consulta =f'select distinct fechevento from eventos join registro_eventos on eventos.idevento=registro_eventos.idevento where idusuario = %s'
        self.cur.execute(consulta,(cedula,))
        evento = self.cur.fetchall()
        return evento
    
    
    
    def consultarHoras(self,fecha):
        consulta=f'select idevento,horaevento,descripcionevento,nomevento from eventos where fechevento = %s'
        self.cur.execute(consulta,(fecha,))
        horas=self.cur.fetchall()
        return horas
      
    
    def guardar_evento(self,nomevento,fechevento,encargadoevento,descripcionevento,horaevento): 
        consulta =f"""insert into eventos (nomevento,fechevento,encargadoevento,descripcionevento,horaevento) values (%s,%s,%s,%s,%s)"""
        datos = (nomevento,fechevento,encargadoevento,descripcionevento,horaevento)
        self.cur.execute(consulta,datos)
        self.conn.commit()
        
    def cambio_contraseña(self,con):
        tup = (con,)
        cons = f"""select count(*) from usuarios where contrausuario = %s"""
        self.cur.execute(cons,tup)
        con = self.cur.fetchone()[0]
        return con
        
    def nueva_con(self,con,correo):
        tup = (con,correo)
        cons = f"""update usuarios set contrausuario = %s where correousuario = %s"""
        self.cur.execute(cons,tup)
        self.conn.commit()
        
    def incertar_Coordinador(self,remplazo,cc,nom,apellido,correo,contra,tpid):
        tup = (cc,tpid,2,nom,apellido,correo,contra,self.fotoCoordinador)
        
        if remplazo:# Si el coordinador ya tenia una cuenta previa como usuario esta se remplaza como cuenta del coordinador
            insert = f"""update usuarios set idusuario = %s,
            tipoid = %s, tipousuario = %s, nomusuario = %s, apeusuario = %s, correousuario = %s, contrausuario = %s, fotousuario = %s
            where idusuario = '{cc}' or correousuario = '{correo}'"""
            self.cur.execute(insert,tup)
            self.conn.commit()
        else:# Si el coordinador no tiene una cuenta previa esta se crea en la base de datos
            insert = f"""insert into usuarios values (%s,%s,%s,%s,%s,%s,%s,%s)"""
            self.cur.execute(insert,tup)
            self.conn.commit()
        
    def Perfil_cordinador(self,foto = None):
        self.fotoCoordinador = foto
        
    
    def registrarEvento(self,usuario,evento):
        consulta =f'insert into registro_eventos (idusuario, idevento) values (%s,%s)'
        self.cur.execute(consulta,(usuario,evento,))
        self.conn.commit()
    
    def consultarCedula(self,correo):
        consulta =f'select idusuario from usuarios where correousuario = %s '
        self.cur.execute(consulta,(correo,))
        cedula=self.cur.fetchone()[0]
        return cedula
    
    def consultarRegistro(self,usuario,evento):
        consulta = f'select count(*) from registro_eventos where idusuario = %s and idevento = %s'
        self.cur.execute(consulta,(usuario,evento,))
        cedula=self.cur.fetchone()[0]
        return cedula>0
    def eliminarRegistro(self,usuario,evento):
        consulta =f'delete from registro_eventos where idusuario = %s and idevento = %s'
        self.cur.execute(consulta,(usuario,evento,))
        self.conn.commit()
    def consultarRegistros(self,usuario):
        consulta = f'select * from registro_eventos where idusuario = %s'
        self.cur.execute(consulta,(usuario,))
        resultado=self.cur.fetchall()
        return resultado
    def consultarusuarioRegistro(self,usuario):
        consulta = f'select count(*) from registro_eventos where idusuario = %s'
        self.cur.execute(consulta,(usuario,))
        cedula=self.cur.fetchone()[0]
        return cedula>0
    
    def guardar_informe(self, asunto, texto, encargado):
        tup = (asunto,texto,encargado)
        consulta = f"""insert into informes (asunto,descrip_informe,encargado) values (%s,%s,%s)""" 
        self.cur.execute(consulta,tup)
        self.conn.commit()
        
    def desactivar_Usuario(self,correo):# Metodo para desactivar un usuario
        consulta = f"""update usuarios set estado_usuario = 'B' where correousuario = '{correo}'"""
        self.cur.execute(consulta)
        self.conn.commit()
        
    def consultar_actividadPerfil(self,correo):
        """Me dice si el usuario tiene una cuenta activa o si ya fue desactivada"""
        consulta = f"""select estado_usuario from usuarios where correousuario = '{correo}'"""
        self.cur.execute(consulta)
        estado = self.cur.fetchall()[0][0]
        if estado == 'A':
            return True
        else: return False
        
    def eliminar_usuario(self,correo):
        consulta = f"""delete from usuarios where correousuario = '{correo}'"""
        self.cur.execute(consulta)
        self.conn.commit()
        
    def lisEventos(self):
        consulta = f"""select idevento,fechevento,horaevento,descripcionevento,nomevento,estado_evento from eventos"""
        self.cur.execute(consulta)
        registros = self.cur.fetchall()
        return registros
    
    def cambiar_estadoEvento(self, estado, idevento):
        """Para cambiar el estado del evento resive como parametro (i,a,e) o (I,A,E) para 
        inhabilitado, habilitado, en espera; correspondientemente, y el id del evento"""
        consulta = None
        if estado == 'e' or estado == 'E':
            consulta = f"""update eventos set estado_evento = 'E' where idevento = '{idevento}'"""
            
        elif estado == 'I' or estado == 'i':
            consulta = f"""update eventos set estado_evento = 'I' where idevento = '{idevento}'"""
        else:
            consulta = f"""update eventos set estado_evento = 'A' where idevento = '{idevento}'"""
        self.cur.execute(consulta)
        self.conn.commit()
    
    def consultardatosinforme(self):
        consulta= f'select nomusuario,apeusuario, asunto, descrip_informe from informes join usuarios on encargado=idusuario '
        self.cur.execute(consulta)
        resultado=self.cur.fetchall()
        return resultado

    def consultarContraseña(self,usuario):
        consulta = f'select contrausuario from usuarios where idusuario=%s'
        self.cur.execute(consulta,(usuario,))
        resultado=self.cur.fetchone()[0]
        return resultado
    
    def eliminar_usuario2(self,usuario):
        consulta = f'delete from usuarios where idusuario=%s'
        self.cur.execute(consulta,(usuario,))
        self.conn.commit()

        
        