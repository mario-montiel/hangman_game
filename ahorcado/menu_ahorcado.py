import os
from ahorcado.ingresar import Ingresar
from ahorcado.jugar import Jugar
from ahorcado.palabra_aleatoria import Palabra_Aleatoria
from prints.prints import Print

jugar = Jugar()
aleatorio = Palabra_Aleatoria("palabras.txt", "juego.txt")
ingresar = Ingresar("palabras.txt")
prints = Print()

class Ahorcado_Menu:
    def __init__(self):
        print(" --------------- !!!JUEGO DEL AHORCADO!!!  ------------------\n")
        x = prints.ahorcado_seleccion_db()
        # seleccion = input("¿Desea usar conexión a la base de datos? (s/n)")
        menu = prints.ahorcado_menu()
        # opcion = input("---- MENU ----\n"
        # + "0. - Ver las palabras ingresadas \n"
        # + "1. - Ingresar Palabra\n"
        # + "2. - Jugar\n"
        # + "3. - Salir\n")
        while menu != '3':
            if menu == '0':
                if x != 'n':
                    try:
                        from database.bd import Conexion
                        db = Conexion()
                        db.database(1)
                    except:
                        print("\nNO SE ENCUENTRÓ NINGUNA BASE DE DATOS\n")
                    menu = prints.ahorcado_menu()
                else:
                    ingresar.ver_lista()
                    menu = prints.ahorcado_menu()
            elif menu == '1':
                ingresar.ingresarnombre()
                menu = prints.ahorcado_menu()
            elif menu == '2':
                aleatorio.palabra = ""
                aleatorio.aleatorio = []
                aleatorio.seleccionarpalabra()
                os.system('cls')
                print("La palabra adivinar es: " + str(aleatorio.aleatorio))
                print("-- !!EMPECEMOS!! --")
                jugar.palabra = aleatorio.palabra
                jugar.limpiar()
                jugar.encuentra()
                jugar.vidas()
                jugar.dibujar()
                print("Debe reiniciar el juego para poder seguir jugando\n")
                menu = prints.ahorcado_menu()
            # opcion = input("---- MENU ----\n"
            # + "0. - Ver Palabras Ingresadas en la bd\n"
            # + "1. - Ingresar Palabra\n"
            # + "2. - Jugar\n"
            # + "3. - Salir\n")
            # menu