from creacion_basedatos import crear_base_datos as bd
from datetime import datetime

class Sala:
    
    def __init__(self, idSala, nombreSala, cantidadAsientos):
      self.__idSala = idSala
      self.__nombreSala = nombreSala  
      self.__cantidadAsientos = cantidadAsientos
      self.__tabla = "sala"

    def __str__(self):
        cadena = "\nId Sala: " + self.__idSala
        cadena+= "\nNombre Sala: " + self.__nombreSala
        cadena+= "\nCantidad Asientos: " + self.__cantidadAsientos
        return cadena
        
    @property
    def getIdSala(self):
        return self.__idSala
    @property
    def getnombreSala(self):
        return self.__nombreSala
    @property
    def getCantidadAsesinatos(self):
        return self.__cantidadAsientos
    @property
    def getTabla(self):
        return self.__tabla
    
   # @setCantidadAsientos.setter
    def setCantidadAsientos (self,nuevoCantidadAsientos):
        self.__cantidadAsientos = nuevoCantidadAsientos

    @classmethod
    def crear_sala (self):
        id = bd.devolver_ID("idSala","sala")
        nombre_sala = input("Nombre de la sala: ")
        cantidad_asientos = int(input("cantidad de Asientos: "))
        if(type(cantidad_asientos) == int):
            bd.cargar_sala(id,nombre_sala,cantidad_asientos)
        else:
            print("Cantidad de asientos erroneo")

    @classmethod
    def modificar_sala (self):
        if(bd.listaVacia("sala") == False):
            idDado = self.mostrarSalas()
            nombre_sala = input("Nombre de la sala: ")
            cantidad_asientos = int(input("Cantidad de Asientos: "))
            if(type(cantidad_asientos) == int):
                bd.modificar_sala(idDado,nombre_sala,cantidad_asientos)
            else:
                print("Cantidad de asientos erroneo")
        else:
            print("No hay Sala")
            
    
    @classmethod
    def existe_Sala (self,id): # id debe ser Entero
        bandera = False
        if(bd.listaVacia("sala") == False):
            todasSalas = bd.lista_id_sala()
            for idSala in todasSalas:
                compara = bd.transformarNumero(str(idSala))
                if(id == compara):
                    bandera = True
                    break
        return bandera

    @classmethod
    def mostrarSalas (self):
        listaSala = bd.devolver_id_nombre_sala()
        seguir = True
        while(seguir):
            print("Elija una opcion: ")
            for sala in listaSala:
                id, nombre = sala
                print(f"{id}- Sala: {nombre}")
            idDado = bd.transformarNumero(input("ingrese un número: "))
            if(type(idDado) == int):
                if(self.existe_Sala(idDado)):
                    seguir = False
                    return idDado
                else:
                    print("No existe la sala ingresada")
            else:
                print("No ingreso un número")


    @classmethod
    def eliminar_sala (self):
        if(bd.listaVacia("sala") == False):
            idDado = self.mostrarSalas()
            if(bd.cantidad_idSala_reservas(idDado) == 0 and bd.cantidad_idSala_horario(idDado) == 0):
                bd.eliminar_sala(idDado)
            else:
                print("No se puede eliminar ya que la sala esta siendo ocupada")
        else:
            print("No hay Sala")

    @classmethod
    def opcion_ver_salas (self):
        if(bd.listaVacia("sala") == False):
            listaSala = bd.devolver_id_nombre_sala()
            for idSala, nombresala in listaSala:
                cantHorario = bd.transformarNumero(str(bd.cantidad_idSala_de_horario(idSala)))
                print("SALA: ",nombresala)
                if(cantHorario > 0):
                    lista_horario = bd.devolver_id_entrada_titulo_nombreSala_horario()
                    for id, entrada, titulo, nombreSala in lista_horario:
                        if(nombreSala == nombresala):
                            entrada = datetime.strptime(entrada,"%Y-%m-%d %H:%M:%S")
                            fecha = datetime.strftime(entrada,"%Y-%m-%d")
                            hora =  datetime.strftime(entrada,"%H:%M:%S")
                            print(f"Nro: {id} || Titulo: {titulo} || Fecha: {fecha} Hora: {hora} || Sala: {nombreSala}")
                else:
                    print("No tiene horario")
        else:
            print("No hay Sala")

