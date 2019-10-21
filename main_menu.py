from ahorcado.menu_ahorcado import Ahorcado_Menu
from gato.menu_gato import Gato_Menu
from prints.prints import Print
prints = Print()
option = prints.menu_main()
while option != '3':
    if option == '1':
        menu_ahorcado = Ahorcado_Menu()
    elif option == '2':
        menu_gato = Gato_Menu()

    option = prints.menu_main()