import pygame
import math

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((1844, 1000))
pygame.display.set_caption("Cuadrícula Hexagonal Dinámica")
reloj = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)
AZUL = (50, 150, 255)
NEGRO = (0, 0, 0)

#Coordenadas
dpunto = 75
x0 = 1844 // 2
y0 = 1000 // 2
x = 0
y = 0

while True: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar el fondo de pantalla con blanco
    pantalla.fill(BLANCO)

    # Dibujar una línea (desde x=100, y=100 hasta x=700, y=500 con grosor de 5)
    pygame.draw.line(pantalla, NEGRO, (0, y0), (1844, y0), 2)
    pygame.draw.line(pantalla, NEGRO, (x0, 0), (x0, 1000), 2)
    
    for x in range(-500 // dpunto, 500 // dpunto):        
        pygame.draw.circle(pantalla, NEGRO, (x0 + x * dpunto, y0), 2)
    for y in range(-900 // dpunto, 900 // dpunto):        
        pygame.draw.circle(pantalla, NEGRO, (x0, y0 + y * dpunto), 2)

    for t in range(0, 50 * dpunto):
        x = t / dpunto
        try:
            #valor = math.sin(x)
            valor = math.log(x)
            if y0 - valor * dpunto < 1850 and y0 - valor * dpunto > 0:
                pygame.draw.circle(pantalla, AZUL, (x0 + x * dpunto, y0 - valor * dpunto), 2)
        except ValueError:
            pass
        
    for t in range(-40 * dpunto, 10 * dpunto):
        x = t / dpunto
        try:
            valor = math.exp(x)            
            if y0 - valor * dpunto < 1850 and y0 - valor * dpunto > 0:
                pygame.draw.circle(pantalla, GRIS, (x0 + x * dpunto, y0 - valor * dpunto), 2)
        except ValueError:
            pass
            

   # Actualizar la pantalla
    pygame.display.flip()


