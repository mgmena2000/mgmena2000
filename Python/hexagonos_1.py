import pygame
import math

# Inicializar Pygame
pygame.init()
ANCHO_GLOBAL = 1900
ALTO_GLOBAL = 1000
ANCHO_HEXAGONOS = 1800
ALTO_HEXAGONOS = 900
POSX_HEXAGONOS = 90
POSY_HEXAGONOS = 40
TOTAL_COLORES = 9

pantalla = pygame.display.set_mode((ANCHO_GLOBAL, ALTO_GLOBAL))
pantalla_hexagonos = pygame.Surface((ANCHO_HEXAGONOS, ALTO_HEXAGONOS))
pygame.display.set_caption("Cuadrícula Hexagonal Dinámica")
reloj = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)
AZUL = (50, 150, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0) 
CIAN = (0, 255, 255) 
MAGENTA = (255, 0, 255) 
TEAL = (0, 128, 128) 
MORADO = (128, 0, 128)
TODOSLOSCOLORES = [BLANCO, GRIS, AZUL, NEGRO, AMARILLO, CIAN, MAGENTA, TEAL, MORADO]
colorPinchado = BLANCO

class ColoresHexagono:
    def __init__(self, color, color_borde):
        self.color = color
        self.color_borde = color_borde

    def dameColor():
        return self.color

    def dameColorBorde():
        return self.color_borde

    def ponColor(color):
        self.color = color

    def ponColorborde(color):
        self.color_borde = color
    

class Hexagono:
    def __init__(self, x, y, radio, fila, columna, color, color_borde):
        self.x = x
        self.y = y        
        self.radio = radio
        self.fila = fila
        self.columna = columna
        self.color = color
        self.color_borde = color_borde
        self.borde = 2
        self.id_adyacentes = []

    def calcular_vertices(self):
        puntos = []
        for i in range(6):
            angulo = math.radians(60 * i + 30)
            px = self.x + self.radio * math.cos(angulo)
            py = self.y + self.radio * math.sin(angulo)
            puntos.append((px, py))
        return puntos

    def dibujar(self, superficie):
        if self.x > -RADIO_HEX and self.x < ANCHO_HEXAGONOS and self.y > -RADIO_HEX and self.y < ALTO_HEXAGONOS:
            vertices = self.calcular_vertices()
            pygame.draw.polygon(superficie, self.color, vertices)
            pygame.draw.polygon(superficie, self.color_borde, vertices, self.borde)

    def contiene_punto(self, pos_mouse):
        mx, my = pos_mouse
        mx = mx - POSX_HEXAGONOS
        my = my - POSY_HEXAGONOS
        distancia = math.sqrt((mx - self.x) ** 2 + (my - self.y) ** 2)
        return distancia <= self.radio * 0.866
    
class Colores:
    def __init__(self, x, y, ancho, largo, color):
        self.x = x
        self.y = y        
        self.ancho = ancho
        self.color = color
        self.color_borde = GRIS
        self.borde = 1
        
    def dibujar(self, superficie):        
        pygame.draw.polygon(superficie, self.color, ((self.x, self.y), (self.x + self.ancho, self.y), (self.x + self.ancho, self.y + self.ancho), (self.x, self.y + self.ancho)))
        #print(f" {self.x} {self.y} {self.color}")
        pygame.draw.polygon(superficie, self.color_borde, ((self.x, self.y), (self.x + self.ancho, self.y), (self.x + self.ancho, self.y + self.ancho), (self.x, self.y + self.ancho)), 1)

    def contiene_punto(self, pos_mouse):
        mx, my = pos_mouse        
        return self.x <= mx and self.x + self.ancho >= mx and self.y <= my and self.y + self.ancho >= my        

def pintarHexagonos(X, Y, ANCHO, ALTO, annadircolores):    
    hexagonos.clear()
    #X = ANCHO / 2
    #Y = ANCHO / 2
    total = 0
    for f in range(FILAS):
        COLUMNAS_NUEVO = COLUMNAS + 1 if f % 2 == 0 else COLUMNAS
        for c in range(COLUMNAS_NUEVO):
            # Desplazar las filas impares horizontalmente el ancho de un hexágono
            desplazamiento_x = (ANCHO / 2) if (f % 2 == 1) else 0
            
            
            # Calcular posición exacta del centro
            centro_x = X + c * ANCHO  + desplazamiento_x
            centro_y = Y + f * ALTO 
            
            # Guardar el hexágono con sus coordenadas de matriz (fila, columna)            
            if annadircolores == True:
                hexagonos.append(Hexagono(centro_x, centro_y, RADIO_HEX, fila=f, columna=c, color=colorPinchado, color_borde=GRIS))
                ColoresHexagonos.append(ColoresHexagono(colorPinchado, GRIS))                
            else:                
                hexagonos.append(Hexagono(centro_x, centro_y, RADIO_HEX, fila=f, columna=c, color=ColoresHexagonos[total].color, color_borde=ColoresHexagonos[total].color_borde))

            total = total + 1

