import numpy as np
import matplotlib.pyplot as plt

def RungeKutta4(fnom, a, b, y0, n):
  """

   Método de Runge-Kutta 4to orden para aproximar la solución de un PVI
   ENTRADA
   fnom   : nombre de la función que define la EDO y'= f(t,y)
   a,b    : extremos del intervalo [a,b]
   y0     : condición inicial y(t0)=y0
   n      : número de pasos
   SALIDA
   t      : vector de abscisas
   y      : vector de ordenadas

  Autor: Luciano Ponzellini Marinelli (2023)
  Traducción a Python: Gianluca Fassio (2023)
  Traducción a Python y revisión: Jerónimo Neder (2023)

  """

  h = (b-a)/n
  t = np.linspace(a, b, n+1)
  y = np.zeros(n+1)
  y[0] = y0

  print('%3s  %10s  %10s' % ('k', 't', 'y'))
  print('%3d  %10.6f  %10.6f' % (0, t[0], y[0]))

  for k in range(n):
        k1 = h * fnom(t[k], y[k])
        k2 = h * fnom(t[k] + h/2, y[k] + k1/2)
        k3 = h * fnom(t[k] + h/2, y[k] + k2/2)
        k4 = h * fnom(t[k] + h, y[k] + k3)
        y[k+1] = y[k] + (k1 + 2*k2 + 2*k3 + k4) / 6
        print('%3d  %10.6f  %10.6f' % (k+1, t[k+1], y[k+1]))

  print('Tamaño del paso: %12.6f' % h)
  print('Número de pasos: %3d' % n)
  return t, y