import numpy as np
import matplotlib.pyplot as plt

def Euler(f, a, b, y0, n):
    """
    Método de Euler para aproximar la solución de un PVI

    ENTRADA:
    f     : función que define la EDO y' = f(t, y)
    a,b   : extremos del intervalo [a,b]
    y0    : condición inicial y(a) = y0
    n     : número de pasos

    SALIDA:
    t     : vector de abscisas
    y     : vector de ordenadas

    Autor: Luciano Ponzellini Marinelli (2015)
    Traducción a Python: Gianluca Fassio (2023)
    Traducción a Python y revisión: Jerónimo Neder (2023)

    """

    print(' Método de Euler')
    print(' k         t_k            y_k ')

    h = (b-a)/n
    t = np.linspace(a, b, n+1)
    y = np.zeros(n+1)
    y[0] = y0

    print('{:3d}  {:10.6f}  {:10.6f}'.format(0, t[0], y[0]))

    for k in range(n):
        y[k+1] = y[k] + h*f(t[k], y[k])
        print('{:3d}  {:10.6f}  {:10.6f}'.format(k+1, t[k+1], y[k+1]))

    print('Tamaño del paso: {:12.6f}'.format(h))
    print('Número de pasos: {:3d}'.format(n))

    return t, y