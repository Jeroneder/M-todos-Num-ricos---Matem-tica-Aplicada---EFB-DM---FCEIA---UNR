import numpy as np
from diagdom import diagdom

def Jacobi(A, b, x0, tol, itmax):
    """
    Método iterativo de Jacobi
    A     : matriz invertible nxn
    b     : lado derecho nx1
    x0    : estimación inicial nx1
    tol   : tolerancia
    itmax : número máximo de iteraciones
    x     : vector nx1 aproximación solución SEL Ax=b
    Traducción a Python: Gianluca Fassio (2023)
    """
    n = len(b)
    x0 = x0.reshape((n, 1))

    if not diagdom(A):
        print('No se garantiza convergencia')

    iter = 0

    while True:
        iter += 1

        x = np.zeros((n, 1))
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if j != i:
                    x[i] -= A[i, j] * x0[j]
            x[i] /= A[i, i]

        err = np.linalg.norm(x - x0, ord=2)
        #print(err)

        if err < tol:
            return x.reshape((n,))

        if iter == itmax:
            print('Número máximo de iteraciones alcanzado')
            return x.reshape((n,))

        x0 = x