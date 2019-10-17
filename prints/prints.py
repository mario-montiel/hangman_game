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