import numpy as np
import matplotlib.pyplot as plt

# Crear figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Parámetros de la esfera
radio = 1

# Ángulos
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Coordenadas de la esfera
x = radio * np.outer(np.cos(u), np.sin(v))
y = radio * np.outer(np.sin(u), np.sin(v))
z = radio * np.outer(np.ones(np.size(u)), np.cos(v))

# Dibujar superficie
ax.plot_surface(x, y, z)

# Mantener proporciones iguales
ax.set_box_aspect([1, 1, 1])

# Etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title("Esfera 3D")
plt.show()
