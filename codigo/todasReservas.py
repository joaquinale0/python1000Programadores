class todasReservas:
    def __init__(self, idTodasReservas, todasReservas_idReserva, todasReservas_idUsuario):
        self.__idTodasReservas = idTodasReservas
        self.__todasReservas_idReserva = todasReservas_idReserva
        self.__todasReservas_idUsuario = todasReservas_idUsuario
    def __str__(self):
        cadena = "\nId Todas Reservas: " + self.__idTodasReservas
        cadena+= "\nTodas Reservas Id Reserva: " + self.__todasReservas_idReserva
        cadena+= "\nTodas Reservas Id Usuario: " + self.__todasReservas_idUsuario
        return cadena
    
    @property
    def getIdTodasReservas(self):
        return self.__idTodasReservas
    @property
    def getTodasReservas_idReserva(self):
        return self.__todasReservas_idReserva
    @property
    def getTodasReservas_idUsuario(self):
        return self.__todasReservas_idUsuario
        
    @setTodasReservas_idReserva.setter
    def setTodasReservas_idReserva (self, nuevoTodasReservas_idReserva):
        self.__todasReservas_idReserva = nuevoTodasReservas_idReserva
    @setTodasReservas_idUsuario.setter
    def setTodasReservas_idUsuario (self, nuevotodasReservas_idUsuario):
        self.__todasReservas_idReserva = nuevotodasReservas_idUsuario
    