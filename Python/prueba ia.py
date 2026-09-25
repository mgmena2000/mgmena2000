import pygame
import sys

# 1. Inicializar Pygame y crear la ventana principal
pygame.init()
pantalla_principal = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Superficie dentro de otra")

# 2. Crear la superficie interna (lienzo secundario)
# Definimos un tamaño de 400x300 píxeles
superficie_interna = pygame.Surface((400, 300))

# Definimos los colores que usaremos
BLANCO = (255, 255, 255)
AZUL = (50, 100, 255)
ROJO = (255, 50, 50)

# Bucle principal del juego
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- RENDERIZADO ---

    # Limpiar la pantalla principal (Fondo blanco)
    pantalla_principal.fill(BLANCO)

    # Rellenar la superficie interna (Fondo azul)
    superficie_interna.fill(AZUL)

    # Dibujar ALGO DENTRO de la superficie interna
    # Nota que las coordenadas (180, 130) son RELATIVAS a la superficie interna
    pygame.draw.rect(superficie_interna, ROJO, (180, 130, 40, 40))

    # 3. Dibujar la superficie interna sobre la pantalla principal
    # La colocamos en las coordenadas (200, 150) de la pantalla principal
    pantalla_principal.blit(superficie_interna, (400, 150))

    # Actualizar la pantalla
    pygame.display.flip()
    reloj.tick(60)
