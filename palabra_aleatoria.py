from random import shuffle
from bd import *
db = conexion()
class palabra_aleatoria:
    import mysql.connector
    palabra = ""
    aleatorio = []
    lista1 = []
    archivo_escrito = []
    listaBD = []
    def __init__(self, archivo_escrito, archivo_juego, decision):
        self.lista1 = [line.rstrip() for line in open(archivo_escrito)]
        lista_juego = [line.rstrip() for line in open(archivo_juego)]
        self.archivo_escrito = list(set(self.lista1))
        self.archivo_juego = lista_juego
        print("CARGANDO DATOS DE LA LISTA... \n")

    def cargarDB(self):
        print("CARGANDO DATOS EN LA BASE DE DATOS... \n")
        for i in list(set(db.database(2))):
            self.listaBD.append(i[1])
            self.archivo_escrito.append(i[1])

    def seleccionarpalabra(self):
        if len(self.archivo_escrito) == 0:
            print("SE TERMINARON TODAS LAS PALABRAS")
            if db.database != "":
                self.archivo_escrito = list(set(self.listaBD))
            else:
                self.archivo_escrito = list(set(self.lista1))

        if len(self.archivo_escrito) > 0:
            shuffle(self.archivo_escrito)
            archivo = open("juego.txt", "w")
            self.palabra = self.archivo_escrito.pop()
            archivo.write(str(self.palabra))
            archivo.close()

        for i in self.palabra:
            self.aleatorio.append("|")