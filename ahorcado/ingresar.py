from random import shuffle
from prints.prints import Print
prints = Print()
class Ingresar:
    archivo_escrito = []
    def __init__(self, archivo_escrito):
        lista = [line.rstrip() for line in open(archivo_escrito)]
        self.archivo_escrito = lista

    def ingresarnombre(self, palabra):
        archivo = open("palabras.txt", "a")
        archivo.write("\n" + str(palabra))
        archivo.close()
        print(palabra)

    def ver_lista(self):
        return str(self.archivo_escrito)
