import sqlite3
import datetime
class crear_base_datos:

    def __init__(self):
        conexion = sqlite3.connect("baseDatos_1")
        cursor = conexion.cursor()
        conexion.commit()
        conexion.close()
        
        self._cursor = cursor
        
    @classmethod
    def crear_tabla_usuario(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()

            cursor.execute('''create table if not exists usuario(
                    idUsuario integer primary key,
                    usuario text,
                    contrasena text,
                    administracion integer,
                    tarjeta integer
                );
            ''')
        except conexion:
            print ("Error creacion de tabla de usuario")
        finally:
            conexion.commit()
            conexion.close()

    @classmethod
    def crear_tabla_sala(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
        
            cursor.execute('''
                create table if not exists sala(
                    idSala integer primary key,
                    nombreSala text,
                    cantidadAsientos integer
                );
            ''')
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error creacion de tabla de sala")
    
    @classmethod
    def crear_tabla_pelicula(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            cursor.execute('''create table if not exists pelicula(
                    idPelicula integer primary key,
                    titulo text,
                    genero text,
                    duracion datetime,
                    categoria integer,
                    formato integer
                );
            ''')
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error creacion de tabla de pelicula")

    @classmethod
    def crear_tabla_horario(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
        
            cursor.execute('''create table if not exists horario(
                    idHorario integer primary key,
                    entrada datetime,
                    salida datetime,
                    horario_idSala integer,
                    horario_idPelicula integer,
                    foreign key (horario_idSala) references sala(idSala),
                    foreign key (horario_idPelicula) references pelicula(idPelicula)
                );
            ''')

            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error creacion de tabla de horario")

    @classmethod
    def crear_tabla_asientos(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
        
            cursor.execute('''create table if not exists asientos(
                idAsientos integer primary key,
                asientoOcupado integer,
                asientos_idSala integer,
                asientos_idHorario integer,
                foreign key (asientos_idSala) references sala(idSala),
                foreign key (asientos_idHorario) references horario(idHorario)
                );
            ''')

            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error creacion de tabla de asientos")

    @classmethod
    def crear_tabla_reserva(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            cursor.execute('''create table if not exists reserva(
                idReserva integer primary key,
                butaca integer,
                pelicula text,
                reserva_idUsuario integer,
                reserva_idSala integer,
                reserva_idPelicula integer,
                reserva_idHorario integer,
                foreign key (reserva_idUsuario) references usuario(idUsuario),
                foreign key (reserva_idSala) references sala(idSala),
                foreign key (reserva_idPelicula) references pelicula(idPelicula),
                foreign key (reserva_idHorario) references horario(idHorario)
                );
            ''')
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error creacion de tabla de reserva")

    @classmethod
    def crear_tabla_todasReservas(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            cursor.execute('''create table if not exists  todasReservas(
                idTodasReservas integer primary key,
                todasReservas_idReserva integer,
                todasReservas_idUsuario integer,
                foreign key (todasReservas_idReserva) references reserva(idReserva),
                foreign key (todasReservas_idUsuario) references usuario(idUsuario)
            );
            ''')
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error creacion de tabla de todasReservas")

    @classmethod
    def crear_tabla_descuento(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            cursor.execute('''create table if not exists descuento(
            idDescuentos integer primary key,
            dia text,
            porcentaje real
            );
            ''')
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error creacion de tabla de descuento")


    
    
# metodos de Fecha Y Hora
    @classmethod
    def crearFecha (self):
        formato_fecha = "%Y-%m-%d %H:%M:%S"
        año = self.transformarNumero(input("ingresar el año: "))
        while(año < 1900 or año > 2100):
            año = self.transformarNumero(input("ingresar el año: "))
        mes = self.transformarNumero(input("ingresar mes mes: "))
        while(mes < 1 or mes > 12):
            mes = self.transformarNumero(input("ingresar el mes: "))
        dia = self.transformarNumero(input("ingresar dia: "))
        while(dia < 1 or dia > 31):
            dia = self.transformarNumero(input("ingresar el dia: "))
        hora = self.transformarNumero(input("ingresar Hora: "))
        while(hora < 0 or hora > 23):
            hora = self.transformarNumero(input("ingresar las hora: "))
        minuto = self.transformarNumero(input("ingresar minuto: "))
        while(minuto < 0 or minuto > 59):
            minuto = self.transformarNumero(input("ingresar los minuto: "))
        segundos = self.transformarNumero(input("ingresar segundos: "))
        while(segundos < 0 or segundos > 59):
            segundos = self.transformarNumero(input("ingresar los segundos: "))
        fecha = str(año) +"-"+ str(mes) +"-"+ str(dia) +" "+ str(hora) +":"+ str(minuto) +":"+ str(segundos)
        fecha = datetime.datetime.strptime(fecha,formato_fecha)
        return str(fecha)


    @classmethod
    def crearHora (self):
        formato_fecha = "%Y-%m-%d %H:%M:%S"
        año = 1900
        mes = 1
        dia = 1
        hora = self.transformarNumero(input("ingresar Hora: "))
        while(hora < 0 or hora > 23):
            hora = self.transformarNumero(input("ingresar las hora: "))
        minuto = self.transformarNumero(input("ingresar minuto: "))
        while(minuto < 0 or minuto > 59):
            minuto = self.transformarNumero(input("ingresar los minuto: "))
        segundos = self.transformarNumero(input("ingresar segundos: "))
        while(segundos < 0 or segundos > 59):
            segundos = self.transformarNumero(input("ingresar los segundos: "))
        fecha = str(año) +"-"+ str(mes) +"-"+ str(dia) +" "+ str(hora) +":"+ str(minuto) +":"+ str(segundos)
        fecha = datetime.datetime.strptime(fecha,formato_fecha)
        return str(fecha)


    # METODOS PARA TRABAJAR CON DATOS SQLITE

    

    @classmethod
    def devolver_ID(self, columna, tabla):
        try:
            if(self.listaVacia(tabla) == True):
                return 1
            else:
                conexion = sqlite3.connect("baseDatos_1")
                cursor = conexion.cursor()
                query = "select " + columna + " from " + tabla + ";"
                cursor.execute(query)
                todosId = cursor.fetchall()
                conexion.commit()
                conexion.close()
                id = str(todosId.pop())
                return self.transformarNumero(id) + 1
        except conexion:
            print (f"Error devolucion de ID de la tabla {tabla}")

    @classmethod
    def transformarNumero (self, recibido):
        num = ""
        for caracter in recibido:
            if(caracter == '1' or caracter == '2' or caracter == '3' or caracter == '4' or caracter == '5' or caracter == '6' or caracter == '7' or caracter == '8' or caracter == '9' or caracter == '0'):
                num = num + caracter
        if(num == ""):
            return 0
        else:
            return int(num)

    @classmethod
    def listaVacia (self,tabla):
        try:
            conexion = sqlite3.connect("baseDatos_1")   
            cursor = conexion.cursor()
            query = "SELECT COUNT(*) FROM " + tabla + ";"
            cursor.execute(query)
            tam = cursor.fetchone()
            tam = self.transformarNumero(str(tam))
            if(tam == 0):
                return True
            else:
                return False
        except conexion:
            print("error en la conecion del modulo de lista")
        finally:
            conexion.commit()
            conexion.close()

    @classmethod
    def devuelveCadena (self, recibido):
        cadena = ""
        for caracter in recibido:
            str(caracter)
            if( caracter != ','):
                cadena = cadena + caracter
        return cadena



    # DEVOLVER lista DE TABLAS USUARIO 

    @classmethod
    def lista_id_horario (self): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idHorario from horario;"
            cursor.execute(query)
            id_horario = cursor.fetchall()
            conexion.commit()
            conexion.close()

            return id_horario
        except conexion:
            print ("Error devolver lista de id_pelicula")


    @classmethod
    def lista_id_pelicula (self): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idPelicula from pelicula;"
            cursor.execute(query)
            id_pelicula = cursor.fetchall()
            conexion.commit()
            conexion.close()

            return id_pelicula
        except conexion:
            print ("Error devolver lista de id_pelicula")

    @classmethod
    def lista_id_sala (self): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idSala from sala;"
            cursor.execute(query)
            id_reservas = cursor.fetchall()
            conexion.commit()
            conexion.close()

            return id_reservas
        except conexion:
            print ("Error devolver lista de idReservas")

    @classmethod
    def lista_id_reserva (self): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idReserva from reserva;"
            cursor.execute(query)
            id_reservas = cursor.fetchall()
            conexion.commit()
            conexion.close()

            return id_reservas
        except conexion:
            print ("Error devolver lista de idReservas")

    @classmethod
    def lista_Usuarios(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            cursor.execute('''select usuario from usuario; ''')
            usuarios = cursor.fetchall()
            conexion.commit()
            conexion.close()

            return usuarios

           
        except conexion:
            print ("Error devolver los Usuarios")

    @classmethod
    def lista_usuarios_contrasena(self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            cursor.execute('''select usuario, contrasena, idUsuario from usuario; ''')
            usuarios = cursor.fetchall()
            
            return usuarios
        except conexion:
            print ("Error devolver los Usuarios y Contraseña")
        finally:
            conexion.commit()
            conexion.close()

    @classmethod
    def administracion_usuario (self, id):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select administracion from usuario where idUsuario = " + str(id) + ";" 
            cursor.execute(query)
            administracion = cursor.fetchone()
            return self.transformarNumero(str(administracion))
        except conexion:
            print ("Error devolver el Usuario")
        finally : 
            conexion.commit()
            conexion.close()

    @classmethod
    def lista_Tabla(self, tabla):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select * from " + tabla + ";"
            cursor.execute(query)
            lista_Tabla = cursor.fetchall()
            conexion.commit()
            conexion.close()

            return lista_Tabla
        except conexion:
            print (f"Error devolver los todas coulumnas de tabla {tabla}")

    @classmethod
    def devolver_user_usuario(self, id): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select usuario from usuario where idUsuario = " + str(id) + ";"
            cursor.execute(query)
            user = cursor.fetchone()
            conexion.commit()
            conexion.close()

            return user
        except conexion:
            print ("Error devolver el usuario")

    @classmethod
    def devolver_nombre_sala(self, id): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select nombreSala from sala where idSala = " + str(id) + ";"
            cursor.execute(query)
            user = cursor.fetchone()
            conexion.commit()
            conexion.close()

            return user
        except conexion:
            print ("Error devolver el nombre de la Sala")

    @classmethod
    def devolver_Titulo_Genero_Formato_pelicula(self, id): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select titulo, genero, formato from pelicula where idPelicula = " + str(id) + ";"
            cursor.execute(query)
            pelicula = cursor.fetchone()
            conexion.commit()
            conexion.close()

            return pelicula
        except conexion:
            print ("Error devolver Titulo Categoria Formato pelicula")

    @classmethod
    def devolver_entrada_horario(self, id): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select entrada from horario where idHorario = " + str(id) + ";"
            cursor.execute(query)
            entrada = cursor.fetchone()
            conexion.commit()
            conexion.close()

            return entrada
        except conexion:
            print ("Error devolver Entrada de Horario")

    @classmethod
    def devolver_una_reserva(self, id): #El id debe ser int
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select * from reserva where idReserva = " + str(id) + ";"
            cursor.execute(query)
            reserva = cursor.fetchone()
            conexion.commit()
            conexion.close()

            return reserva
        except conexion:
            print ("Error devolver Una Reserva")


    @classmethod
    def lista_descuentos (self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            cursor.execute("select dia, porcentaje from descuento")
            listaDescuento = cursor.fetchall()
            conexion.commit()
            conexion.close()

            return listaDescuento
        except conexion:
            print ("Error creacion de tabla de descuento")

    @classmethod
    def modificar_porcentade_descuento (self, idDescuento, porcentaje):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "update descuento set porcentaje = " + str(porcentaje) + " where idDescuentos = " + str(idDescuento) + ";"
            cursor.execute(query)
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error modificar el porcentaje de descuento")


# SECTOR DE SALA
    @classmethod
    def cargar_sala (self, id, nombre, cantidad):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "insert into sala values(?,?,?)"
            cursor.execute(query,(id,nombre,cantidad))
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error crear una sala")

    @classmethod
    def devolver_id_nombre_sala (self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idSala, nombreSala from sala"
            cursor.execute(query)
            listaSala = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return listaSala
        except conexion:
            print ("Error devolver_id_nombre_sala")
    
    @classmethod
    def modificar_sala (self, id,  nombre, asientos):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "update sala set nombreSala = '" + nombre + "' where idSala = " + str(id) + ";"
            cursor.execute(query)
            conexion.commit()
            conexion.close()
            #--------------------------------------
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "update sala set cantidadAsientos = " + str(asientos) +  " where idSala = " + str(id) + ";"
            cursor.execute(query)
            conexion.commit()
            conexion.close()
        except ModuleNotFoundError:
            print ("Error modificar sala")


    @classmethod
    def eliminar_sala (self, id):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "delete from sala where idSala = " + str(id) + ";"
            cursor.execute(query)
            
        except ModuleNotFoundError:
            print ("Error eliminar sala")
        finally:
            conexion.commit()
            conexion.close()

# devolver_id_nombre_sala
    @classmethod
    def devolver_cantidad_butacas_sala (self, id):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select cantidadAsientos from sala where idSala = " + str(id) + ";"
            cursor.execute(query)
            tamButaca = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return tamButaca
        except conexion:
            print ("Error devolver_cantidad_butacas")


# TABLA PELICULA
    @classmethod
    def cargar_pelicula (self, id,  titulo, genero, duracion, categoria, formato):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "insert into pelicula values(?,?,?,?,?,?)"
            cursor.execute(query,(id, titulo, genero, duracion, categoria, formato))
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error crear una pelicula")

    @classmethod
    def modificar_pelicula (self, id,  titulo, genero, duracion, categoria, formato): 
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "update pelicula set titulo = '" + titulo + "', genero = '"+ genero +"', duracion = '" + str(duracion) + "', categoria = " + str(categoria) +", formato = " + str(formato) +"  where idPelicula = " + str(id) + ";"
            cursor.execute(query)
            conexion.commit()
            conexion.close()
        except ModuleNotFoundError:
            print ("Error modificar pelicula")

    @classmethod
    def eliminar_pelicula (self, id):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "delete from pelicula where idPelicula = " + str(id) + ";"
            cursor.execute(query)
            
        except ModuleNotFoundError:
            print ("Error eliminar pelicula")
        finally:
            conexion.commit()
            conexion.close()

    @classmethod
    def devolver_id_titulo_pelicula (self):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idPelicula, titulo from pelicula;"
            cursor.execute(query)
            listaPelicula = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return listaPelicula
        except conexion:
            print ("Error devolver_id_titulo_pelicula")


    @classmethod
    def devolver_titulo_pelicula (self, id):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select titulo from pelicula where idPelicula = " + str(id) + ";"
            cursor.execute(query)
            titulo = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return titulo
        except conexion:
            print ("Error devolver_titulo_pelicula")


# TABLA HORARIO

    @classmethod
    def cargar_horario (self, id,  entrada, salida, horario_idSala, horario_idPelicula):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "insert into horario values(?,?,?,?,?)"
            cursor.execute(query,(id, entrada, salida, horario_idSala, horario_idPelicula))
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error crear una horario")

    @classmethod
    def modificar_horario (self, id,  entrada, salida, horario_idSala, horario_idPelicula): 
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "update horario set entrada = '" + entrada + "', salida = '"+ salida +"', horario_idSala = '" + str(horario_idSala) + "', horario_idPelicula = " + str(horario_idPelicula) + "  where idHorario = " + str(id) + ";"
            cursor.execute(query)
            conexion.commit()
            conexion.close()
        except ModuleNotFoundError:
            print ("Error modificar horario")

    @classmethod
    def eliminar_horario (self, id):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "delete from horario where idHorario = " + str(id) + ";"
            cursor.execute(query)
            
        except ModuleNotFoundError:
            print ("Error eliminar horario")
        finally:
            conexion.commit()
            conexion.close()

    @classmethod
    def devolver_id_entrada_titulo_nombreSala_horario (self):     
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idHorario, entrada, titulo, nombreSala from horario left join pelicula, sala on horario.horario_idPelicula = pelicula.idPelicula AND horario.horario_idSala = sala.idSala;"
            cursor.execute(query)
            listaHorario = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return listaHorario
        except conexion:
            print ("Error devolver_id_titulo_pelicula")


    @classmethod
    def devolver_idSala_idPelicula_horario (self, id):    
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select horario_idSala, horario_idPelicula from horario where idHorario = " + str(id) + ";"
            cursor.execute(query)
            listaHorario = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return listaHorario
        except conexion:
            print ("Error devolver_idSala_idPelicula_horario")

    @classmethod
    def devolver_entrada_Horario (self, id):    
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select entrada from horario WHERE idHorario = " + str(id) + ";"
            cursor.execute(query)
            entrada = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return entrada
        except conexion:
            print ("Error devolver_entrada_Horario")

    @classmethod
    def cantidad_idSala_de_horario (self, idSala):    
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select count(horario_idSala) from horario WHERE horario_idSala = " + str(idSala) + ";"
            cursor.execute(query)
            contador = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return contador
        except conexion:
            print ("Error cantidad_idSala_de_horario")

# select entrada from horario WHERE idHorario = 1;

# TABLA RESERVA



    @classmethod
    def cargar_reserva (self, id,  butaca, pelicula, reserva_idUsuario, reserva_idSala, reserva_idPelicula, reserva_idHorario):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "insert into reserva values(?,?,?,?,?,?,?)"
            cursor.execute(query,(id, butaca, pelicula, reserva_idUsuario, reserva_idSala, reserva_idPelicula, reserva_idHorario))
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error crear una reserva")


        
    @classmethod
    def devolver_lista_reserva_de_un_usuario (self, id):  
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idReserva, pelicula, butaca, reserva_idHorario from reserva where reserva_idUsuario = " + str(id) + ";"
            cursor.execute(query)
            listaReserva = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return listaReserva
        except conexion:
            print ("Error devolver_lista_reserva_de_un_usuario")

    @classmethod
    def lista_idReserva_de_un_usuario (self, id):  
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idReserva from reserva where reserva_idUsuario = " + str(id) + ";"
            cursor.execute(query)
            listaIdReserva = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return listaIdReserva
        except conexion:
            print ("Error lista_idReserva_de_un_usuario")


    @classmethod
    def cantidad_de_reservas_de_un_usuario (self, id):  
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select count(idReserva) from reserva where reserva_idUsuario = " + str(id) + ";"
            cursor.execute(query)
            cantidadReserva = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return cantidadReserva
        except conexion:
            print ("Error cantidad_de_reservas_de_un_usuario")

    @classmethod
    def modificar_reserva (self, id,  butaca, pelicula, reserva_idUsuario, reserva_idSala, reserva_idPelicula, reserva_idHorario):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "update reserva set butaca = " + str(butaca) + ", pelicula = '"+ pelicula +"', reserva_idUsuario = " + str(reserva_idUsuario) + ", reserva_idSala = " + str(reserva_idSala) + ", reserva_idPelicula = " + str(reserva_idPelicula) + ", reserva_idHorario = " + str(reserva_idHorario) +  "  where idReserva = " + str(id) + ";"
            cursor.execute(query)
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error modificar una reserva")


    @classmethod
    def devolver_fecha_reserva (self):    
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select entrada from reserva left join horario on horario.horario_idPelicula = pelicula.idPelicula AND horario.horario_idSala = sala.idSala;"
            cursor.execute(query)
            listaHorario = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return listaHorario
        except conexion:
            print ("Error devolver_id_titulo_pelicula")

    @classmethod
    def devolver_idHorario_Reserva (self, id):    
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select reserva_idHorario from reserva WHERE idReserva = " + str(id) + ";"
            cursor.execute(query)
            idHorario = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return idHorario
        except conexion:
            print ("Error devolver_idHorario_Reserva")

#   TABLA ASIENTO

    @classmethod
    def cantidad_uso_butaca(self, idHorario, butaca):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select count(asientoOcupado) from asientos WHERE asientos_idHorario = " + str(idHorario) + " AND asientoOcupado = " + str(butaca) + ";"
            cursor.execute(query)
            idHorario = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return idHorario
        except conexion:
            print ("Error devolver_idHorario_Reserva")

    @classmethod
    def cargar_asiento (self, id,  butaca, idSala, idHorario):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "insert into asientos values(?,?,?,?)"
            cursor.execute(query,(id, butaca, idSala, idHorario))
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error crear un asiento")

    @classmethod
    def modificar_asiento (self, id,  butaca, idSala, idHorario):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "update asientos set asientoOcupado = " + str(butaca) + ", asientos_idSala = " + str(idSala) +", asientos_idHorario = " + str(idHorario) +  "  where idAsientos = " + str(id) + ";"
            cursor.execute(query)
            conexion.commit()
            conexion.close()
        except conexion:
            print ("Error modificar una asiento")

    @classmethod
    def devolver_idAsiento_butaca(self, idHorario, butaca):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select idAsientos from asientos WHERE asientos_idHorario = " + str(idHorario) + " AND asientoOcupado = " + str(butaca) + ";"
            cursor.execute(query)
            idHorario = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return idHorario
        except conexion:
            print ("Error devolver_idAsiento_butaca")

#   METODOS PARA ELIMINAR 
    @classmethod
    def cantidad_idPelicula_reservas(self, idPelicula):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select count(idReserva) from reserva WHERE reserva_idPelicula = " + str(idPelicula) + ";"
            cursor.execute(query)
            cant = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return cant[0]
        except conexion:
            print ("Error cantidad_idPelicula_reservas")

    @classmethod
    def cantidad_idPelicula_horario(self, idPelicula):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select count(idHorario) from horario WHERE horario_idPelicula = " + str(idPelicula) + ";"
            cursor.execute(query)
            cant = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return cant[0]
        except conexion:
            print ("Error cantidad_idPelicula_horario")

    @classmethod
    def cantidad_idSala_reservas(self, idSala):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select count(idReserva) from reserva WHERE reserva_idSala = " + str(idSala) + ";"
            cursor.execute(query)
            cant = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return cant[0]
        except conexion:
            print ("Error cantidad_idSala_reservas")

    @classmethod
    def cantidad_idSala_horario(self, idSala):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select count(idHorario) from horario WHERE horario_idSala = " + str(idSala) + ";"
            cursor.execute(query)
            cant = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return cant[0]
        except conexion:
            print ("Error cantidad_idSala_horario")

    @classmethod
    def cantidad_idHorario_reservas(self, idHorario):
        try:
            conexion = sqlite3.connect("baseDatos_1")
            cursor = conexion.cursor()
            query = "select count(idReserva) from reserva WHERE reserva_idHorario = " + str(idHorario) + ";"
            cursor.execute(query)
            cant = cursor.fetchone()
            conexion.commit()
            conexion.close()
            return cant[0]
        except conexion:
            print ("Error cantidad_idSala_reservas")