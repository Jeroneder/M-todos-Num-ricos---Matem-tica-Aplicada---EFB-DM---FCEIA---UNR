import numpy as np
from numpy.linalg import norm
from diagdom import diagdom

def GaussSeidel(A, b, x0, tol, itmax):
    """
    Método Iterativo de Gauss-Seidel
    A     : matriz invertible nxn
    b     : lado derecho nx1
    x0    : estimacion inicial nx1
    tol   : tolerancia
    itmax : numero maximo de iteraciones
    x     : vector nx1 aproximacion a la solucion SEL Ax=b

    Autores: Javier Signorelli - Javier Sorribas (2010)
    Modificacion: Luciano Ponzellini Marinelli (2015)
    Traducción a Python y revisión: Jerónimo Neder (2023)

    """

    n = len(b)
    x0 = np.transpose(x0)

    if not diagdom(A):
        print('No se garantiza convergencia')


    #x = x0 #de esta forma se genera un efecto reflejo. Python almacena varibles como etiquetas
                                  #si defino x=x0 entiende que modificar x es modificar x0
                                  #pues es x es otra etiqueta para un mismo valor almacena con etiqueta x0
    x0 = x0.astype(float).reshape((n, 1))  # Convertir a punto flotante componentes del vector
    x = np.copy(x0) #solución del problema del reflejo de variables

    #Chequear bien
    #x = np.zeros((n, 1))

    iter = 0
    while True:
        iter = iter + 1


        #x = np.zeros((n, 1))

        for i in range(n):
            x[i] = b[i]
            #print(x[i])
            for j in range(n):
                if j != i:
                    x[i] = x[i] - A[i,j]*x[j]

            #print(x[i])
            #print(x[i]/A[i,i])
            #print(np.divide(x[i],A[i,i]))
            s = np.divide(x[i],A[i,i])
            #print(s)
            x[i] = s.copy()
            #print(x[i])
            #print(2)
            #print(x[i]/A[i,i])
            #print(x0)

        err = norm(x - x0, 2)
        #print(err)

        if err < tol:
           #print(iter) # Maximo de iteraciones, donde corto la tol
            x = np.transpose(x)
            return x

        if iter == itmax:
            print('Número máximo de iteraciones alcanzado')
            x = np.transpose(x)
            return x

        x0 = np.copy(x)