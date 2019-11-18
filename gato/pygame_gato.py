import pygame
from juego import Juego
from pygame.locals import *
import sys

jugar = Juego()

# ventana = pygame.display.set_mode((800,600))

# game_over = False

# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     pygame.draw.get(ventana, (255, 0, 0), jugar.dibujo())
            





# ///////////////////////
# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
NEGRO = (0, 0, 0)  # Color del fondo de la ventana (RGB)

tablero = str(jugar.dibujo())
def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("GATO_GAME")
    
    white = (255, 255, 255)

    # Bucle principal
    jugando = True
    while jugando:
        ventana.fill(NEGRO)
        
        
        
        font = pygame.font.Font(None, 30)
        #tablero
        # pygame.image.load(jugar.dibujo()).convert_alpha()
        tablero_surface = font.render(u''+ jugar.dibujo()+'', True, white)
        
        ventana.blit(tablero_surface, (200,200))
        # ventana.blit(tablero, (600,400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
                
        pygame.display.update()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
