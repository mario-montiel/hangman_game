import os
from ahorcado.ingresar import Ingresar
from ahorcado.jugar import Jugar
from ahorcado.palabra_aleatoria import Palabra_Aleatoria
from prints.prints import Print

jugar = Jugar()
ingresar = Ingresar("palabras.txt")
prints = Print()

class Ahorcado_Menu:
    def __init__(self):
        #Print de "EMPECEMOS"
        prints.juego_ahorcado()
        #PRINT DE CONEXION A BD
        x = prints.ahorcado_seleccion_db()
        #PRINT DE MENU
        menu = prints.ahorcado_menu()
        while menu != '3':
            if menu == '0':
                if x != 'n':
                    try:
                        from database.bd import Conexion
                        db = Conexion()
                        db.database(1)
                    except:
                        #PRINT SIN CONEXION
                        prints.sin_conexion()
                    menu = prints.ahorcado_menu()
                else:
                    ingresar.ver_lista()
                    menu = prints.ahorcado_menu()
            elif menu == '1':
                ingresar.ingresarnombre()
                menu = prints.ahorcado_menu()
            elif menu == '2':
                aleatorio = Palabra_Aleatoria("palabras.txt", "juego.txt")
                aleatorio.palabra = ""
                aleatorio.aleatorio = []
                aleatorio.seleccionarpalabra()
                os.system('cls')
                print("La palabra adivinar es: " + str(aleatorio.aleatorio))
                #prints.palabra_a_adivinar(str(aleatorio.aleatorio))
                prints.empecemos()
                jugar.palabra = aleatorio.palabra
                jugar.limpiar()
                jugar.encuentra()
                jugar.vidas()
                jugar.dibujar()
                prints.debe_reiniciar()
                menu = prints.ahorcado_menu()
            else:
                prints.seleccione_opc_correcta()
                menu = prints.ahorcado_menu()
            