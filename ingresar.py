from random import shuffle
from bd import *
class ingresar:
    palabra = ""
    archivo_escrito = []
    def __init__(self, archivo_escrito):
        lista = [line.rstrip() for line in open(archivo_escrito)]
        self.archivo_escrito = lista
        print("lista" + str(self.archivo_escrito))

    def ingresarnombre(self):
        opc = input("¿Desea agregar una palabra? (s/n)\n")
        while opc.lower() != 'n':
            palabra = str(input("Ingrese una palabra\n"))
            db = conexion()
            db.database(palabra)
            self.palabra = palabra
            archivo = open("palabras.txt", "a")
            archivo.write("\n" + str(palabra))
            archivo.close()
            print("La palabra se agregó correctamente en el texto \n")
            opc = input("¿Desea agregar una palabra? (s/n)\n")