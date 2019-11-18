import sys
import numpy as np
class Dibujos:
    def inicio(self, tipo_letra, vidas, letra_usada):
        inicio = '''
        +---+
        |   |
        |
        |
        |
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        sys.stdout.write(inicio)
        return inicio
    def error_uno(self, tipo_letra, vidas, letra_usada):
        error_uno = '''
        +---+
        |   |
        |   0
        |
        |
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        sys.stdout.write(error_uno)
        return error_uno
    def error_dos(self, tipo_letra, vidas, letra_usada):
        error_dos = '''
        +---+
        |   |
        |   O
        |   |
        |
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        sys.stdout.write(error_dos)
        return error_dos
    def error_tres(self, tipo_letra, vidas, letra_usada):
        error_tres = '''
        +---+
        |   |
        |   O
        |  /|\ 
        |
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        sys.stdout.write(error_tres)
        return error_tres
    def error_cuatro(self, tipo_letra, vidas, letra_usada):
        error_cuatro = '''
        +---+
        |   |
        |   O
        |  /|\ 
        |  / 
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        sys.stdout.write(error_cuatro)
        return error_cuatro
    def error_final(self, tipo_letra, vidas, letra_usada):
        error_final = '''
        +---+
        |   |
        |   O
        |  /|\ 
        |  / \ 
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        sys.stdout.write(error_final)
        return error_final
    