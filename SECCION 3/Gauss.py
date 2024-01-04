import numpy as np

def Gauss(A, b):
    """
    Cálculo solución del sistema lineal Ax=b mediante eliminación Gaussiana
    Datos:
      A matriz invertible nxn
      b vector nx1
    Resultado:
      x solucion nx1 del sistema Ax=b

    Autores: Javier Signorelli - Javier Sorribas (2010)
    Modificación: Luciano Ponzellini Marinelli (2015)
    Traducción a Python y revisión: Jerónimo Neder (2023)

    """
    # Inicialización
    n, _ = A.shape #utilizar '_' como nombre de variable es común cuando no necesitas utilizar el valor de esa variable.

    # Cálculo de la matriz ampliada
    Aum = np.hstack((A, b.reshape(-1, 1)))

    for q in range(n-1):
        # Pivoteo parcial con escalonamiento
        S = np.max(np.abs(Aum[q:, q:-1]), axis=1)
        j = np.argmax(np.abs(Aum[q:, q]) / S) + q

        # Intercambio fila q-ésima con fila j-ésima
        C = np.copy(Aum[q, :])
        Aum[q, :] = Aum[j, :]
        Aum[j, :] = C

        # Verificación
        if Aum[q, q] == 0:
            print('A no es inversible. No hay solución o no es única')
            return None

        # Proceso de eliminación en columna q-ésima
        for k in range(q+1, n):
            m = Aum[k, q] / Aum[q, q]
            Aum[k, q:] = Aum[k, q:] - m * Aum[q, q:]

    # Sustitución regresiva (hacia atrás)
    x = np.zeros(n)
    x[-1] = Aum[-1, -1] / Aum[-1, -2]
    for k in range(n-2, -1, -1):
        x[k] = (Aum[k, -1] - np.dot(Aum[k, k+1:n], x[k+1:])) / Aum[k, k]

    return x