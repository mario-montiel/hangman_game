class Texto:
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>> AHORCADO CLASE JUGAR
    def guardar_letras_ingresadas_a(self, txt_destino, arreglo, index):
        archivo = open(txt_destino, "a")
        archivo.write("\n" + str(arreglo[0:index]) + "\n")
        archivo.close()
        
    def guardar_dibujo_a(self, txt_destino, dibujo):
        archivo = open(txt_destino, "a")
        archivo.write("\n" + str(dibujo) + "\n")
        archivo.close()