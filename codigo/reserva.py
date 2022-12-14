from creacion_basedatos import crear_base_datos as bd
from horario import horario
from datetime import datetime

class reserva:
    def __init__(self, idReserva, butaca, pelicula, reserva_idUsuario, reserva_idSala, reserva_idPelicula, reserva_idHorario):
        self.__idReserva = idReserva
        self.__butaca = butaca
        self.__pelicula = pelicula
        self.__reserva_idUsuario = reserva_idUsuario
        self.__reserva_idSala = reserva_idSala
        self.__reserva_idPelicula = reserva_idPelicula
        self.__reserva_idHorario = reserva_idHorario

    def __str__(self):
        cadena = "\nId Reserva: " + self.__idReserva
        cadena+= "\nButaca: " + self.__butaca
        cadena+= "\nPelicula: " + self.__pelicula
        cadena+= "\nReserva Id Usuario: " + self.__reserva_idUsuario
        cadena+= "\nReserva Id Sala: " + self.__reserva_idSala
        cadena+= "\nReserva Id Pelicula: " + self.__reserva_idPelicula
        cadena+= "\nReserva Id Horario: " + self.__reserva_idHorario
        return cadena
    
    @property
    def getIdReserva(self):
        return self.__idReserva
    @property
    def getButaca(self):
        return self.__butaca
   
    @property
    def getPelicula(self):
        return self.__pelicula
    @property
    def getReserva_idUsuario(self):
        return self.__reserva_idUsuario
    @property
    def getReserva_idSala(self):
        return self.__reserva_idSala
    @property
    def getReserva_idHorario (self):
        return self.__reserva_idHorario

    
    #@setbutaca.setter
    def setbutaca (self,nuevobutaca):
        self.__butaca = nuevobutaca
    #@setpelicula.setter
    def setpelicula (self,nuevopelicula):
        self.__pelicula = nuevopelicula


    @classmethod
    def ver_todas_reservas(self):
        if(bd.listaVacia("reserva") == False):
            todasReservas = bd.lista_Tabla("reserva")
            for  id, butaca, pelicula, idUsuario, idSala, idPelicula, idHorario in todasReservas:
                print(id)
                self.ver_una_reserva(id)
        else:
            print("No hay Reservas")

    @classmethod
    def ver_una_reserva(self, id): # id debe ser Entero
        if(bd.listaVacia("reserva") == False):
            if(self.existe_Reserva(id)):
                id, butaca, pelicula, idUsuario, idSala, idPelicula, idHorario = bd.devolver_una_reserva(id)
                titulo, categoria, formato = bd.devolver_Titulo_Genero_Formato_pelicula(idPelicula)
                formato = self.devolverFormato(formato)
                peliculaDatos = titulo + " \t " + str(categoria) + " \t " + formato
                usuario = bd.devuelveCadena(bd.devolver_user_usuario(idUsuario))
                sala = bd.devuelveCadena(bd.devolver_nombre_sala(idSala))
                entrada = bd.devuelveCadena(bd.devolver_entrada_horario(idHorario))
                print(f"\tTICKET\nNumero de reserva: {id}\nUsuario: {usuario}\nSala: {sala}\nButaca: {butaca}\nPelicula: {pelicula} \nDetalle de la Pelicula: {peliculaDatos}\nHorario de entrada: {entrada}")
            else:
                print(f"No existe la reserva nro: {id}")
        else:
            print("No hay Reservas")


    @classmethod
    def existe_Reserva (self,id): # id debe ser Entero
        bandera = False
        if(bd.listaVacia("reserva") == False):
            todasReservas = bd.lista_id_reserva()
            for idReservas in todasReservas:
                compara = bd.transformarNumero(str(idReservas))
                if(id == compara):
                    bandera = True
                    break
        return bandera

    @classmethod
    def opcion_ver_una_reserva (self):
        id = int(input("Nro de reserva: "))
        self.ver_una_reserva(id)

    @classmethod
    def devolverFormato(self, formato):
        if(formato == 1):
            return "2D"
        else:
            return "3D"

    @classmethod
    def crear_reserva (self, idUsuario):
        if(bd.listaVacia("horario") == False):
            id = bd.devolver_ID("idReserva","reserva")
            print("\n")
            reserva_idHorario = horario.mostrarhorarios()
            id_sala, id_pelicula = bd.devolver_idSala_idPelicula_horario(reserva_idHorario)
            pelicula = bd.devuelveCadena(bd.devolver_titulo_pelicula(id_pelicula))
            butaca = self.cargarButaca(id_sala)
            ocupado = bd.transformarNumero(str(bd.cantidad_uso_butaca(reserva_idHorario,butaca)))
            if(ocupado == 0):
                idAsiento = bd.devolver_ID("idAsientos", "asientos")
                bd.cargar_asiento(idAsiento, butaca, id_sala, reserva_idHorario)
                bd.cargar_reserva(id, butaca, pelicula, idUsuario, id_sala, id_pelicula, reserva_idHorario)            
            else:
                print(f"Butaca número {butaca} esta ocupada")
        else:
            print("No existe horario para poder crear una reserva")


    @classmethod
    def modificar_reserva (self, id):
        fecha_actual = datetime.now()
        formato_fecha = "%Y-%m-%d %H:%M:%S"
        cantidadReserva = bd.transformarNumero(str(bd.cantidad_de_reservas_de_un_usuario(id)))
        if(cantidadReserva > 0):
            idDado = self.mostrarReserva(id)
            id_Horario = bd.transformarNumero(str(bd.devolver_idHorario_Reserva(idDado)))
            fecha_reserva = bd.devuelveCadena(list(bd.devolver_entrada_Horario(id_Horario)))
            fecha_reserva = datetime.strptime(fecha_reserva,formato_fecha)
            if(fecha_actual < fecha_reserva):
                reserva_idHorario = horario.mostrarhorarios()
                id_sala, id_pelicula = bd.devolver_idSala_idPelicula_horario(reserva_idHorario)
                pelicula = bd.devuelveCadena(bd.devolver_titulo_pelicula(id_pelicula))
                butaca = self.cargarButaca(id_sala)
                ocupado = bd.transformarNumero(str(bd.cantidad_uso_butaca(reserva_idHorario,butaca))) # DEVUELVE UN CANTIDAD DE VECES OCUPADA LA BUTACA SEGUN HORAIO
                if(ocupado == 0):
                    idAsientos = bd.transformarNumero(str(bd.devolver_idAsiento_butaca(reserva_idHorario,butaca))) # DEVUELVE IDBUTACA PARA MODIFICARLA SEGUN HORAIO Y BUTACA
                    bd.modificar_asiento(idAsientos,butaca,id_sala,reserva_idHorario)
                    bd.modificar_reserva(idDado, butaca, pelicula, id, id_sala, id_pelicula,reserva_idHorario)
                else:
                    print(f"Butaca número {butaca} esta ocupada")
            else:
                print("Esa reserva ya expiro")

        else:
            print("No hay reservas")

    @classmethod
    def cargarButaca(self, idSala):
        tam = bd.transformarNumero(str(bd.devolver_cantidad_butacas_sala(idSala)))
        butaca = bd.transformarNumero(input(f"Elegir una butaca 1 al {tam}: "))
        while(butaca < 1 or butaca > tam ):
            butaca = bd.transformarNumero(input(f"Elegir una butaca 1 al {tam}: "))
        return butaca


