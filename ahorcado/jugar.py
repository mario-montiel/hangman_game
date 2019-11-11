import os
from dibujos.dibujos import Dibujos
from txt.txt import Texto
dibujos = Dibujos()
txt = Texto()
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
    a = ""
    correcta = []
    existe = False
    derrota_mortal = 0
    terminar = 0

    def encuentra(self, letra_ingresada_main):
            cadena = self.palabra
            carac = letra_ingresada_main.lower()
            
            indice = 0
            for i in self.palabra:
                self.pruebon.append("_")
                if cadena[indice] == carac.lower():
                    self.i.append(indice)
                    for q in self.correcta:
                        if q == carac:
                            self.existe = True
                    if self.existe == False:
                        self.correcta.append(carac)
                indice+=1
                self.indice = indice
            
            for i in self.i:
                if self.palabra[i] == carac.lower():
                    self.pruebon[i] = carac.lower()
                    self.comprobar = 1
                else:
                    self.comprobar = 0
            txt.guardar_letras_ingresadas_a("juego.txt", self.pruebon, indice)
            self.a = "".join(self.pruebon)
            self.arreglo()
            self.vidas()
            self.dibujar()
            self.derrota_final()
            
    def arreglo(self):
        return self.pruebon[0:self.indice]

    def vidas(self):
        if self.comprobar == 1:
            self.tipo_letra = "CORRECTA"
        else:
            self.vida = self.vida - 1
            self.tipo_letra = "INCORRECTA"
        if self.vida <= 0:
            self.terminar = 1
        elif self.verificar[0:self.indice] == self.palabra:
            self.terminar = 1

    def dibujar(self):
        error_uno = ""
        error_dos = ""
        error_tres = ""
        error_cuatro = ""
        error_final = ""
        inicio = ""

        if self.vida == 5:
            inicio = dibujos.inicio(self.tipo_letra, str(self.vida),self.letra )
        txt.guardar_dibujo_a("juego.txt", str(inicio))

        if self.vida == 4:
            error_uno = dibujos.error_uno(self.tipo_letra, str(self.vida),self.letra )
        txt.guardar_dibujo_a("juego.txt", str(error_uno))

        if self.vida == 3:
            error_dos = dibujos.error_dos(self.tipo_letra, str(self.vida),self.letra )
        txt.guardar_dibujo_a("juego.txt", str(error_dos))

        if self.vida == 2:
            error_tres = dibujos.error_tres(self.tipo_letra, str(self.vida),self.letra )
        txt.guardar_dibujo_a("juego.txt", str(error_tres))

        if self.vida == 1:
            error_cuatro = dibujos.error_cuatro(self.tipo_letra, str(self.vida),self.letra )
        txt.guardar_dibujo_a("juego.txt", str(error_cuatro))

        if self.vida == 0:
            error_final = dibujos.error_final(self.tipo_letra, str(self.vida),self.letra )
            self.pruebon = []
            self.derrota_mortal = 1
        txt.guardar_dibujo_a("juego.txt", str(error_final))

    def limpiar(self):
        self.cadena = []
        self.i = []
        self.pruebon = []
        self.comprobar = 0
        self.vida = 5
        self.verificar = []
        self.indice = 0
        
    def derrota_final(self):
            
        if self.derrota_mortal == 1:
            return 1
    
    def victoria_final(self):
        
        if self.a[0:self.indice] == self.palabra:
            return 1
        
        
        
        
        
        
        
        
        
        
        
        
#     import os
# from bd import *
# db = conexion()
# class jugar:
#     palabra = ""
#     letra = ''
#     cadena = []
#     i = []
#     pruebon = []
#     comprobar = 0
#     vida = 5
#     tipo_letra = ""
#     indice = 0
#     verificar = []
#     puntos = 0
#     a = ""
#     usuario = ""
#     correcta = []
#     existe = False

#     def encuentra(self):
#         while self.vida > 0 and self.a[0:self.indice] != self.palabra:
#             db.fin = 1
#             letra = (str(input("Ingrese una letra para adivinar la palabra\n")))
#             if len(letra) != 1:
#                 print("INGRESE SOLO 1 CARACTER")
#             self.letra = letra.lower()
#             cadena = self.palabra
#             carac = letra.lower()
#             indice = 0
#             os.system('cls')
#             for i in self.palabra:
#                 self.pruebon.append("|")
#                 if cadena[indice] == carac.lower():
#                     self.i.append(indice)
#                     for q in self.correcta:
#                         if q == carac:
#                             self.existe = True
#                     if self.existe == False:
#                         self.correcta.append(carac)
#                         print("LETRAS INGRESADAS: " + str(self.correcta))
#                     else:
#                         print("ESTA LETRA YA LA HABÍAS INGRESADO")
#                 indice+=1
#                 self.indice = indice
#             print("CADENA: " + cadena)
#             for i in self.i:
#                 if self.palabra[i] == carac.lower():
#                     self.pruebon[i] = carac.lower()
#                     self.comprobar = 1
#                     self.puntos += 10
#                 else:
#                     self.comprobar = 0
#             archivo = open("juego.txt", "a")
#             archivo.write("\n" + str(self.pruebon[0:indice]) + "\n")
#             archivo.close()
#             self.a = "".join(self.pruebon)
#             self.vidas()
#             self.dibujar()
#         # print("PUNTOS: " + str(self.puntos))
#         db.usuario = self.usuario
#         db.puntos = self.puntos
#         db.database(4)

