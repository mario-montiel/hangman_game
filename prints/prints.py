class Print:

    def db_notfound(self):
        print("NO SE ENCONTRÓ NINGUNA BASE DE DATOS")

    def ahorcado_seleccion_db(self):
        seleccion = input("¿Desea usar conexión a la base de datos? (s/n)")
        return seleccion

    def ahorcado_menu(self):
        opcion = input("---- MENU ----\n"
        + "0. - Ver las palabras ingresadas \n"
        + "1. - Ingresar Palabra\n"
        + "2. - Jugar\n"
        + "3. - Salir\n")
        return opcion
    def juego_ahorcado(self):
         print(" --------------- !!!JUEGO DEL AHORCADO!!!  ------------------\n")
    def sin_conexion(self):
        print("\nNO SE ENCUENTRÓ NINGUNA BASE DE DATOS\n")
    def empecemos(self):
        print("-- !!EMPECEMOS!! --")
    def debe_reiniciar(self):
        print("Debe reiniciar el juego para poder seguir jugando\n")
    def seleccione_opc_correcta(self):
        print("INGRESE UNA OPCION DEL MENÚ CORRECTAMENTE")
    def palabra_a_adivinar(self):
        print("La palabra adivinar es: ")
    #CLASE INGRESAR
    def agregar_palabra(self):
        opc = input("¿Desea agregar una palabra? (s/n)\n")
        return opc
    def se_agrego_correctamente(self):
        print("La palabra se agregó correctamente en el texto \n")
    def ingrese_una_palabra(self):
        palabra = str(input("Ingrese una palabra\n"))
        return palabra
    
