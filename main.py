from ingresar import *
from jugar import *
from palabra_aleatoria import *
from usuario import *
from bd import *

print(" --------------- !!!JUEGO DEL AHORCADO!!!  ------------------\n")
decision = input("¿DESEA JUGAR CON PALABRAS DE LA BASE DE DATOS? (s/n)")
aleatorio = palabra_aleatoria("palabras.txt", "juego.txt", decision)
u = input("Ingrese el nombre de un Usuario\n")
usu = usuario(u)
if decision.lower() == 's':
    aleatorio.cargarDB()
    db = conexion()
    db.usuario = u
    db.database(3)
else:
    aleatorio.seleccionarpalabra()

opcion = input("---- MENU ----\n"
+ "1. - Ingresar Palabra\n"
+ "2. - Jugar\n"
+ "4. - Puntuación\n"
+ "5. - Salir\n")

jugar = jugar()
p_verificar = jugar.verificar
ingresar = ingresar("palabras.txt")

while opcion != '5':
    if opcion == '0':
        db.database(1)
    if opcion == '1':
        ingresar.ingresarnombre()
    elif opcion == '2':
        aleatorio.palabra = ""
        aleatorio.aleatorio = []
        aleatorio.seleccionarpalabra()
        os.system('cls')
        print("La palabra adivinar es: " + str(aleatorio.aleatorio))
        print("-- !!EMPECEMOS!! --")
        jugar.palabra = aleatorio.palabra
        jugar.limpiar()
        jugar.usuario = usu.usuario
        jugar.encuentra()
        jugar.vidas()
        print("USUARIO: " + str(usu.usuario))
        jugar.dibujar()
        print("Debe reiniciar el juego para poder seguir jugando\n")
    elif opcion == '3':
        os.system('cls')
        u = input("Ingrese el nombre de un Usuario\n")
        db.usuario = u
        db.database(3)
        usu = usuario(u)
        jugar.puntos = 0
        db.database(4)
    elif opcion == '4':
        db.database(5)
    opcion = input("---- MENU ----\n"
    + "0. - Ver Palabras\n"
    + "1. - Ingresar Palabra\n"
    + "2. - Jugar\n"
    + "3. - Jugador Nuevo\n"
    + "4. - Puntuación\n"
    + "5. - Salir\n")
