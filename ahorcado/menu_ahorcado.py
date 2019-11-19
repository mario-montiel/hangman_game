import os
from ahorcado.ingresar import Ingresar
from ahorcado.jugar import Jugar
from ahorcado.palabra_aleatoria import Palabra_Aleatoria
import pygame
from pygame.locals import *

ingresar = Ingresar("palabras.txt")


class Ahorcado_Menu:
    def __init__(self):
        print("!-------------------- AHORCADO --------------------------!")
        print("------ EMPECEMOS -------")
        menu = input("---- MENU ----\n"
        + "0. - Ver las palabras ingresadas \n"
        + "1. - Ingresar Palabra\n"
        + "2. - Jugar\n"
        + "3. - Salir\n")
        while menu != '3':
            if menu == '0':
                ingresar = Ingresar("palabras.txt")
                try:
                    from database.bd import Conexion
                    db = Conexion()
                    db.database(1)
                    print("LISTAS DE LA BASE DE DATOS Y DEL TEXTO: " + ingresar.ver_lista())
                except:
                    print("NO SE HA ENCONTRADO NINGUNA BASE DE DATOS MY FRIEND")
                menu = input("---- MENU ----\n"
                + "0. - Ver las palabras ingresadas \n"
                + "1. - Ingresar Palabra\n"
                + "2. - Jugar\n"
                + "3. - Salir\n")
                ingresar.ver_lista()
                menu = input("---- MENU ----\n"
                    + "0. - Ver las palabras ingresadas \n"
                    + "1. - Ingresar Palabra\n"
                    + "2. - Jugar\n"
                    + "3. - Salir\n")
            elif menu == '1':
                ingresar = Ingresar("palabras.txt")
                respuesta = input("¿DESEA AGREGAR PALABRA? (s/n)\n")
                while respuesta.lower() != 'n':
                    palabra = input("INGRESE UNA PALABRA\n")
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
                from database.bd import Conexion
                db = Conexion()
                aleatorio = Palabra_Aleatoria("palabras.txt", "juego.txt")
                aleatorio.palabra = ""
                aleatorio.seleccionarpalabra()
                print(" ----- EMPECEMOS ------")
                usuario = input("\n INGRESE UN USUARIO: \n")
                
                try:
                    from database.bd import Conexion
                    db = Conexion()
                    db.usuario = usuario
                    db.database(3)
                    db.palabra = x
                except:
                    print("NO SE HA ENCONTRADO NINGUNA BASE DE DATOS MY FRIEND")
                jugar = Jugar()
                jugar.usuario = usuario
                x = aleatorio.palabra
                
                jugar.palabra = x
                jugar.limpiar()
                while jugar.derrota_final() != 1 and jugar.victoria_final() != 1:
                    letra = input("\nINGRESE UNA LETRA: \n")
                    # os.system('cls')
                    jugar.encuentra(letra)
                    print(jugar.arreglo())
                    jugar.derrota_final()
                    jugar.pygame()
                try:
                    db.database(x)
                except:
                    print("SOLO PODRÁ JUGAR CON LA LISTA DEL ARCHIVO MY FRIEND")
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
            elif menu == 3:
                nuevo_usuario = input("Ingrese el nuevo Usuario")
            else:
                print("Selecciona una opción correcta")
                menu = input("---- MENU ----\n"
                    + "0. - Ver las palabras ingresadas \n"
                    + "1. - Ingresar Palabra\n"
                    + "2. - Jugar\n"
                    + "3. - Salir\n")
