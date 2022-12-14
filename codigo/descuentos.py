from creacion_basedatos import crear_base_datos as bd

class descuento:
    def __init__(self, idDescuentos, dia, porcentaje):
        self.__idDescuentos = idDescuentos
        self.__dia = dia
        self.__porcentaje = porcentaje
    def __str__(self):
        cadena = "\nId Descuentos: " + self.__idDescuentos
        cadena+= "\nDia: " + self.__dia
        cadena+= "\nPorcentaje: " + self.__porcentaje
        return cadena
    
    @property
    def getIdDescuentos(self):
        return self.__idDescuentos
    @property
    def getDia(self):
        return self.__dia
    @property
    def getPorcentaje(self):
        return self.__porcentaje
        
    #@setDia.setter
    def setDia (self, nuevoDia):
        self.__dia = nuevoDia
    #@setPorcentaje.setter
    def setPorcentaje (self, nuevoPorcentaje):
        self.__porcentaje = nuevoPorcentaje
    
    @classmethod
    def mostrar_descuentos(self):
        if (bd.listaVacia("descuento") == False):
            listaDescuento = bd.lista_descuentos()
            for descuento in listaDescuento:
                dia , porcentaje = descuento
                print(f"Dia: {str.upper(dia)}  hay descuento de {porcentaje}")
        else:
            print("No hay dia de descuentos")

    @classmethod
    def modicar_descuentos(self):
        if (bd.listaVacia("descuento") == False):
            dia = int(input("1-LUNES\n2-MARTES\n3-MIERCOLES\n4-JUEVES\n5-VIERNES\n6-SABADO\n7-DOMINGO : "))
            if(dia == 1 or dia == 2 or dia == 3 or dia == 4 or dia == 5 or dia == 6 or dia == 7):
                porcentaje = float(input("Ingresar porcentaje nuevo \nEjemplo 0.2 : "))
                if(type(porcentaje) == float):
                    bd.modificar_porcentade_descuento(dia, porcentaje)
                else:
                    print("Igreso erroneo tipo de dato ingresado no es número real")
            else:
                print("Ingreso un dia erroneo")
        else:
            print("No hay dia de descuentos")