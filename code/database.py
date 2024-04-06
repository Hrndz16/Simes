#importacion del modulo
import psycopg2
class DataBase():
    def __init__(self) -> None:
        # Conexion a base de datos
        self.conn = psycopg2.connect(user='postgres',password = 'POSTGRES1',host='127.0.0.1', port='5432', database='db_Simes')
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
            
        