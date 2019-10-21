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
        print(inicio)
    def error_uno(self, tipo_letra, vidas, letra_usada):
        error_uno = '''
        +---+
        |   |
        |   0
        |
        |
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        print(error_uno)
    def error_dos(self, tipo_letra, vidas, letra_usada):
        error_dos = '''
        +---+
        |   |
        |   O
        |   |
        |
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        print(error_dos)
    def error_tres(self, tipo_letra, vidas, letra_usada):
        error_tres = '''
        +---+
        |   |
        |   O
        |  /|\ 
        |
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        print(error_tres)
    def error_cuatro(self, tipo_letra, vidas, letra_usada):
        error_cuatro = '''
        +---+
        |   |
        |   O
        |  /|\ 
        |  / 
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        print(error_cuatro)
    def error_final(self, tipo_letra, vidas, letra_usada):
        error_final = '''
        +---+
        |   |
        |   O
        |  /|\ 
        |  / \ 
        |
        =========  LETRA ''' + tipo_letra + ''', TOTAL DE VIDAS:   '''+ vidas +'''    LETRA USADA:  '''+ letra_usada
        print(error_final)