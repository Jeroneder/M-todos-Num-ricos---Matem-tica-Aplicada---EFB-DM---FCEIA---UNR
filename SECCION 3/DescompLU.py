import numpy as np

def DescompLU(A, b):
    """
    Cálculo solución del sistema lineal Ax=b mediante descomposición LU
    Datos:
      A matriz invertible nxn
      b vector nx1
    Resultado:
      x solucion nx1 del sistema Ax=b

    Autores: Javier Signorelli - Javier Sorribas (2010)
    Modificación: Luciano Ponzellini Marinelli (2015)
    Traducción a Python y revisión: Jerónimo Neder (2023)

    """

    n, _ = A.shape

    for q in range(n-1):
        # Pivoteo parcial con escalonamiento
        S = np.max(np.abs(A[q:n, q:n]), axis=1)
        j = np.argmax(np.abs(A[q:n, q]) / S) + q

        # Intercambio de la fila q-ésima con la fila k-ésima
        A[[q, j], :] = A[[j+q, q], :]
        b[q], b[j] = b[j], b[q]

        # Verificación de la invertibilidad de la matriz
        if A[q, q] == 0:
            print('A no es inversible. No hay solución o no es única')
            return None

        # Proceso de eliminación en la columna q-ésima
        for k in range(q+1, n):
            m = A[k, q] / A[q, q]
            A[k, q] = m
            A[k, q+1:] = A[k, q+1:] - m * A[q, q+1:]

    # Resolución para determinar y con sustitución progresiva (hacia adelante)
    y = np.zeros(n)
    for k in range(n):
        y[k] = b[k] - np.dot(A[k, :k], y[:k])

    # Resolución para determinar x con sustitución regresiva (hacia atrás)
    x = np.zeros(n)
    x[n-1] = y[n-1] / A[n-1, n-1]
    for k in range(n-2, -1, -1):
        x[k] = (y[k] - np.dot(A[k, k+1:], x[k+1:])) / A[k, k]

    return x