import sys
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
         sys.stdout.write("\n --------------- !!!JUEGO DEL AHORCADO!!!  ------------------\n")
    def sin_conexion(self):
        sys.stdout.write("\nNO SE ENCUENTRÓ NINGUNA BASE DE DATOS\n")
    def empecemos(self):
        sys.stdout.write("-- !!EMPECEMOS!! --")
    #POSIBLE SOLUCION
    def debe_reiniciar(self, respuesta):
        respuesta = ""
        return respuesta
    def seleccione_opc_correcta(self):
        sys.stdout.write("INGRESE UNA OPCION DEL MENÚ CORRECTAMENTE")
    def palabra_a_adivinar(self, variable):
        sys.stdout.write("La palabra adivinar es: " + variable)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE INGRESAR
    def agregar_palabra(self):
        opc = input("¿Desea agregar una palabra? (s/n)\n")
        return opc
    def se_agrego_correctamente(self):
        sys.stdout.write("La palabra se agregó correctamente en el texto \n")
    def ingrese_una_palabra(self):
        palabra = str(input("Ingrese una palabra\n"))
        return palabra
    def ver_la_lista(self, variable):
        sys.stdout.write("lista" + variable)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE JUGAR
    def ingrese_letra(self):
        letra = (str(input("Ingrese una letra para adivinar la palabra\n")))
        return letra
    def solo_un_caracter(self):
        sys.stdout.write("INGRESE SOLO 1 CARACTER")
    def letras_correctas(self, ingresadas):
        sys.stdout.write("LETRAS INGRESADAS: " + ingresadas)
    def letra_ya_ingresada(self):
        sys.stdout.write("ESTA LETRA YA LA HABÍAS INGRESADO")
    def cadena(self, cadena):
        sys.stdout.write("CADENA: " + cadena)
    def juego_terminado(self):
        sys.stdout.write("JUEGO TERMINADO")
    def vidas_terminadas(self):
        sys.stdout.write("SE TE TERMINARON TODAS TUS VIDAS")
    def la_palabra_a_Adivinar_era(self,palabra):
        sys.stdout.write("La palabra adivinar era: " +palabra)
    def puntos_totales(self,puntos):
        sys.stdout.write("PUNTOS TOTALES: " + puntos)
    def completo_vidas(self):
        sys.stdout.write("COMPLETÓ TODAS LAS PALABRAS")
    def mostarar_letras_actuales(self, index, arreglo):
        sys.stdout.write(str(arreglo[0:index]))
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE PALABRA ALEATORIA
    def cargando_datos_lista(self):
        sys.stdout.write("CARGANDO DATOS DE LA LISTA... \n")
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>CLASE BD
    def palabra_usada(self, palabra):
        sys.stdout.write("PALABRA USADA: " + palabra)
    def palabras_ingresadas_a_bd(self):
       sys.stdout.write("\nPALABRAS INGRESADAS EN LA BASE DE DATOS:")
    def n(self):
        sys.stdout.write("\n")
    def i(self,i):
        sys.stdout.write(str(i))
    def no_hay_conexion_en_la_bd(self):
        sys.stdout.write("!!!NO HAY CONEXION A LA BASE DE DATOS!!!\n SE LIMITARÁN ALGUNAS FUNCIONES")
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
        sys.stdout.write("RANGO FUERA DEL INDICADO")
    def ingrese_caracteres_correctos(self):
        sys.stdout.write("INGRESE LOS CARACTERES CORRECTOS PORFAVOR")
    def se_repite(self):
        sys.stdout.write("SE REPITE")
    def misma_posicion(self):
        sys.stdout.write("SE INGRESÓ LA MISMA POSICIÓN, INGRESE UNA POSICIÓN DIFERENTE Y QUE SEA CORRECTA")
    def nadie_gano(self):
        sys.stdout.write("JUEGO TERMINADO .... NADIE GANÓ !!!!")
    def ganaste(self, jugador):
        sys.stdout.write("GANASTE " + jugador)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>LIMPIAR CONSOLA
    def limpiar_consola(self):
        import os
        os.system('cls')
    def jugador(self, jugador):
        sys.stdout.write(jugador)