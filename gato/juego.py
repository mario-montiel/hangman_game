# import numeric
import os
import numpy as np
from prints.prints import Print
prints = Print()
class Juego:
    # juego = Juego()
    intentos = 0
    jugador = ""
    turno = 0
    tablero = np.array([['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']])
    position = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    posicion = 0
    def posiciones(self):
        while self.intentos <= 0:
            self.turnos()
            posicion = prints.posicion(str(self.position))
            os.system('cls')

            # Cambiamos el número de la posición del arreglo position por el
            # símbolo dependiendo el turno del jugador
            if self.jugador == "JUGADOR 1 (x)":
                #Verificamos si se quiere poner una ubicación correcta en el tablero
                if int(posicion[0]) < 0 or int(posicion[0]) > 2 or int(posicion[1]) < 0 or int(posicion[1]) > 2:
                    while int(posicion[0]) < 0 or int(posicion[0]) > 2 or int(posicion[1]) < 0 or int(posicion[1]) > 2:
                        prints.rango_fuera_del_indicado()
                        # os.system('cls')
                        prints.ingrese_caracteres_correctos()
                        posicion = prints.posicion(str(self.position))
                if len(posicion) == 2:
                    posicion1 = int(posicion[0])
                    posicion2 = int(posicion[1])
                else:
                    while len(posicion) != 2:
                        os.system('cls')
                        prints.ingrese_caracteres_correctos()
                        posicion = prints.posicion(str(self.position))
                if self.tablero[posicion1, posicion2] ==  "x" or self.tablero[posicion1, posicion2] ==  "o":
                    prints.se_repite()
                else:
                    self.tablero[posicion1, posicion2] =  "x"
                    # Eliminamos el elemento ingresado del array position
                    self.position.remove(posicion)
                    self.turno += 1
            else:
                #Verificamos si se quiere poner una ubicación correcta en el tablero
                if len(posicion) == 2:
                    posicion1 = int(posicion[0])
                    posicion2 = int(posicion[1])
                else:
                    while len(posicion) != 2:
                        os.system('cls')
                        prints.ingrese_caracteres_correctos()
                        posicion = prints.posicion(str(self.position))
                if self.tablero[posicion1, posicion2] ==  "x" or self.tablero[posicion1, posicion2] ==  "o":
                    prints.misma_posicion()
                else:
                    self.tablero[posicion1, posicion2] =  "o"
                    # Eliminamos el elemento ingresado del array position
                    self.position.remove(posicion)
                    self.turno += 1

            self.ganar()

            if len(self.position) == 0:
                prints.nadie_gano()
                break

            print(self.tablero)
        self.limpiar()

    def turnos(self):
        if self.turno % 2:
            self.jugador = "JUGADOR 2 (o)"
            print(self.jugador)
        else:
            self.jugador = "JUGADOR 1 (x)"
            print(self.jugador)

    def ganar(self):
        if self.tablero[0,0] == 'x' and self.tablero[0,1] == 'x' and self.tablero[0,2] == 'x' or self.tablero[0,0] == 'o' and self.tablero[0,1] == 'o' and self.tablero[0,2] == 'o':
            self.intentos = 1
            prints.ganaste(str(self.jugador))
        elif self.tablero[1,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[1,2] == 'x' or self.tablero[1,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[1,2] == 'o':
            self.intentos = 1
            prints.ganaste(str(self.jugador))
        elif self.tablero[2,0] == 'x' and self.tablero[2,1] == 'x' and self.tablero[2,2] == 'x' or self.tablero[2,0] == 'o' and self.tablero[2,1] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            prints.ganaste(str(self.jugador))
        elif self.tablero[0,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[2,2] == 'x' or self.tablero[0,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            prints.ganaste(str(self.jugador))
        elif self.tablero[2,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[0,2] == 'x' or self.tablero[2,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[0,2] == 'o':
            self.intentos = 1
            prints.ganaste(str(self.jugador))
        elif self.tablero[0,0] == 'x' and self.tablero[1,0] == 'x' and self.tablero[2,0] == 'x' or self.tablero[0,0] == 'o' and self.tablero[1,0] == 'o' and self.tablero[2,0] == 'o':
            self.intentos = 1
            prints.ganaste(str(self.jugador))
        elif self.tablero[0,1] == 'x' and self.tablero[1,1] == 'x' and self.tablero[2,1] == 'x' or self.tablero[0,1] == 'o' and self.tablero[1,1] == 'o' and self.tablero[2,1] == 'o':
            self.intentos = 1
            prints.ganaste(str(self.jugador))
        elif self.tablero[0,2] == 'x' and self.tablero[1,2] == 'x' and self.tablero[2,2] == 'x' or self.tablero[0,2] == 'o' and self.tablero[1,2] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            prints.ganaste(str(self.jugador))

    def limpiar(self):
        self.tablero = np.array([['*',' *', '*'], ['*', '*', '*'], ['*', '*', '*']])
        self.intentos = 0
        self.position = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        self.posiciones
        self.posicion = 0