def pintarBotonesColores(X, Y, ANCHO):    
    BotonesColores.clear()
    total = 0
    for f in range(TOTAL_COLORES):
        x0 = X + total % 2 * ANCHO
        y0 = Y + total // 2 * ANCHO
        elcolor = TODOSLOSCOLORES[total]
        BotonesColores.append(Colores(x0, y0, ANCHO, ANCHO, color=elcolor))
        total = total + 1
        
    
def pintarInfo(fila, columna):
        pygame.draw.rect(pantalla, BLANCO, [50, 950, 1500, 950])        
        pygame.draw.polygon(pantalla, AZUL, ((44, 945), (44, 990), (1720, 990), (1720, 945)), 5)
        fuente = pygame.font.SysFont("arial", 32)
        texto_superficie = fuente.render(f"Clic detectado en -> Fila: {fila}, Columna: {columna}", True, NEGRO)
        pantalla.blit(texto_superficie, (50, 950))
    
# --- GENERACIÓN DINÁMICA DE LA CUADRÍCULA ---
hexagonos = []
ColoresHexagonos = []
BotonesColores = []
RADIO_HEX = 40
FILAS = 1000 // RADIO_HEX
COLUMNAS = 1840 // math.trunc(math.sqrt(2.5) * RADIO_HEX * 2)
FILAS = 100
COLUMNAS= 200

# Margen inicial para que no se pegue a las esquinas de la pantalla
MARGEN_X = RADIO_HEX - 1000
MARGEN_Y = RADIO_HEX - 1000

# Cálculos de separación matemática
ANCHO_HEX = math.sqrt(3) * RADIO_HEX  # Separación horizontal aproximada (1.732 * radio)
ALTO_HEX = RADIO_HEX * 1.5            # Separación vertical

pintarHexagonos(MARGEN_X, MARGEN_Y, ANCHO_HEX, ALTO_HEX, True)
pintarBotonesColores(10, 10, 32)

pantalla.fill(BLANCO)
pantalla_hexagonos.fill(BLANCO)
#Dibujamos el tablero de los hexagonos
#pygame.draw.polygon(pantalla, AZUL, ((POSX_HEXAGONOS, 15), (ANCHO_HEXAGONOS + POSX_HEXAGONOS, 15), (ANCHO_HEXAGONOS + POSX_HEXAGONOS, ALTO_HEXAGONOS + POSY_HEXAGONOS), (POSX_HEXAGONOS, ALTO_HEXAGONOS + POSY_HEXAGONOS)), 5)


# Bucle principal
ejecutando = True
pulsado = False
moviendo = False
infof = 0
infoc = 0
x_pulsado = MARGEN_X
y_pulsado = MARGEN_Y
idHexagono = -1
idHexagonoPrevio = -1
idColor = -1
actualizar = True

