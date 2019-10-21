import os
from ahorcado.ingresar import Ingresar
from ahorcado.jugar import Jugar
from ahorcado.palabra_aleatoria import Palabra_Aleatoria
from prints.prints import Print

jugar = Jugar()
ingresar = Ingresar("palabras.txt")
prints = Print()

class Ahorcado_Menu:
    def __init__(self):
        print(" --------------- !!!JUEGO DEL AHORCADO!!!  ------------------\n")
        x = prints.ahorcado_seleccion_db()
        menu = prints.ahorcado_menu()
        while menu != '3':
            if menu == '0':
                ingresar = Ingresar("palabras.txt")
                if x != 'n':
                    try:
                        from database.bd import Conexion
                        db = Conexion()
                        db.database(1)
                    except:
                        print("\nNO SE ENCUENTRÓ NINGUNA BASE DE DATOS\n")
                    ingresar.ver_lista()
                    menu = prints.ahorcado_menu()
                else:
                    ingresar.ver_lista()
                    menu = prints.ahorcado_menu()
            elif menu == '1':
                ingresar.ingresarnombre()
                menu = prints.ahorcado_menu()
            elif menu == '2':
                aleatorio = Palabra_Aleatoria("palabras.txt", "juego.txt")
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
            else:
                print("INGRESE UNA NÚMERO DEL MENÚ CORRECTAMENTE")
                menu = prints.ahorcado_menu()