    # Aproxima la raiz cuadrada de 2
    # ENTRADA:
    # x0 = aproximacion inicial de la raiz de 2
    # tol = (opcional) tolerancia admitida (valor por defecto: tol = 5e-9)
    # SALIDA:
    # x1 = valor aproximado de la raiz de 2
    # Autor: Luciano Ponzellini Marinelli (2015)
    # Traducción a Python: Gianluca Fassio (2023)
    # Traducción a Python y revisión: Jerónimo Neder (2023)


import math

def rcuad2(x0, tol=5e-9):

      print('\n Valor inicial aproximado:', x0)
      print('\n  n   raiz             error')

      # inicio aproximación
      x1 = 0.5 * (x0 + 2 / x0)
      # calculo error entre aproximaciones
      err = abs(x1 - x0)
      # contador
      k = 1

      # imprimo valor inicial
      print('%3d  %12.15f  %12.15f' % (k, x1, err))

      # verifico convergencia
      while err > tol:
          x0 = x1
          # actualiza termino aproximado
          x1 = 0.5 * (x0 + 2 / x0)
          err = abs(x1 - x0)
          k = k + 1
          # imprimo valores aproximados
          print('%3d  %12.15f  %12.15f' % (k, x1, err))

      # outputs
      print('\nValor final aproximado: %12.15f'% (x1))            #aproximado
      print('Valor exacto Python:    %12.15f' % (math.sqrt(2)))   #exacto
      print('Error absoluto:', abs(x1 - math.sqrt(2))) #error final
      return x1