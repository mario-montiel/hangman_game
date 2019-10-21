from random import shuffle
class Ingresar:
    palabra = ""
    archivo_escrito = []
    def __init__(self, archivo_escrito):
        lista = [line.rstrip() for line in open(archivo_escrito)]
        self.archivo_escrito = lista

    def ingresarnombre(self):
        opc = input("¿Desea agregar una palabra? (s/n)\n")
        while opc.lower() != 'n':
            palabra = str(input("Ingrese una palabra\n"))
            try:
                from database.bd import Conexion
                db = Conexion()
                db.database(palabra)
            except:
                print("NO SE ENCONTRÓ NINGUNA BASE DE DATOS")
            self.palabra = palabra
            archivo = open("palabras.txt", "a")
            archivo.write("\n" + str(palabra))
            archivo.close()
            print("La palabra se agregó correctamente en el texto \n")
            opc = input("¿Desea agregar una palabra? (s/n)\n")

    def ver_lista(self):
        print("LISTA: ")
        for i in self.archivo_escrito:
            print(i)