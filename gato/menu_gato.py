from gato.juego import Juego
import os
from prints.prints import Print
prints = Print()
jugar = Juego()
class Gato_Menu:
    def __init__(self):
        # seleccion = input("¿Desea usar conexión a la base de datos? (s/n)")
        opcion = input("---- MENU ----\n"
                        + "1. - Jugar\n"
                        + "2. - Salir\n")
        while opcion != '2':

                if opcion == '1':
                    coordenadas = jugar.position
                    while jugar.intentos <= 0:
                        posicion = input("SELECCIONA UNA POSICIÓN\n" + str(coordenadas) + "\n")
                        jugar.posiciones(posicion)
                    if jugar.ganarJugador1 == 1:
                        print("GANASTE JUGADOR 1 ( x )")
                    if jugar.ganarJugador2 == 2:
                        print("GANASTE JUGADOR 1 ( 0 )")
                    
                    
                    opcion = input("---- MENU ----\n"
                                    + "1. - Jugar\n"
                                    + "2. - Salir\n")
                elif opcion == '2':
                    break
                opcion = input("---- MENU ----\n"
                                + "1. - Jugar\n"
                                + "2. - Salir\n")
