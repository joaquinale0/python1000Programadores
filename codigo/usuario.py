from datetime import datetime
from creacion_basedatos import crear_base_datos as bd
import sqlite3

class Usuario:
    def __init__(self, usuario, contrasena, tarjeta, administracion, idUsuario):
        self.__idUsuario = idUsuario 
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__administracion = administracion
        self.__tarjeta = tarjeta
  
    def __str__(self):
        cadena= "\nIdUsuario: " + str(self.__idUsuario)
        cadena+= "\nUsuario: " + self.__usuario
        cadena+= "\nContrasena: " + self.__contrasena
        cadena+= "\nAdministracion: " + str(self.__administracion)
        cadena+= "\nTarjeta: " + str(self.__tarjeta)
        return cadena

    @property
    def getIdUsuario(self):
        return self.__idUsuario
    
    @property
    def getUsuario(self):
        return self.__usuario
    
    @property
    def getContrasena(self):
        return self.__contrasena
    
    @property
    def getAdministracion(self):
        return self.__administracion
    
    @property
    def getTarjeta(self):
        return self.__tarjeta
        
    #@setUsuario.setter
    def setUsuario (self, nuevoUsuario):
        self.__usuario = nuevoUsuario

    #@setContrasena.setter
    def setContrasena (self,nuevoContrasena):
        self.__contrasena = nuevoContrasena
    
    @classmethod
    def crear_usuario(self):
        user = input("Escribir usuario: ")
        return user

    @classmethod
    def crear_contrasena(self):
        contra = input("Escribir contrasena: ")
        return contra

    @classmethod
    def crear_fecha_nacimiento(self):
        fecha = input("Escribir dd (dia) de nacimiento: ")
        fecha +="/"+ input("escribir mm (mes) de nacimiento: ")
        fecha +="/"+ input("escribir YYYY (año) de nacimiento: ")
        fechaNacimientosss = datetime.strptime(fecha, "%d/%m/%Y")
        return fechaNacimientosss

    @classmethod
    def crear_cuenta (self):
        user = self.crear_usuario()
        if(bd.listaVacia("usuario") == True):
            contra = self.crear_contrasena()
            id = bd.devolver_ID("idUsuario", "usuario")
            cuenta = Usuario(user, contra, 0, 0, id)

            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            cursor.execute("insert into usuario values(?,?,?,?,?)", (cuenta.getIdUsuario, cuenta.getUsuario, cuenta.getContrasena, cuenta.getAdministracion, cuenta.getTarjeta))
            conexion.commit()
            conexion.close()
        else:
            if(self.usuarioUnico(user) == True):
                contra = self.crear_contrasena()
                id = bd.devolver_ID("idUsuario", "usuario")
                cuenta = Usuario(user, contra, 0, 0, id)

                conexion = sqlite3.connect("baseDatos_1")
                cursor = conexion.cursor()
                cursor.execute("insert into usuario values(?,?,?,?,?)", (cuenta.getIdUsuario, cuenta.getUsuario, cuenta.getContrasena, cuenta.getAdministracion, cuenta.getTarjeta))
                conexion.commit()
                conexion.close()
            else:
                while(Usuario.usuarioUnico(user) == False):
                    print("El Usuario Ya Existe")
                    user = self.crear_usuario()
                contra = self.crear_contrasena()
                id = bd.devolver_ID("idUsuario", "usuario")
                cuenta = Usuario(user, contra, 0, 0, id)

                conexion = sqlite3.connect("baseDatos_1")
                cursor = conexion.cursor()
                cursor.execute("insert into usuario values(?,?,?,?,?)", (cuenta.getIdUsuario, cuenta.getUsuario, cuenta.getContrasena, cuenta.getAdministracion, cuenta.getTarjeta))
                conexion.commit()
                conexion.close()         

    @classmethod
    def usuarioUnico (self,usuario): 
        bandera = True
        if(bd.listaVacia("usuario") == False):
            todosUsuarios = bd.lista_Usuarios()
            for user in todosUsuarios:
                compara = bd.devuelveCadena(user)
                if(usuario == compara):
                    bandera = False
                    break
        return bandera
        

    @classmethod
    def iniciarSesion (self):
        user = self.crear_usuario()
        contra = self.crear_contrasena()
        idUser = -1

        if(bd.listaVacia("usuario")):
            return -1
        else:
            todasCuentas = bd.lista_usuarios_contrasena()
            if(self.usuarioUnico(user) == True):
                print("Usuario no existe")
                return -1
            else:
                for usuario, contrasena, id in todasCuentas:
                    if(usuario == user and contra == contrasena):
                        idUser = id
                        break
                if(idUser == -1):
                    print("Contraseña erronea")
                    return idUser
                else:
                    return idUser

