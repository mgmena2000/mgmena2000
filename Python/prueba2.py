import turtle
import random

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Detectar clic en cuadrados aleatorios")
ventana.setup(width=600, height=600)

# Clase para gestionar cada cuadrado
class Cuadrado:
    def __init__(self, x, y, lado):
        self.x_min = x
        self.y_min = y
        self.lado = lado
        self.x_max = x + lado
        self.y_max = y + lado
        
    def dibujar(self, tortuga):
        tortuga.penup()
        tortuga.goto(self.x_min, self.y_min)
        tortuga.pendown()
        for _ in range(4):
            tortuga.forward(self.lado)
            tortuga.left(90)
            
    def contiene_punto(self, x, y):
        # Verifica si las coordenadas (x, y) están dentro de este cuadrado
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max

# Tortuga auxiliar para dibujar en pantalla
dibujante = turtle.Turtle()
dibujante.speed(0)
dibujante.hideturtle()

# Lista global para almacenar los objetos Cuadrado creados
lista_cuadrados = []

# Generar 5 cuadrados aleatorios
for i in range(5):
    # Posiciones al azar (dejando margen para que no se salgan de la pantalla de 600x600)
    x_azar = random.randint(-250, 150)
    y_azar = random.randint(-250, 150)
    lado_azar = random.randint(40, 100)
    
    # Crear el objeto y guardarlo en la lista
    nuevo_cuadrado = Cuadrado(x_azar, y_azar, lado_azar)
    lista_cuadrados.append(nuevo_cuadrado)
    
    # Dibujarlo
    nuevo_cuadrado.dibujar(dibujante)

# Función que maneja el evento del clic
def manejar_clic(x, y):
    ha_tocado_alguno = False
    
    # Revisamos todos los cuadrados guardados
    for indice, cuadrado in enumerate(lista_cuadrados):
        if cuadrado.contiene_punto(x, y):
            print(f"¡Le diste al Cuadrado #{indice + 1}! (Coordenadas del clic: {int(x)}, {int(y)})")
            ha_tocado_alguno = True
            
    if not ha_tocado_alguno:
        print(f"Clic al aire en: ({int(x)}, {int(y)})")

# Escuchar clics en la pantalla
ventana.onscreenclick(manejar_clic)

ventana.mainloop()