#     def vidas(self):
#         if self.comprobar == 1:
#             self.tipo_letra = "CORRECTA"
#         else:
#             self.vida = self.vida - 1
#             self.tipo_letra = "INCORRECTA"
#         if self.vida <= 0:
#             print("JUEGO TERMINADO")
#             print("SE TE TERMINARON TODAS TUS VIDAS")
#             print("La palabra adivinar era: " + str(self.palabra))
#             print("PUNTOS TOTALES: " + str(self.puntos))
#         elif self.verificar[0:self.indice] == self.palabra:
#             print("JUEGO TERMINADO")
#             print("COMPLETÓ TODAS LAS PALABRAS")
#             print("La palabra adivinar era: " + str(self.palabra))
#             print("PUNTOS TOTALES: " + str(self.puntos))

#     def dibujar(self):
#         error_uno = ""
#         error_dos = ""
#         error_tres = ""
#         error_cuatro = ""
#         error_final = ""
#         inicio = ""

#         if self.vida == 5:
#             inicio = '''
#    +---+
#    |   |
#    |
#    |
#    |
#    |
# =========  PALABRA ''' + self.tipo_letra + ''', TOTAL DE VIDAS:   '''+str(self.vida) +'''    LETRA USADA:  '''+self.letra
#             print(self.pruebon[0:self.indice])
#             print(inicio)
#         archivo = open("juego.txt", "a")
#         archivo.write("\n" + str(inicio) + "\n")
#         archivo.close()

#         if self.vida == 4:
#             error_uno = '''
#    +---+
#    |   |
#    |   O
#    |
#    |
#    |
# =========  PALABRA ''' + self.tipo_letra + ''', TOTAL DE VIDAS:   '''+str(self.vida) +'''    LETRA USADA:  '''+self.letra
#             print(self.pruebon[0:self.indice])
#             print(error_uno)
#         archivo = open("juego.txt", "a")
#         archivo.write("\n" + str(error_uno) + "\n")
#         archivo.close()

#         if self.vida == 3:
#             error_dos = '''
#    +---+
#    |   |
#    |   O
#    |   |
#    |
#    |
# =========  PALABRA ''' + self.tipo_letra + ''', TOTAL DE VIDAS:   '''+str(self.vida) +'''    LETRA USADA:  '''+self.letra
#             print(self.pruebon[0:self.indice])
#             print(error_dos)
#         archivo = open("juego.txt", "a")
#         archivo.write("\n" + str(error_dos) + "\n")
#         archivo.close()

#         if self.vida == 2:
#             error_tres = '''
#    +---+
#    |   |
#    |   O
#    |  /|\
#    |
#    |
# =========  PALABRA ''' + self.tipo_letra + ''', TOTAL DE VIDAS:   '''+str(self.vida) +'''    LETRA USADA:  '''+self.letra
#             print(self.pruebon[0:self.indice])
#             print(error_tres)
#         archivo = open("juego.txt", "a")
#         archivo.write("\n" + str(error_tres) + "\n")
#         archivo.close()

#         if self.vida == 1:
#             error_cuatro = '''
#    +---+
#    |   |
#    |   O
#    |  /|\
#    |  /
#    |
# =========  PALABRA ''' + self.tipo_letra + ''', TOTAL DE VIDAS:   '''+str(self.vida) +'''    LETRA USADA:  '''+self.letra
#             print(self.pruebon[0:self.indice])
#             print(error_cuatro)
#         archivo = open("juego.txt", "a")
#         archivo.write("\n" + str(error_cuatro) + "\n")
#         archivo.close()

#         if self.vida == 0:
#             error_final = '''
#    +---+
#    |   |
#    |   O
#    |  /|\
#    |  / \
#    |
# =========  PALABRA ''' + self.tipo_letra + ''', TOTAL DE VIDAS:   '''+str(self.vida) +'''    LETRA USADA:  '''+self.letra
#             print(self.pruebon[0:self.indice])
#             print(error_final)
#             print("LA PALABRA ADIVINAR ERA: " + str(self.palabra))
#             self.pruebon = []
#         archivo = open("juego.txt", "a")
#         archivo.write("\n" + str(error_final) + "\n")
#         archivo.close()

#     def limpiar(self):
#         self.cadena = []
#         self.i = []
#         self.pruebon = []
#         self.comprobar = 0
#         self.vida = 5
#         self.verificar = []
#         self.indice = 0
        

