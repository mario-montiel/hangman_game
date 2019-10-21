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
    def palabra_a_adivinar(self, variable):
        print("La palabra adivinar es: " + variable)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE INGRESAR
    def agregar_palabra(self):
        opc = input("¿Desea agregar una palabra? (s/n)\n")
        return opc
    def se_agrego_correctamente(self):
        print("La palabra se agregó correctamente en el texto \n")
    def ingrese_una_palabra(self):
        palabra = str(input("Ingrese una palabra\n"))
        return palabra
    def ver_la_lista(self, variable):
        print("lista" + variable)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE JUGAR
    def ingrese_letra(self):
        letra = (str(input("Ingrese una letra para adivinar la palabra\n")))
        return letra
    def solo_un_caracter(self):
        print("INGRESE SOLO 1 CARACTER")
    def letras_correctas(self, ingresadas):
        print("LETRAS INGRESADAS: " + ingresadas)
    def letra_ya_ingresada(self):
        print("ESTA LETRA YA LA HABÍAS INGRESADO")
    def cadena(self, cadena):
        print("CADENA: " + cadena)
    def juego_terminado(self):
        print("JUEGO TERMINADO")
    def vidas_terminadas(self):
        print("SE TE TERMINARON TODAS TUS VIDAS")
    def la_palabra_a_Adivinar_era(self,palabra):
        print("La palabra adivinar era: " +palabra)
    def puntos_totales(self,puntos):
         print("PUNTOS TOTALES: " + puntos)
    def completo_vidas(self):
        print("COMPLETÓ TODAS LAS PALABRAS")
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE PALABRA ALEATORIA
    def cargando_datos_lista(self):
         print("CARGANDO DATOS DE LA LISTA... \n")
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE BD
    def palabra_usada(self, palabra):
        print("PALABRA USADA: " + palabra)
    def palabras_ingresadas_a_bd(self):
        print("\nPALABRAS INGRESADAS EN LA BASE DE DATOS:")
    def n(self):
        print("\n")
    def i(self,i):
        print(i)
    def no_hay_conexion_en_la_bd(self):
        print("!!!NO HAY CONEXION A LA BASE DE DATOS!!!\n"
            + "SE LIMITARÁN ALGUNAS FUNCIONES")
        return ""
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE MENU GATO
    def menu_gato(self):
        opcion = input("---- MENU ----\n"
                    + "1. - Jugar\n"
                    + "2. - Salir\n")
        return opcion
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE MAIN MENU
    def menu_main(self):
        option = input("¿Seleccione el juego a jugar?\n"
               + "1. - Ahorcado\n"
               + "2. - Gato\n"
               + "3. - Salir\n")
        return option
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE JUEGO
    def posicion(self, posicion):
        posicion = input("SELECCIONA UNA POSICIÓN\n" + posicion + "\n")
        return posicion
    def rango_fuera_del_indicado(self):
        print("RANGO FUERA DEL INDICADO")
    def ingrese_caracteres_correctos(self):
        print("INGRESE LOS CARACTERES CORRECTOS PORFAVOR")
    def se_repite(self):
         print("SE REPITE")
    def misma_posicion(self):
        print("SE INGRESÓ LA MISMA POSICIÓN, INGRESE UNA POSICIÓN DIFERENTE Y QUE SEA CORRECTA")
    def nadie_gano(self):
        print("JUEGO TERMINADO .... NADIE GANÓ !!!!")
    def ganaste(self, jugador):
        print("GANASTE " + jugador)