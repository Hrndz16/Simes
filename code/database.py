#importacion del modulo
import psycopg2,os
class DataBase():
    def __init__(self) -> None:
        # Conexion a base de datos
        self.conn = psycopg2.connect(user='postgres',host='127.0.0.1', port='5432', database='db_Simes')
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
        print(ruta)
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
    
    def listaCoordinadores(self):
        """Retorna la lista de Coordinadores"""
        consulta = f"""select idusuario,nomusuario,apeusuario from usuarios where tipousuario = '2'"""
        self.cur.execute(consulta)
        coordinadores = self.cur.fetchall()
        return coordinadores
    
    def cargarEventos(self):
        consulta =f'select distinct fechevento from eventos'
        self.cur.execute(consulta)
        evento = self.cur.fetchall()
        return evento
    
    
    
    def consultarHoras(self,fecha):
        consulta=f'select idevento,horaevento,descripcionevento,nomevento from eventos where fechevento = %s'
        self.cur.execute(consulta,(fecha,))
        horas=self.cur.fetchall()
        return horas
      
# a=DataBase()
# evento=a.cargarEventos()
# print(type(evento[0][1]))
    
    def guardar_evento(self,nomevento,fechevento,encargadoevento,descripcionevento,horaevento):
        consulta =f"""insert into eventos (nomevento,fechevento,encargadoevento,descripcionevento,horaevento) values (%s,%s,%s,%s,%s)"""
        datos = (nomevento,fechevento,encargadoevento,descripcionevento,horaevento)
        self.cur.execute(consulta,datos)
        self.conn.commit()