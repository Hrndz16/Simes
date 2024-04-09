#importacion del modulo
import psycopg2
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
            
    def buscarRegistros(self,cc = 0,nombre = 0,apellido = 0,correo = 0):
        atributos_usuario = ['idusuario','nomusuario','apeusuario','correousuario']
        lis = [cc,nombre,apellido,correo]
        lis2 = []
        for i in lis:
            if i != 0:
                con = f"select count(*) from usuarios where {atributos_usuario} ilike '%{i}%'"
                self.cur.execute(con)
                conteo = self.cur.fetchall
                lis2.append(conteo[0][0])
            else:
                lis2.append(0)