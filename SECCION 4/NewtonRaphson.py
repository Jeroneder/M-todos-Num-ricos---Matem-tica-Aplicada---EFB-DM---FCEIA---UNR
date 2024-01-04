import numpy as np

def NewtonRaphson(fnom, fpnom, x0, tol, itmax):
    # Método de Newton-Raphson
    # ENTRADA
    # fnom : función que define la ecuación
    # fpnom : derivada de la función fnom
    # x0 : estimación inicial
    # tol : tolerancia
    # itmax : número máximo de iteraciones
    # SALIDA
    # x : raíz aproximada
    # Autores: Javier Signorelli - Javier Sorribas (2010)
    # Modifcacion: Luciano Ponzellini Marinelli (2015)
    # Traducción a Python: Gianluca Fassio (2023)
    # Traducción a Python y revisión: Jerónimo Neder (2023)

    print("Método iterativo de Newton-Raphson\n")
    print("Iter x f(x) Error\n")

    iter = 1
    while True:
        fx = fnom(x0)
        fpx = fpnom(fnom,x0)  # Nótese que tenemos que pasarle la derivada
        x = x0 - fx / fpx

        if abs(x - x0) <= tol and abs(fnom(x)) <= tol:
            print("Se alcanzó la tolerancia.\n")
            print("Resultado final:\nRaíz aproximada %12.6f\n" % x)
            return

        x0 = x
        iter = iter + 1

        if iter > itmax:
            print("Número de iteraciones máximo alcanzado.\n")
            print("Resultado parcial:\nRaíz aproximada = %12.6f\n" % x)
            break