from ahorcado.menu_ahorcado import Ahorcado_Menu
from gato.menu_gato import Gato_Menu

option = input("¿Seleccione el juego a jugar?\n"
               + "1. - Ahorcado\n"
               + "2. - Gato\n"
               + "3. - Salir\n")
while option != '3':
    if option == '1':
        menu_ahorcado = Ahorcado_Menu()
    elif option == '2':
        menu_gato = Gato_Menu()

    option = input("¿Seleccione el juego a jugar?\n"
               + "1. - Ahorcado\n"
               + "2. - Gato\n"
               + "3. - Salir\n")