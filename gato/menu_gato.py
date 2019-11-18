from gato.juego import Juego
import os
import pygame 
jugar = Juego()
class Gato_Menu:
    def __init__(self):
        # seleccion = input("¿Desea usar conexión a la base de datos? (s/n)")
        opcion = input("---- MENU ----\n"
                        + "1. - Jugar\n"
                        + "2. - Salir\n")
        while opcion != '2':

                if opcion == '1':
                    from database.bd import Conexion
                    db = Conexion()
                    while str(jugar.ganarJugador1()) <= '0':
                        jugar.validar = 0
                        coordenadas = str(jugar.position)
                        print("\n ---- ¡¡ " + str(jugar.turnos()) + " !! ---- " + "\n" + str(jugar.dibujo()))
                        posicion = input("SELECCIONA UNA POSICIÓN\n" + str(coordenadas) + "\n")
                        
                        jugar.posiciones(posicion)
                        if jugar.derrota_mortal == 1:
                            print("\nINGRESE UNA POSICIÓN VÁLIDA...")
                            jugar.derrota_mortal = 0
                        jugar.pygame()
                    if jugar.intentos == 1:
                        print("\n ---- ¡¡ GANASTE JUGADOR 1 ( x ) !! ---- " + "\n")
                        # print(jugar.board)
                        try:
                            db.database('x')
                        except:
                            print("NO SE ENCONTRÓ NINGUNA BASE DE DATOSx")
                    if jugar.intentos == 2:
                        print("\n ---- ¡¡ GANASTE JUGADOR 2 ( 0 ) !! ---- " + "\n")
                        # print(jugar.board)
                        try:
                            db.database('o')
                        except:
                            print("NO SE ENCONTRÓ NINGUNA BASE DE DATOSo")
                    jugar.limpiar()
                    
                elif opcion == '2':
                    break
                opcion = input("---- MENU ----\n"
                                + "1. - Jugar\n"
                                + "2. - Salir\n")
