from gato.juego import Juego
jugar = Juego()
class Gato_Menu:
    def __init__(self):
        # seleccion = input("¿Desea usar conexión a la base de datos? (s/n)")
        opcion = input("---- MENU ----\n"
                    + "1. - Jugar\n"
                    + "2. - Salir\n")
        while opcion != '3':
                if opcion == '1':
                    jugar.posiciones()
                elif opcion == '2':
                    print("OPCION 1")
                opcion = input("---- MENU ----\n"
                            + "1. - Jugar\n"
                            + "2. - Salir\n")
