# import numeric
import os
import numpy as np
class Juego:
    # juego = Juego()
    intentos = 0
    jugador = ""
    turno = 0
    tablero = np.array([['*',' *', '*'], ['*', '*', '*'], ['*', '*', '*']])
    position = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    def posiciones(self):
        while self.intentos <= 0:
            self.turnos()
            posicion = input("SELECCIONA UNA POSICIÓN\n" + str(self.position) + "\n")

            os.system('cls')

            # Cambiamos el simbolo '*' por el símbolo dependiendo el turno del jugador
            if self.jugador == "JUGADOR 1":
                #Verificamos si se quiere poner una ubicación correcta en el tablero
                if len(posicion) == 2:
                    posicion1 = int(posicion[0])
                    posicion2 = int(posicion[1])
                else:
                    while len(posicion) != 2:
                        os.system('cls')
                        print("INGRESE LOS CARACTERES CORRECTOS PORFAVOR")
                        posicion = input("SELECCIONA UNA POSICIÓN\n" + str(self.position) + "\n")
                if self.tablero[posicion1, posicion2] ==  "x" or self.tablero[posicion1, posicion2] ==  "o":
                    print("SE REPITE")
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
                        print("INGRESE LOS CARACTERES CORRECTOS PORFAVOR")
                        posicion = input("SELECCIONA UNA POSICIÓN\n" + str(self.position) + "\n")
                if self.tablero[posicion1, posicion2] ==  "x" or self.tablero[posicion1, posicion2] ==  "o":
                    print("SE INGRESÓ LA MISMA POSICIÓN, INGRESE UNA POSICIÓN DIFERENTE Y QUE SEA CORRECTA")
                else:
                    self.tablero[posicion1, posicion2] =  "o"
                    # Eliminamos el elemento ingresado del array position
                    self.position.remove(posicion)
                    self.turno += 1

            if len(self.position) == 0:
                print("JUEGO TERMINADO .... NADIE GANÓ !!!!")
                break

            print(self.tablero)
            self.ganar()
        self.limpiar()

    def turnos(self):
        if self.turno % 2:
            self.jugador = "JUGADOR 2"
            print(self.jugador)
        else:
            self.jugador = "JUGADOR 1"
            print(self.jugador)

    def ganar(self):
        if self.tablero[0,0] == 'x' and self.tablero[0,1] == 'x' and self.tablero[0,2] == 'x' or self.tablero[0,0] == 'o' and self.tablero[0,1] == 'o' and self.tablero[0,2] == 'o':
            self.intentos = 1
            print("GANASTE " + str(self.jugador))
        elif self.tablero[1,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[1,2] == 'x' or self.tablero[1,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[1,2] == 'o':
            self.intentos = 1
            print("GANASTE " + str(self.jugador))
        elif self.tablero[2,0] == 'x' and self.tablero[2,1] == 'x' and self.tablero[2,2] == 'x' or self.tablero[2,0] == 'o' and self.tablero[2,1] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            print("GANASTE " + str(self.jugador))
        elif self.tablero[0,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[2,2] == 'x' or self.tablero[0,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            print("GANASTE " + str(self.jugador))
        elif self.tablero[2,0] == 'x' and self.tablero[1,1] == 'x' and self.tablero[0,2] == 'x' or self.tablero[2,0] == 'o' and self.tablero[1,1] == 'o' and self.tablero[0,2] == 'o':
            self.intentos = 1
            print("GANASTE " + str(self.jugador))
        elif self.tablero[0,0] == 'x' and self.tablero[1,0] == 'x' and self.tablero[2,0] == 'x' or self.tablero[0,0] == 'o' and self.tablero[1,0] == 'o' and self.tablero[2,0] == 'o':
            self.intentos = 1
            print("GANASTE " + str(self.jugador))
        elif self.tablero[0,1] == 'x' and self.tablero[1,1] == 'x' and self.tablero[2,1] == 'x' or self.tablero[0,1] == 'o' and self.tablero[1,1] == 'o' and self.tablero[2,1] == 'o':
            self.intentos = 1
            print("GANASTE " + str(self.jugador))
        elif self.tablero[0,2] == 'x' and self.tablero[1,2] == 'x' and self.tablero[2,2] == 'x' or self.tablero[0,2] == 'o' and self.tablero[1,2] == 'o' and self.tablero[2,2] == 'o':
            self.intentos = 1
            print("GANASTE " + str(self.jugador))

    def limpiar(self):
        self.tablero = np.array([['*',' *', '*'], ['*', '*', '*'], ['*', '*', '*']])
        self.intentos = 0
        self.position = ['01', '02', '03', '11', '12', '13', '21', '22', '23']