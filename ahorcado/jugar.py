import os
from prints.prints import Print
from dibujos.dibujos import Dibujos
dibujos = Dibujos()
prints = Print()
class Jugar:
    palabra = ""
    letra = ''
    cadena = []
    i = []
    pruebon = []
    comprobar = 0
    vida = 5
    tipo_letra = ""
    indice = 0
    verificar = []
    puntos = 0
    a = ""
    # usuario = ""
    correcta = []
    existe = False

    def encuentra(self):
        while self.vida > 0 and self.a[0:self.indice] != self.palabra:
            # db.fin = 1
            letra = prints.ingrese_letra()
            if len(letra) != 1:
                prints.solo_un_caracter()
            self.letra = letra.lower()
            cadena = self.palabra
            carac = letra.lower()
            indice = 0
            os.system('cls')
            for i in self.palabra:
                self.pruebon.append("|")
                if cadena[indice] == carac.lower():
                    self.i.append(indice)
                    for q in self.correcta:
                        if q == carac:
                            self.existe = True
                    if self.existe == False:
                        self.correcta.append(carac)
                        prints.letras_correctas(str(self.correcta))
                    else:
                        prints.letra_ya_ingresada()
                indice+=1
                self.indice = indice
            prints.cadena(cadena)
            for i in self.i:
                if self.palabra[i] == carac.lower():
                    self.pruebon[i] = carac.lower()
                    self.comprobar = 1
                    self.puntos += 10
                else:
                    self.comprobar = 0
            archivo = open("juego.txt", "a")
            archivo.write("\n" + str(self.pruebon[0:indice]) + "\n")
            archivo.close()
            self.a = "".join(self.pruebon)
            self.vidas()
            self.dibujar()
        # print("PUNTOS: " + str(self.puntos))
        # db.usuario = self.usuario
        # db.puntos = self.puntos
        # db.database(4)

    def vidas(self):
        if self.comprobar == 1:
            self.tipo_letra = "CORRECTA"
        else:
            self.vida = self.vida - 1
            self.tipo_letra = "INCORRECTA"
        if self.vida <= 0:
            prints.juego_terminado()
            prints.vidas_terminadas()
            prints.la_palabra_a_Adivinar_era(str(self.palabra))
            prints.puntos_totales(str(self.puntos))
        elif self.verificar[0:self.indice] == self.palabra:
            prints.juego_terminado()
            prints.completo_vidas()
            prints.la_palabra_a_Adivinar_era(str(self.palabra))
            prints.puntos_totales(str(self.puntos))

    def dibujar(self):
        error_uno = ""
        error_dos = ""
        error_tres = ""
        error_cuatro = ""
        error_final = ""
        inicio = ""

        if self.vida == 5:
            inicio = dibujos.inicio(self.tipo_letra, str(self.vida),self.letra )
            print(self.pruebon[0:self.indice])
        archivo = open("juego.txt", "a")
        archivo.write("\n" + str(inicio) + "\n")
        archivo.close()

        if self.vida == 4:
            error_uno = dibujos.error_uno(self.tipo_letra, str(self.vida),self.letra )
            print(self.pruebon[0:self.indice])
        archivo = open("juego.txt", "a")
        archivo.write("\n" + str(error_uno) + "\n")
        archivo.close()

        if self.vida == 3:
            error_dos = dibujos.error_dos(self.tipo_letra, str(self.vida),self.letra )
            print(self.pruebon[0:self.indice])
        archivo = open("juego.txt", "a")
        archivo.write("\n" + str(error_dos) + "\n")
        archivo.close()

        if self.vida == 2:
            error_tres = dibujos.error_tres(self.tipo_letra, str(self.vida),self.letra )
            print(self.pruebon[0:self.indice])
        archivo = open("juego.txt", "a")
        archivo.write("\n" + str(error_tres) + "\n")
        archivo.close()

        if self.vida == 1:
            error_cuatro = dibujos.error_cuatro(self.tipo_letra, str(self.vida),self.letra )
            print(self.pruebon[0:self.indice])
        archivo = open("juego.txt", "a")
        archivo.write("\n" + str(error_cuatro) + "\n")
        archivo.close()

        if self.vida == 0:
            error_final = dibujos.error_final(self.tipo_letra, str(self.vida),self.letra )
            print(self.pruebon[0:self.indice])
            prints.la_palabra_a_Adivinar_era(str(self.palabra))
            self.pruebon = []
        archivo = open("juego.txt", "a")
        archivo.write("\n" + str(error_final) + "\n")
        archivo.close()

    def limpiar(self):
        self.cadena = []
        self.i = []
        self.pruebon = []
        self.comprobar = 0
        self.vida = 5
        self.verificar = []
        self.indice = 0

