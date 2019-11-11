# import numeric
import sys
import os
import numpy as np

class Juego:
    intentos = 0
    jugador = ""
    turno = 0
    tablero = np.array(
        [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']])
    board = ""
    position = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    derrota_mortal = 0
    validar = 0

    def posiciones(self, posicion):
        self.turnos()
        
        # Cambiamos el número de la posición del arreglo position por el
        # símbolo dependiendo el turno del jugador
        if self.jugador == "TURNO:JUGADOR 1 (x)":
            # Verificamos si se quiere poner una ubicación correcta en el tablero
            if len(posicion) == 2 and 0 <= int(posicion[0]) <= 2 and 0 <= int(posicion[1]) <= 2:
                posicion1 = int(posicion[0])
                posicion2 = int(posicion[1])
                self.tablero[posicion1, posicion2] = "x"
                # Eliminamos el elemento ingresado del array position
                for i in self.position:
                    if i == posicion:
                        self.validar = 0
                        self.position.remove(str(posicion))
                    if i != posicion:
                        self.validar = 1
                self.turno += 1
            else:
                self.derrota_mortal = 1
                return 1
            
        elif self.jugador == "TURNO: JUGADOR 2 (o)":
            # Verificamos si se quiere poner una ubicación correcta en el tablero
            if len(posicion) == 2 and 0 <= int(posicion[0]) <= 2 and 0 <= int(posicion[1]) <= 2:
                posicion1 = int(posicion[0])
                posicion2 = int(posicion[1])
                self.tablero[posicion1, posicion2] = "o"
                # Eliminamos el elemento ingresado del array position
                for i in self.position:
                    if i == posicion:
                        self.validar = 0
                        self.position.remove(str(posicion))
                    else:
                        self.validar = 1
                self.turno += 1
            else:
                self.derrota_mortal = 1
                return 1
            
        self.dibujo()
        self.ganarJugador1()
        self.ganarJugador2()

    def turnos(self):
        if self.turno % 2:
            self.jugador = "TURNO: JUGADOR 2 (o)"
            return self.jugador
        else:
            self.jugador = "TURNO:JUGADOR 1 (x)"
            return self.jugador

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
        return self.board

    def ganarJugador1(self):
        if self.tablero[0, 0] == 'x' and self.tablero[0, 1] == 'x' and self.tablero[0, 2] == 'x':
            self.intentos = 1
        elif self.tablero[1, 0] == 'x' and self.tablero[1, 1] == 'x' and self.tablero[1, 2] == 'x':
            self.intentos = 1
        elif self.tablero[2, 0] == 'x' and self.tablero[2, 1] == 'x' and self.tablero[2, 2] == 'x':
            self.intentos = 1
        elif self.tablero[0, 0] == 'x' and self.tablero[1, 1] == 'x' and self.tablero[2, 2] == 'x':
            self.intentos = 1
        elif self.tablero[2, 0] == 'x' and self.tablero[1, 1] == 'x' and self.tablero[0, 2] == 'x':
            self.intentos = 1
        elif self.tablero[0, 0] == 'x' and self.tablero[1, 0] == 'x' and self.tablero[2, 0] == 'x':
            self.intentos = 1
        elif self.tablero[0, 1] == 'x' and self.tablero[1, 1] == 'x' and self.tablero[2, 1] == 'x':
            self.intentos = 1
        elif self.tablero[0, 2] == 'x' and self.tablero[1, 2] == 'x' and self.tablero[2, 2] == 'x':
            self.intentos = 1
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
            [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']])
        self.intentos = 0
        self.derrota_mortal = 0
        self.validar = 0
        self.position = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        self.posiciones