# TAL VEZ NO ME SIRVA

    @classmethod
    def mostrarReserva (self, id):
        listaReserva = bd.devolver_lista_reserva_de_un_usuario(id)
        seguir = True
        while(seguir):
            print("Elija una opcion: ")
            for reserv in listaReserva:
                idReserva, pelicula, butaca, reserva_idHorario = reserv
                print(f"{idReserva}- pelicula: {pelicula} butaca: {butaca} reservado en el horario: {reserva_idHorario}")
            idDado = bd.transformarNumero(input("ingrese un número: "))
            if(type(idDado) == int):
                if(self.existe_reserva_de_usuario(id, idDado)):
                    seguir = False
                    return idDado
                else:
                    print("No existe la reserva ingresada")
            else:
                print("No ingreso un número")

    @classmethod
    def existe_reserva_de_usuario (self,idUsuario, idReserva): # id debe ser Entero
        bandera = False
        cantidReserva = bd.transformarNumero(str(bd.cantidad_de_reservas_de_un_usuario(idUsuario)))
        if(cantidReserva > 0):
            todasReservas = bd.lista_idReserva_de_un_usuario(idUsuario)
            for idReser in todasReservas:
                compara = bd.transformarNumero(str(idReser))
                if(idReserva == compara):
                    bandera = True
                    break
        return bandera


    @classmethod
    def mostrar_ultima_reserva(self, id):
        cantidReserva = bd.transformarNumero(str(bd.cantidad_de_reservas_de_un_usuario(id)))
        if(cantidReserva > 0):
            todosReservas = bd.lista_idReserva_de_un_usuario(id)
            ultimaReserva = todosReservas.pop()
            ultimaReserva = bd.transformarNumero(str(ultimaReserva))
            self.ver_una_reserva(ultimaReserva)
        else:
            print("No hay reservas")


    @classmethod
    def opcion_mostrar_historial (self, id):
        cantidReserva = bd.transformarNumero(str(bd.cantidad_de_reservas_de_un_usuario(id)))
        if(cantidReserva > 0):
            todosReservas = bd.lista_idReserva_de_un_usuario(id)
            for idReserva in todosReservas:
                self.ver_una_reserva(bd.transformarNumero(str(idReserva)))
        else:
            print("No hay reservas")