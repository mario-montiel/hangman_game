# import numeric
import numpy as np
class Juego:
    # juego = Juego()
    intentos = 1
    jugador = 0
    turno = 0
    tablero = np.array([['*',' *', '*'], ['*', '*', '*'], ['*', '*', '*']])
    position = list(set(['01', '02', '03', '11', '12', '13', '21', '22', '23']))
    def posiciones(self):
        while self.intentos > 0:
            self.turnos()
            # posicion = input("SELECCIONE LA POSICIÓN \n"
            # + "[* - * - *\n"
            # + " * - * - *\n"
            # + " * - * - *]\n")
            posicion = input("SELECCIONA UNA POSICIÓN\n" + str(self.position) + "\n")

            # print(posicion[0])
            self.tablero[0,1] =  "x"
            print(self.tablero)
            print(self.position)
            # for i in range(len(self.tablero)):
            #     for j in range(len(self.tablero[i])):
            #         print(self.tablero[i][j], end=' ')
            self.turno += 1

    def turnos(self):
        if self.turno % 2:
            print("Jugador2")
        else:
            print("Jugador1")
        # if turno == 0:
    # def intentos(self):

    # def dibujo (self):
        # if posicion == '00'
