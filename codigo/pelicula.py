from creacion_basedatos import crear_base_datos as bd

class Pelicula:
    def __init__(self, idPelicula, titulo, genero, duracion, categoria, formato):
        self.__idPelicula = idPelicula
        self.__titulo = titulo
        self.__genero = genero
        self.__duracion = duracion
        self.__categoria = categoria
        self.__formato = formato

    def __str__(self):
        cadena = "\nId Pelicula: " + self.__idPelicula
        cadena+= "\nTitulo: " + self.__titulo
        cadena+= "\nGenero: " + self.__genero
        cadena+= "\nDuracion: " + self.__duracion
        cadena+= "\ncategoria: " + self.__categoria
        cadena+= "\nFormato: " + self.__formato
        return cadena
    
    @property
    def getIdPelicula(self):
        return self.__idPelicula
    @property
    def getTitulo(self):
        return self.__titulo
    @property
    def getGenero(self):
        return self.__genero
    @property
    def getDuracion(self):
        return self.__duracion
    @property
    def getCategoria(self):
        return self.__categoria
    @property
    def getFormato(self):
        return self.__formato
    
   # @setTitulo.setter
    def setTitulo (self,nuevoTitulo):
        self.__titulo = nuevoTitulo
    #@setGenero.setter
    def setGenero (self,nuevoGenero):
        self.__genero = nuevoGenero
    #@setDuracion.setter
    def setDuracion (self,nuevaDuracion):
        self.__duracion = nuevaDuracion
    #@setCategoria.setter
    def setCategoria (self,nuevoCategoria):
        self.__categoria = nuevoCategoria
    #@setFormato.setter
    def setFormato (self,nuevoFormato):
        self.__formato = nuevoFormato
    

    @classmethod
    def crear_Pelicula (self):
        id = bd.devolver_ID("idPelicula","pelicula")
        titulo = input("Titulo de la pelicula: ")
        genero = input("Genero de la pelicula: ")
        duracion_Pelicula = bd.crearHora()
        categoria = bd.transformarNumero(input("1-Apto para Todo Publico\n2-Mayor 13años\n3-Mayor 16 años\n4-Mayor de 18 años: "))
        while(categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4 ):
                    categoria = bd.transformarNumero(input("1-Apto para Todo Publico\n2-Mayor 13años\n3-Mayor 16 años\n4-Mayor de 18 años: "))
        formato = bd.transformarNumero(input("1- 2D \n2- 3D: "))
        while(formato != 1 and formato != 2 and formato != 3 and formato != 4 ):
                    formato = bd.transformarNumero(input("1- 2D \n2- 3D: "))
        
        bd.cargar_pelicula(id, titulo, genero, duracion_Pelicula, categoria, formato)

    @classmethod
    def modificar_Pelicula (self):
        if(bd.listaVacia("pelicula") == False):
            idDado = self.mostrarPeliculas()
            titulo = input("Titulo de la pelicula: ")
            genero = input("Genero de la pelicula: ")
            duracion_Pelicula = bd.crearHora()
            categoria = bd.transformarNumero(input("Elegir una opcion:\n1-Apto para Todo Publico\n2-Mayor 13años\n3-Mayor 16 años\n4-Mayor de 18 años: "))
            print("categoria " , categoria , type(categoria))
            while(categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4 ):
                categoria = bd.transformarNumero(input("Elegir una opcion:\n1-Apto para Todo Publico\n2-Mayor 13años\n3-Mayor 16 años\n4-Mayor de 18 años: "))
            formato = bd.transformarNumero(input("Elegir una opcion:\n1- 2D \n2- 3D: "))
            while(formato != 1 and formato != 2 and formato != 3 and formato != 4 ):
                formato = bd.transformarNumero(input("Elegir una opcion:\n1- 2D \n2- 3D: "))
            bd.modificar_pelicula(idDado, titulo, genero, duracion_Pelicula, categoria, formato)
        else:
            print("No hay Sala")

    @classmethod
    def eliminar_Pelicula (self):
        if(bd.listaVacia("pelicula") == False):
            idDado = self.mostrarPeliculas()
            if(bd.cantidad_idPelicula_reservas(idDado) == 0 and bd.cantidad_idPelicula_horario(idDado) == 0):
                bd.eliminar_pelicula(idDado)
            else:
                print("No se puede eliminar ya que la pelicula esta siendo ocupada")
        else:
            print("No hay Pelicula")
            
    
    @classmethod
    def existe_Pelicula (self,id): # id debe ser Entero
        bandera = False
        if(bd.listaVacia("pelicula") == False):
            todasPelicula = bd.lista_id_pelicula()
            for idPeli in todasPelicula:
                compara = bd.transformarNumero(str(idPeli))
                if(id == compara):
                    bandera = True
                    break
        return bandera

    @classmethod
    def mostrarPeliculas (self):
        listaPelicula = bd.devolver_id_titulo_pelicula()
        seguir = True
        while(seguir):
            print("Elija una opcion: ")
            for pelicula in listaPelicula:
                id, titulo = pelicula
                print(f"{id}- Pelicula: {titulo}")
            idDado = bd.transformarNumero(input("ingrese un número: "))
            if(type(idDado) == int):
                if(self.existe_Pelicula(idDado)):
                    seguir = False
                    return idDado
                else:
                    print("No existe la sala ingresada")
            else:
                print("No ingreso un número")
