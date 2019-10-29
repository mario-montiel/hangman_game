# import numeric
import sys
import os
from prints.prints import Print
import numpy as np
prints = Print()


class Juego:
    intentos = 0
    jugador = ""
    turno = 0

    tablero = np.array(
        [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']])
    board = ""

    position = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    posicion = 0

    def posiciones(self, posicion):
        self.turnos()

        # Cambiamos el número de la posición del arreglo position por el
        # símbolo dependiendo el turno del jugador
        if self.jugador == "TURNO:JUGADOR 1 (x)":
            # Verificamos si se quiere poner una ubicación correcta en el tablero
            # self.condicion_jugador1()
            if len(posicion) == 2:
                posicion1 = int(posicion[0])
                posicion2 = int(posicion[1])
            # else:
            #     while len(posicion) != 2:
            #         os.system('cls')
            #         prints.ingrese_caracteres_correctos()
            #         posicion = prints.posicion(str(self.position))
            # if self.tablero[posicion1, posicion2] == "x" or self.tablero[posicion1, posicion2] == "o":
            #     prints.se_repite()
            # else:
            self.tablero[posicion1, posicion2] = "x"
                # Eliminamos el elemento ingresado del array position
            self.position.remove(posicion)
            self.turno += 1
        else:
            # Verificamos si se quiere poner una ubicación correcta en el tablero
            if len(posicion) == 2:
                posicion1 = int(posicion[0])
                posicion2 = int(posicion[1])
            # else:
            #     while len(posicion) != 2:
            #         os.system('cls')
            #         prints.ingrese_caracteres_correctos()
            #         posicion = prints.posicion(str(self.position))
            # if self.tablero[posicion1, posicion2] == "x" or self.tablero[posicion1, posicion2] == "o":
            #     prints.misma_posicion()
            # else:
            self.tablero[posicion1, posicion2] = "o"
                # Eliminamos el elemento ingresado del array position
            self.position.remove(posicion)
            self.turno += 1
        self.dibujo()
        # self.ganar()

        if len(self.position) == 0:
            print("asdf")
            # break

        # self.limpiar()
        
    # def condicion_jugador1(self):
    #     if int(posicion[0]) < 0 or int(posicion[0]) > 2 or int(posicion[1]) < 0 or int(posicion[1]) > 2:
    #         while int(posicion[0]) < 0 or int(posicion[0]) > 2 or int(posicion[1]) < 0 or int(posicion[1]) > 2:
    #             return str(self.position)

    def turnos(self):
        if self.turno % 2:
            self.jugador = "TURNO: JUGADOR 2 (o)"
            # print(self.jugador)
            prints.jugador(self.jugador)
        else:
            self.jugador = "TURNO:JUGADOR 1 (x)"
            # print(self.jugador)
            prints.jugador(self.jugador)

    def dibujo(self):
        self.board = '''
        -------  ------  ----
        |  ''' + self.tablero[0, 0] + '''  |  ''' + self.tablero[0, 1] + '''  |  ''' + self.tablero[0, 2] + '''  |    
        -------  ------  ----
        |  ''' + self.tablero[1, 0] + '''  |  ''' + self.tablero[1, 1] + '''  |  ''' + self.tablero[1, 2] + '''  |    
        -------  ------  ----
        |  ''' + self.tablero[2, 0] + '''  |  ''' + self.tablero[2, 1] + '''  |  ''' + self.tablero[2, 2] + '''  | 
        -------  ------  ---- 
        '''
        # sys.stdout.write(str(self.board))

    def ganarJugador1(self):
        if self.tablero[0, 0] == 'x' and self.tablero[0, 1] == 'x' and self.tablero[0, 2] == 'x':
            self.intentos = 1
            # prints.ganaste(str(self.jugador))
        elif self.tablero[1, 0] == 'x' and self.tablero[1, 1] == 'x' and self.tablero[1, 2] == 'x':
            self.intentos = 1
            # prints.ganaste(str(self.jugador))
        elif self.tablero[2, 0] == 'x' and self.tablero[2, 1] == 'x' and self.tablero[2, 2] == 'x':
            self.intentos = 1
            # prints.ganaste(str(self.jugador))
        elif self.tablero[0, 0] == 'x' and self.tablero[1, 1] == 'x' and self.tablero[2, 2] == 'x':
            self.intentos = 1
            # prints.ganaste(str(self.jugador))
        elif self.tablero[2, 0] == 'x' and self.tablero[1, 1] == 'x' and self.tablero[0, 2] == 'x':
            self.intentos = 1
            # prints.ganaste(str(self.jugador))
        elif self.tablero[0, 0] == 'x' and self.tablero[1, 0] == 'x' and self.tablero[2, 0] == 'x':
            self.intentos = 1
            # prints.ganaste(str(self.jugador))
        elif self.tablero[0, 1] == 'x' and self.tablero[1, 1] == 'x' and self.tablero[2, 1] == 'x':
            self.intentos = 1
            # prints.ganaste(str(self.jugador))
        elif self.tablero[0, 2] == 'x' and self.tablero[1, 2] == 'x' and self.tablero[2, 2] == 'x':
            self.intentos = 1
            # prints.ganaste(str(self.jugador))
        return self.intentos
            
    def ganarJugador2(self):
        if self.tablero[0, 0] == 'o' and self.tablero[0, 1] == 'o' and self.tablero[0, 2] == 'o':
            self.intentos = 2
        elif self.tablero[1, 0] == 'o' and self.tablero[1, 1] == 'o' and self.tablero[1, 2] == 'o':
            self.intentos = 2
        elif self.tablero[2, 0] == 'o' and self.tablero[2, 1] == 'o' and self.tablero[2, 2] == 'o':
            self.intentos = 2
        elif self.tablero[0, 0] == 'o' and self.tablero[1, 1] == 'o' and self.tablero[2, 2] == 'o':
            self.intentos = 2
        elif self.tablero[2, 0] == 'o' and self.tablero[1, 1] == 'o' and self.tablero[0, 2] == 'o':
            self.intentos = 2
        elif self.tablero[0, 0] == 'o' and self.tablero[1, 0] == 'o' and self.tablero[2, 0] == 'o':
            self.intentos = 2
        elif self.tablero[0, 1] == 'o' and self.tablero[1, 1] == 'o' and self.tablero[2, 1] == 'o':
            self.intentos = 2
        elif self.tablero[0, 2] == 'o' and self.tablero[1, 2] == 'o' and self.tablero[2, 2] == 'o':
            self.intentos = 2
        return self.intentos
            
    def limpiar(self):
        self.tablero = np.array(
            [['*', ' *', '*'], ['*', '*', '*'], ['*', '*', '*']])
        self.intentos = 0
        self.position = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        self.posiciones
        self.posicion = 0
