import os
from usuario import Usuario
from reserva import reserva
from descuentos import descuento
from pelicula import Pelicula
from sala import Sala
from horario import horario
from creacion_basedatos import crear_base_datos as bd
from datetime import datetime 


try:
    # conexion = sqlite3.connect("baseDatos_1")
    bd.crear_tabla_usuario()
    bd.crear_tabla_pelicula()
    bd.crear_tabla_sala()
    bd.crear_tabla_horario()
    bd.crear_tabla_asientos()
    bd.crear_tabla_descuento()
    bd.crear_tabla_reserva()
    bd.crear_tabla_todasReservas()

except SyntaxError:
    print("Un Error de creacion de la base de datos")
    
seguir = True 

while(seguir):
    input("Presione enter para volver al menu") # borrar pantalla
    os.system ("cls") # borrar pantalla
                            

    #VARIABLES
    menu_cliente = -1
    fecha_actual = datetime.now()
    fecha = datetime.strftime(fecha_actual,"%Y-%m-%d")
    hora =  datetime.strftime(fecha_actual,"%H:%M:%S")
    print (f"\nFECHA: {fecha} \t\t\t HORA: {hora}")
    
    menu = bd.transformarNumero(input("\n1-Crear cuenta\n2-Iniciar Sesión\n3-Ver Salas\n0-Salir: "))

    if(menu == 1):
        cuenta = Usuario.crear_cuenta()
    elif (menu == 2):
        id = Usuario.iniciarSesion()
        if(id != -1):
            if(bd.administracion_usuario(id) == 0): # MENU DE CLIENTE
                seguir_en_cuenta = True
                while(seguir_en_cuenta):
                    input("Presione enter para volver al menu") # borrar pantalla
                    os.system ("cls") # borrar pantalla

                    menu_cliente = bd.transformarNumero(input("\n1-Crear una reserva\n2-Modificar una reserva\n3-Observar ultima reserva\n4-Historial de reservas\n0-Salir: "))
                    print("\n")
                    if(menu_cliente == 1):
                        reserva.crear_reserva(id)
                    elif(menu_cliente == 2):
                        reserva.modificar_reserva(id)
                    elif(menu_cliente == 3):
                        reserva.mostrar_ultima_reserva(id)
                    elif(menu_cliente == 4):
                        reserva.opcion_mostrar_historial(id)
                    elif(menu_cliente == 0):
                        seguir_en_cuenta = False
                    else:
                        print("Elija Nuevamente una opcion")
            elif (bd.administracion_usuario(id) == 1):  # MENU DE ADMIN
                seguir_en_cuenta = True
                while(seguir_en_cuenta):
                    input("Presione enter para volver al menu") # borrar pantalla
                    os.system ("cls") # borrar pantalla

                    menu_admin = bd.transformarNumero(input("\n1-Reserva\n2-Sala\n3-Descuento\n4-Pelicula\n5-Horario\n0-Salir: "))
                    print(menu_admin)
                    if(menu_admin == 1): # MENU RESERVA 
                        seguir_en_opcion = True
                        while(seguir_en_opcion):
                            input("Presione enter para volver al menu") # borrar pantalla
                            os.system ("cls") # borrar pantalla

                            menu_reserva = int(input("\n1-Ver todas las reservas\n2-Ver una reserva\n0-Salir: "))
                            if(menu_reserva == 1):
                                reserva.ver_todas_reservas()    
                            elif(menu_reserva == 2):
                                reserva.opcion_ver_una_reserva()
                            elif(menu_reserva == 0):
                                seguir_en_opcion = False
                            else:
                                print("Elija Nuevamente una opcion")

                    elif(menu_admin == 2): # MENU SALA
                        seguir_en_opcion = True
                        while(seguir_en_opcion):
                            input("Presione enter para volver al menu") # borrar pantalla
                            os.system ("cls") # borrar pantalla

                            menu_sala = bd.transformarNumero(input("\n1-Crear Sala\n2-Modificar Sala\n3-Eliminar Sala\n0-Salir: "))
                            if(menu_sala == 1):
                                Sala.crear_sala()
                            elif(menu_sala == 2):
                                Sala.modificar_sala()
                            elif(menu_sala == 3):
                                Sala.eliminar_sala()
                            elif(menu_sala == 0):
                                seguir_en_opcion = False
                            else:
                                print("Elija Nuevamente una opcion")
                    elif(menu_admin == 3): # MENU DESCUENTO
                        seguir_en_opcion = True
                        while(seguir_en_opcion):
                            input("Presione enter para volver al menu") # borrar pantalla
                            os.system ("cls") # borrar pantalla
                            
                            menu_descuento = bd.transformarNumero(input("\n1-Ver Descuentos\n2-Modificar Descuento\n0-Salir: "))
                            if(menu_descuento == 1):
                                descuento.mostrar_descuentos()
                            elif(menu_descuento == 2):
                                descuento.modicar_descuentos()
                            elif(menu_descuento == 0):
                                seguir_en_opcion = False
                            else:
                                print("Elija Nuevamente una opcion")
                    elif(menu_admin == 4): # MENU PELICULA
                        seguir_en_opcion = True
                        while(seguir_en_opcion):
                            input("Presione enter para volver al menu") # borrar pantalla
                            os.system ("cls") # borrar pantalla
                            

                            menu_pelicula = bd.transformarNumero(input("\n1-Crear pelicula\n2-Modificar pelicula\n3-Eliminar pelicula\n0-Salir: "))
                            if(menu_pelicula == 1):
                                Pelicula.crear_Pelicula()
                            elif(menu_pelicula == 2):
                                Pelicula.modificar_Pelicula()
                            elif(menu_pelicula == 3):
                                Pelicula.eliminar_Pelicula()
                            elif(menu_pelicula == 0):
                                seguir_en_opcion = False
                            else:
                                print("Elija Nuevamente una opcion")
                    elif(menu_admin == 5): # MENU HORARIO
                        seguir_en_opcion = True
                        while(seguir_en_opcion):
                            input("Presione enter para volver al menu") # borrar pantalla
                            os.system ("cls") # borrar pantalla
                            
                            menu_horario = bd.transformarNumero(input("\n1-Crear horario\n2-Modificar horario\n3-Eliminar horario\n0-Salir: "))
                            if(menu_horario == 1):
                                horario.crear_Horario()
                            elif(menu_horario == 2):
                                horario.modificar_horario()
                            elif(menu_horario == 3):
                                horario.eliminar_horario()
                            elif(menu_horario == 0):
                                seguir_en_opcion = False
                            else:
                                print("Elija Nuevamente una opcion")
                    elif(menu_admin == 0):
                        seguir_en_cuenta = False
                    else:
                        print("Elija Nuevamente una opcion")
                # MENU DEL ADMINISTRADOR
            else:
                print("No Permitido!!")
        else:
            pass
    elif (menu == 3):
        print("\n")
        Sala.opcion_ver_salas()
    else:
        seguir = False
