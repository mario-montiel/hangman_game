import os
from ahorcado.ingresar import Ingresar
from ahorcado.jugar import Jugar
from ahorcado.palabra_aleatoria import Palabra_Aleatoria
from prints.prints import Print

ingresar = Ingresar("palabras.txt")
prints = Print()


class Ahorcado_Menu:
    def __init__(self):
        # Print de "EMPECEMOS"
        # prints.juego_ahorcado()
        print("!-------------------- AHORCADO --------------------------!")
        # prints.empecemos()
        print("------ EMPECEMOS -------")
        # PRINT DE CONEXION A BD
        # x = prints.ahorcado_seleccion_db()
        x = input("¿Desea utilizar Base de Datos? (s/n)")
        # PRINT DE MENU
        # menu = prints.ahorcado_menu()
        menu = input("---- MENU ----\n"
        + "0. - Ver las palabras ingresadas \n"
        + "1. - Ingresar Palabra\n"
        + "2. - Jugar\n"
        + "3. - Salir\n")
        while menu != '3':
            if menu == '0':
                ingresar = Ingresar("palabras.txt")
                if x != 'n':
                    try:
                        from database.bd import Conexion
                        db = Conexion()
                        db.database(1)
                        print("LISTAS DE LA BASE DE DATOS Y DEL TEXTO: " + ingresar.ver_lista())
                    except:
                        # prints.sin_conexion()
                        print("NO SE HA ENCONTRADO NINGUNA BASE DE DATOS MY FRIEND")
                    menu = input("---- MENU ----\n"
                    + "0. - Ver las palabras ingresadas \n"
                    + "1. - Ingresar Palabra\n"
                    + "2. - Jugar\n"
                    + "3. - Salir\n")
                    # menu = prints.ahorcado_menu()
                else:
                    ingresar.ver_lista()
                    # menu = prints.ahorcado_menu()
                    menu = input("---- MENU ----\n"
                    + "0. - Ver las palabras ingresadas \n"
                    + "1. - Ingresar Palabra\n"
                    + "2. - Jugar\n"
                    + "3. - Salir\n")
            elif menu == '1':
                ingresar = Ingresar("palabras.txt")
                respuesta = input("¿DESEA AGREGAR PALABRA? (s/n)")
                while respuesta.lower() != 'n':
                    palabra = input("INGRESE UNA PALABRA")
                    try:
                        from database.bd import Conexion
                        db = Conexion()
                        db.database(palabra)
                        ingresar.ingresarnombre(palabra)
                        respuesta = input("¿DESEA AGREGAR OTRA PALABRA? (s/n)")
                    except:
                        print("NO SE ENCONTRÓ NINGUNA BASE DE DATOS")
                        break
                menu = input("---- MENU ----\n"
                    + "0. - Ver las palabras ingresadas \n"
                    + "1. - Ingresar Palabra\n"
                    + "2. - Jugar\n"
                    + "3. - Salir\n")
            elif menu == '2':
                aleatorio = Palabra_Aleatoria("palabras.txt", "juego.txt")
                aleatorio.palabra = ""
                aleatorio.seleccionarpalabra()
                # os.system('cls')
                print(" ----- EMPECEMOS ------")
                jugar = Jugar()
                x = aleatorio.palabra
                jugar.palabra = x
                jugar.limpiar()
                while jugar.derrota_final() != 1 and jugar.victoria_final() != 1:
                    letra = input("\nINGRESE UNA LETRA: \n")
                    jugar.encuentra(letra)
                    print(jugar.arreglo())
                    jugar.derrota_final()
                if jugar.derrota_final() == 1:
                    print("\n ---------- ¡¡ NO TIENES MÁS INTENTOS... REINICIA EL GAME PLEASE !! -------------\n")
                elif jugar.victoria_final() == 1:
                    print("\n ---------- ¡¡ COMPLETASTE EL JUEGO... GANASTE !! -------------\n")    
                
                print("Debe reiniciar el juego para poder continuar")
                menu = input("---- MENU ----\n"
                    + "0. - Ver las palabras ingresadas \n"
                    + "1. - Ingresar Palabra\n"
                    + "2. - Jugar\n"
                    + "3. - Salir\n")
            else:
                prints.seleccione_opc_correcta()
                menu = prints.ahorcado_menu()
