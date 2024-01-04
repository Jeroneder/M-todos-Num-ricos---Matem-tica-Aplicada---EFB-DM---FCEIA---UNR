import numpy as np

def diagdom(A):
    """
    Determina si la matriz A es diagonalmente dominante
    Entrada:
        A: matriz invertible nxn
    Salida:
        z: variable lógica: False (0) o True (1)
    Autores: Javier Signorelli - Javier Sorribas (2010)
    Modificación: Luciano Ponzellini Marinelli (2015)
    Traducción a Python: Gianluca Fassio (2023)
    Traducción a Python y revisión: Jerónimo Neder (2023)

    """
    n = A.shape[0]
    i = 0
    z = True

    while (i < n and z == True):
        i += 1
        if np.sum(np.abs(A[i-1,:])) >= 2*np.abs(A[i-1,i-1]):
            z = False

    return z