from random import shuffle
from prints.prints import Print
prints = Print()
class Ingresar:
    palabra = ""
    archivo_escrito = []
    def __init__(self, archivo_escrito):
        lista = [line.rstrip() for line in open(archivo_escrito)]
        self.archivo_escrito = lista

    def ingresarnombre(self):
        opc = prints.agregar_palabra()
        while opc.lower() != 'n':
            palabra = prints.ingrese_una_palabra()
            try:
                from database.bd import Conexion
                db = Conexion()
                db.database(palabra)
            except:
                prints.db_notfound()
            self.palabra = palabra
            archivo = open("palabras.txt", "a")
            archivo.write("\n" + str(palabra))
            archivo.close()
            prints.se_agrego_correctamente()
            opc = prints.agregar_palabra()

    def ver_lista(self):
        prints.ver_la_lista(str(self.archivo_escrito))
