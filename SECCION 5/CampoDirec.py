import math as m
import numpy as np
import matplotlib.pyplot as plt

def CampoDirec(xmin, xmax, ymin, ymax, fpvi):
    # Generar una cuadrícula de puntos en el dominio
    T, Y = np.meshgrid(np.linspace(xmin, xmax, 20), np.linspace(ymin, ymax, 20))

    # Calcular las derivadas con respecto al tiempo y a la variable dependiente
    dT = np.ones_like(T)
    dY = fpvi(T, Y)

    # Crear la figura y graficar el campo de direcciones
    plt.figure()
    plt.quiver(T, Y, dT, dY, scale=20)
    plt.title('Campo de Direcciones')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend(['Campo de direcciones'])
    plt.show()