# import numeric
import numpy as np
class Juego:
    # juego = Juego()
    intentos = 0
    jugador = ""
    turno = 0
    tablero = np.array([['*',' *', '*'], ['*', '*', '*'], ['*', '*', '*']])
    position = list(set(['00', '01', '02', '10', '11', '12', '20', '21', '22']))
    def posiciones(self):
        while self.intentos <= 0:
            self.turnos()
            # posicion = input("SELECCIONE LA POSICIÓN \n"
            # + "[* - * - *\n"
            # + " * - * - *\n"
            # + " * - * - *]\n")
            posicion = input("SELECCIONA UNA POSICIÓN\n" + str(self.position) + "\n")
            if len(posicion) > 2 or len(posicion) < 2:
                print("INGRESE LOS CARACTERES CORRECTOS PORFAVOR")
                break
            # print(posicion)
            print(str(posicion[0] + ',' + posicion[1]))

            # print(self.tablero[2,1])

            posicion1 = int(posicion[0])
            posicion2 = int(posicion[1])

            if self.jugador == "JUGADOR 1":
                self.tablero[posicion1, posicion2] =  "x"
            else:
                self.tablero[posicion1, posicion2] =  "o"

            print(self.tablero)
            self.turno += 1
            self.ganar()
        self.limpiar()

    def turnos(self):
        if self.turno % 2:
            self.jugador = "JUGADOR 2"
            print(self.jugador)
        else:
            self.jugador = "JUGADOR 1"
            print(self.jugador)
        # if turno == 0:
    def ganar(self):
        if self.tablero[0,0] == 'x' and self.tablero[0,1] == 'x' and self.tablero[0,2] == 'x' or self.tablero[0,0] == 'o' and self.tablero[0,1] == 'o' and self.tablero[0,2] == 'o':
            self.intentos = 1
            print("GANASTE " + self.jugador)
        elif self.tablero[1,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[1,2] == 'x' or self.tablero[1,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[1,2] == 'o':
            self.intentos = 1
            print("GANASTE")
        elif self.tablero[2,0] == 'x' and self.tablero[2,1] == 'x' and self.tablero[2,2] == 'x' or self.tablero[2,0] == 'o' and self.tablero[2,1] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            print("GANASTE")
        elif self.tablero[0,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[2,2] == 'x' or self.tablero[0,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            print("GANASTE")
        elif self.tablero[2,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[0,2] == 'x' or self.tablero[2,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[0,2] == 'o':
            self.intentos = 1
            print("GANASTE")
        elif self.tablero[0,0] == 'x' and self.tablero[1,0] == 'x' and self.tablero[2,0] == 'x' or self.tablero[0,0] == 'o' and self.tablero[1,0] == 'o' and self.tablero[2,0] == 'o':
            self.intentos = 1
            print("GANASTE")
        elif self.tablero[0,1] == 'x' and self.tablero[1,1] == 'x' and self.tablero[2,1] == 'x' or self.tablero[0,1] == 'o' and self.tablero[1,1] == 'o' and self.tablero[2,1] == 'o':
            self.intentos = 1
            print("GANASTE")
        elif self.tablero[0,2] == 'x' and self.tablero[1,2] == 'x' and self.tablero[2,2] == 'x' or self.tablero[0,2] == 'o' and self.tablero[1,2] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            print("GANASTE")

    def limpiar(self):
        self.tablero = np.array([['*',' *', '*'], ['*', '*', '*'], ['*', '*', '*']])
        self.intentos = 0
        self.position = list(set(['01', '02', '03', '11', '12', '13', '21', '22', '23']))