from gato.juego import Juego
import os
from prints.prints import Print
prints = Print()
jugar = Juego()
class Gato_Menu:
    def __init__(self):
        # seleccion = input("¿Desea usar conexión a la base de datos? (s/n)")
        opcion = prints.menu_gato()
        while opcion != '2':
                if opcion == '1':
                    jugar.posiciones()
                elif opcion == '2':
                    break
                opcion = prints.menu_gato()
