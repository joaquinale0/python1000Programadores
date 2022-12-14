from creacion_basedatos import crear_base_datos as bd
from sala import Sala
from pelicula import Pelicula

class horario:
    def __init__(self, idHorario, entrada, salida, horario_idSala, horario_idhorario):
        self.__idHorario = idHorario
        self.__entrada = entrada
        self.__salida = salida
        self.__horario_idSala = horario_idSala
        self.__horario_idhorario = horario_idhorario
    def __str__(self):
        cadena = "\nId Horario: " + self.__idHorario
        cadena+= "\nEntrada: " + self.__entrada
        cadena+= "\nsalida: " + self.__salida
        cadena+= "\nhorario_idSala: " + self.__horario_idSala
        cadena+= "\nhorario_idhorario: " + self.__horario_idhorario
        return cadena
    
    @property
    def getIdHorario(self):
        return self.__idHorario
    @property
    def getEntrada(self):
        return self.__entrada
    @property
    def getSalida(self):
        return self.__salida
    
    #@setEntrada.setter
    def setEntrada (self,nuevoEntrada):
        self.__entrada = nuevoEntrada
   #@setSalida.setter
    def setSalida (self,nuevoSalida):
        self.__salida = nuevoSalida

    @classmethod
    def crear_Horario (self):
        id = bd.devolver_ID("idHorario","horario")
        print("\nFecha de entrada")
        entrada = bd.crearFecha()
        print("\nFecha de salida")
        salida = bd.crearFecha()
        id_sala = Sala.mostrarSalas()
        id_pelicula = Pelicula.mostrarPeliculas()
        
        bd.cargar_horario(id, entrada, salida, id_sala, id_pelicula)

    @classmethod
    def modificar_horario (self):
        if(bd.listaVacia("horario") == False):
            idDado = self.mostrarhorarios()
            print("\nFecha de entrada")
            entrada = bd.crearFecha()
            print("\nFecha de salida")
            salida = bd.crearFecha()
            id_sala = Sala.mostrarSalas()
            id_pelicula = Pelicula.mostrarPeliculas()
            bd.modificar_horario(idDado, entrada, salida, id_sala, id_pelicula)
        else:
            print("No hay horario")

    @classmethod
    def eliminar_horario (self):
        if(bd.listaVacia("horario") == False):
            idDado = self.mostrarhorarios()
            if(bd.cantidad_idHorario_reservas(idDado) == 0 ):
                bd.eliminar_horario(idDado)
            else:
                print("No se puede eliminar ya que el horario esta siendo ocupada")
        else:
            print("No hay horario")
            
    @classmethod
    def existe_horario (self,id): # id debe ser Entero
        bandera = False
        if(bd.listaVacia("horario") == False):
            todashorario = bd.lista_id_horario()
            for idHorario in todashorario:
                compara = bd.transformarNumero(str(idHorario))
                if(id == compara):
                    bandera = True
                    break
        return bandera

    @classmethod
    def mostrarhorarios (self):
        listahorario = bd.devolver_id_entrada_titulo_nombreSala_horario()
        seguir = True
        while(seguir):
            print("Elija una opcion: ")
            for horario in listahorario:
                id, entrada, titulo, nombreSala = horario
                print(f"{id}- horario: {entrada} Pelicula: {titulo} Sala: {nombreSala}")
            idDado = bd.transformarNumero(input("ingrese un número: "))
            if(type(idDado) == int):
                if(self.existe_horario(idDado)):
                    seguir = False
                    return idDado
                else:
                    print("No existe el Horario ingresada")
            else:
                print("No ingreso un número")