#print(f"COLUMNAS: {COLUMNAS}")
while ejecutando:
    #pantalla.fill(BLANCO)
    pintar_info = False;
    for evento in pygame.event.get():
        pintar_info = False;
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                pulsado = False;
                if not moviendo:
                    pos_clic = pygame.mouse.get_pos()
                    seleccionados = 0                    
                    total = -1
                    idHexagonoPrevio = idHexagono
                    for hexag in hexagonos:
                        total = total + 1
                        if hexag.contiene_punto(pos_clic):
                            #print(f"Clic detectado en -> Fila: {hexag.fila}, Columna: {hexag.columna}")
                            pintar_info = True;
                            infof, infoc = hexag.fila, hexag.columna                            
                            idHexagono = total                            
                            #hexag.color = BLANCO if hexag.color == colorPinchado else colorPinchado #En el caso que queramos pintar de BLANCO el hexagono que ya no está seleccionado
                            hexag.color = colorPinchado
                            ColoresHexagonos[idHexagono].color = hexag.color
                            hexag.color_borde = GRIS if hexag.color_borde == NEGRO else NEGRO
                            #print(f"ID: {idHexagono}")
                            hexag.id_adyacentes.clear()
                            if hexag.columna > 1:
                                hexag.id_adyacentes.append(hexag.fila * COLUMNAS + ((hexag.fila - 1) // 2) + hexag.columna) #Izquierda
                            if hexag.columna < COLUMNAS:
                                hexag.id_adyacentes.append(hexag.fila * COLUMNAS + ((hexag.fila - 1) // 2) + hexag.columna + 2) #Derecha
                            if hexag.columna < COLUMNAS:
                                if hexag.fila < FILAS:    
                                    hexag.id_adyacentes.append((hexag.fila + 2 - 1) * COLUMNAS + ((hexag.fila + 2) // 2) + hexag.columna + ((hexag.fila + 2) % 2)) #Abajo Derecha
                            if hexag.columna > 0 or hexag.fila % 2 == 1:
                                if hexag.fila < FILAS:
                                    hexag.id_adyacentes.append((hexag.fila + 2 - 1) * COLUMNAS + ((hexag.fila + 2) // 2) + hexag.columna - 1 + ((hexag.fila + 2) % 2)) #Abajo Izquierda
                            if hexag.fila > 0:
                                if hexag.columna < COLUMNAS:
                                    hexag.id_adyacentes.append((hexag.fila + 0 - 1) * COLUMNAS + ((hexag.fila + 2) // 2) + hexag.columna - 1 + ((hexag.fila + 2) % 2)) #Arriba Derecha
                                if hexag.columna > 0 or hexag.fila % 2 == 1:
                                    if hexag.fila > 0:
                                        hexag.id_adyacentes.append((hexag.fila + 0 - 1) * COLUMNAS + ((hexag.fila + 2) // 2) + hexag.columna - 2 + ((hexag.fila + 2) % 2)) #Arriba Izquierda
                            #print(f"Nuevo ID: {hexag.id_adyacentes}")
                            #print(f"Color pinchado {colorPinchado}")                            
                            break # Rompemos el bucle para evitar comprobar el resto una vez encontrado
                        else:
                            #hexag.color = BLANCO if hexag.color == colorPinchado else BLANCO #En el caso que queramos pintar de BLANCO el hexagono que ya no está seleccionado
                            hexag.color_borde = GRIS if hexag.color_borde == NEGRO else GRIS
                        
                else:
                    moviendo = False;
                    
                #Comprobamos si ha pulsado en los botones de colores
                pos_clic = pygame.mouse.get_pos()
                idColor = -1 
                for botonColor in BotonesColores:
                    if botonColor.contiene_punto(pos_clic):
                        botonColor.color_borde = GRIS if botonColor.color_borde == NEGRO else NEGRO
                        #print(f"color: {botonColor.color}")
                        colorPinchado = botonColor.color
                        idColor = idColor + 1
                        #break
                    else:
                        botonColor.color_borde = GRIS if botonColor.color_borde == NEGRO else GRIS
                        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            dx, dy = pygame.mouse.get_rel()
            #print(f"PULSADO: INC: F: {dx}, C: {dy} POS F {x_pulsado}, C: {y_pulsado}")
            pintarHexagonos(x_pulsado ,y_pulsado, ANCHO_HEX, ALTO_HEX, False)
            pulsado = True
            
        elif pulsado and evento.type == pygame.MOUSEMOTION:
            moviendo = True
            pintar_info = False
            pantalla_hexagonos.fill(BLANCO)
            #pantalla.fill(BLANCO), ((20, 20), (ANCHO_GLOBAL - 35, 20), (ANCHO_GLOBAL - 35, 930), (17, 930))            
            dx, dy = pygame.mouse.get_rel()
            x_pulsado = x_pulsado + dx
            y_pulsado = y_pulsado + dy
            #print(f"MOVIENDO: INC: F: {dx}, C: {dy} POS F {x_pulsado}, C: {y_pulsado}")                    
            pintarHexagonos(x_pulsado ,y_pulsado, ANCHO_HEX, ALTO_HEX, False)
            actualizar = True
            
        elif evento.type == pygame.MOUSEWHEEL:
            actualizar = True
            if evento.y > 0:
                RADIO_HEX = RADIO_HEX + 1
            elif evento.y < 0:
                RADIO_HEX = RADIO_HEX - 1
            ANCHO_HEX = math.sqrt(3) * RADIO_HEX  # Separación horizontal aproximada (1.732 * radio)
            ALTO_HEX = RADIO_HEX * 1.5            # Separación vertical
                

    if pintar_info:        
        #print("INFO")
        pintarInfo(infof, infoc)
        hexagonos[idHexagono].dibujar(pantalla_hexagonos)        
        if idHexagonoPrevio >= 0:
            hexagonos[idHexagonoPrevio].dibujar(pantalla_hexagonos)
        pantalla.blit(pantalla_hexagonos, (POSX_HEXAGONOS, POSY_HEXAGONOS))                
        #print(f"Fila: {hexagonos[idHexagono].fila}, Col: {hexagonos[idHexagono].columna}")
        BotonesColores[idColor].dibujar(pantalla)
        """
        total = 0
        for adyacentes in hexagonos[idHexagono].id_adyacentes:
            if adyacentes < len(hexagonos):
                if total == 0:
                    hexagonos[adyacentes].color = AZUL
                elif total == 1:
                    hexagonos[adyacentes].color = AMARILLO
                elif total == 2:
                    hexagonos[adyacentes].color = CIAN
                elif total == 3:
                    hexagonos[adyacentes].color = MAGENTA
                elif total == 4:
                    hexagonos[adyacentes].color = TEAL
                elif total == 5:
                    hexagonos[adyacentes].color = MORADO
                ColoresHexagonos[adyacentes].color = hexagonos[adyacentes].color
                ColoresHexagonos[adyacentes].color_borde = hexagonos[adyacentes].color_borde 
                #hexagonos[adyacentes].color = NEGRO
                hexagonos[adyacentes].dibujar(pantalla)
                #print(f"ID: {idHexagono}")
                #print(hexagonos[idHexagono].id_adyacentes)
                #print(f"Fila A: {hexagonos[adyacentes].fila}, Col A: {hexagonos[adyacentes].columna}")
                total = total + 1
        """
    elif actualizar:
        for hexag in hexagonos:
            hexag.dibujar(pantalla_hexagonos)
        pantalla.blit(pantalla_hexagonos, (POSX_HEXAGONOS, POSY_HEXAGONOS))            
        #pygame.draw.polygon(pantalla, BLANCO, ((0, 0), (ANCHO_GLOBAL, 0), (ANCHO_GLOBAL, 950), (0, 950)), 30)        
        pygame.draw.rect(pantalla, BLANCO, [0, ALTO_HEXAGONOS + POSY_HEXAGONOS + 2, ANCHO_GLOBAL, ALTO_GLOBAL]) #ABAJO
        #pygame.draw.rect(pantalla, BLANCO, [0, 0, POSX_HEXAGONOS - 2, ALTO_GLOBAL]) #IZQUIERDA
        #pygame.draw.rect(pantalla, BLANCO, [0, 0, ANCHO_GLOBAL, POSY_HEXAGONOS - 2]) #ARRIBA
        #pygame.draw.rect(pantalla, BLANCO, [POSX_HEXAGONOS + ANCHO_HEXAGONOS + 2, 0, ANCHO_GLOBAL, ALTO_GLOBAL]) #DERECHA
        pygame.draw.polygon(pantalla, AZUL, ((POSX_HEXAGONOS, POSY_HEXAGONOS), (ANCHO_HEXAGONOS + POSX_HEXAGONOS, POSY_HEXAGONOS), (ANCHO_HEXAGONOS + POSX_HEXAGONOS, ALTO_HEXAGONOS + POSY_HEXAGONOS), (POSX_HEXAGONOS, ALTO_HEXAGONOS + POSY_HEXAGONOS)), 5) #TABLERO HEXAGONOS
        pygame.draw.polygon(pantalla, AZUL, ((5, 5), (POSX_HEXAGONOS - 10, 5), (POSX_HEXAGONOS - 10, POSY_HEXAGONOS + ALTO_HEXAGONOS), (5, POSY_HEXAGONOS + ALTO_HEXAGONOS)), 5) #TABLERO COLORES
        #print("TODOS")        
        actualizar = False
                    

    for botonColor in BotonesColores:
        botonColor.dibujar(pantalla)                   

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
