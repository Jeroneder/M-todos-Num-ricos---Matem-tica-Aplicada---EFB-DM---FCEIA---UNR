import numpy as np
from df1dx import df1dx

def NewtonRaphsonDeriv(fnom, x0, tol, itmax):
    """
    Método de Newton-Raphson utilizando derivación numérica
    ENTRADA
    fnom    : nombre función que define la ecuación
    x0      : estimación inicial
    tol     : tolerancia
    itmax   : número máximo de iteraciones
    SALIDA
    x       : raíz aproximada
    USAMOS
    dfidx   : función que calcula la derivada numérica primera aproximada

    Autores: Javier Signorelli - Javier Sorribas (2010)
    Modifcacion: Luciano Ponzellini Marinelli (2015)
    Traducción a Python: Gianluca Fassio (2023)
    Traducción a Python y revisión: Jerónimo Neder (2023)

    """

    print(' Método iterativo de Newton-Raphson con derivada numérica\n')
    print(' Iter      x         f(x)        Error \n')

    iter = 1

    while True:
        fx = fnom(x0)
        fpx = df1dx(fnom, x0)
        x = x0 - fx/fpx

        print('%3.0f  %10.6f  %10.6f  %10.6f \n' % (iter, x, fnom(x), abs(x-x0)))

        if abs(x-x0) <= tol and abs(fnom(x)) <= tol:
            print(' Se alcanzó la tolerancia. \n\n')
            print(' Resultado final:\n Raíz aproximada %12.6f \n' % x)
            return x

        x0 = x
        iter = iter + 1

        if iter > itmax:
            print(' Número de iteraciones máximo alcanzado. \n\n')
            print(' Resultado parcial:\n Raíz aproximada = %12.6f \n' % x)
            break