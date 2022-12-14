class asientos:
    def __init__(self, idAsientos, asientos_idSala, asientoOcupado, asientos_idHorario):
        self.__idAsientos = idAsientos
        self.__asientoOcupado = asientoOcupado
        self.__asientos_idSala = asientos_idSala
        self.__asientos_idHorario = asientos_idHorario
    def __str__(self):
        cadena = "\nId Asientos: " + self.__idAsientos
        cadena+= "\nAsiento Ocupado: " + self.__asientoOcupado
        cadena+= "\nAsientos Id Sala: " + self.__asientos_idSala
        cadena+= "\nAsientos Id Horario: " + self.__asientos_idHorario
        return cadena
    
    @property
    def getIdAsientos(self):
        return self.__idAsientos
    @property
    def getasientoOcupado(self):
        return self.__asientoOcupado
    
    @setAsientoOcupado.setter
    def setAsientoOcupado (self, nuevoOcupado):
        self.__asientoOcupado = nuevoOcupado
    