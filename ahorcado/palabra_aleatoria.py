from random import shuffle
from prints.prints import Print
prints = Print()
# from bd import *
# db = conexion()
class Palabra_Aleatoria:
    import mysql.connector
    palabra = ""
    aleatorio = []
    lista1 = []
    archivo_escrito = []
    listaBD = []
    def __init__(self, archivo_escrito, archivo_juego):
        self.lista1 = [line.rstrip() for line in open(archivo_escrito)]
        self.archivo_escrito = list(set(self.lista1))
        prints.cargando_datos_lista()

    def seleccionarpalabra(self):
        if len(self.archivo_escrito) == 0:
            self.archivo_escrito = list(set(self.lista1))

        if len(self.archivo_escrito) > 0:
            shuffle(self.archivo_escrito)
            archivo = open("juego.txt", "w")
            self.palabra = self.archivo_escrito.pop()
            # print(self.palabra)
            archivo.write(str(self.palabra))
            archivo.close()