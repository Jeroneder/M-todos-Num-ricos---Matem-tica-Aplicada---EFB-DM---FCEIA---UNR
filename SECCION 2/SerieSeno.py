 #Script: SerieSeno
    # Evalúa la representación en serie de la función SENO
    # ssum = SerieSeno(x,tol,n)
    # ENTRADA:
    # x:     argumento de la funcion SENO
    # tol:   (opcional) tolerancia admitida para sumatoria (por defecto: tol = 5e-9)
    #        La serie termina cuando abs(T_k/S_k) < tol,  donde:
    #        T_k:   k-ésimo término y S_k suma incluyendo el k-ésimo término
    # n:     (opcional) máximo número de términos no nulos (por defecto: n = 15)
    #
    # RESULTADO:
    # ssum: valor de la serie al cabo de n términos o al satisfacer la tolerancia
    #
    # Autores: Javier Signorelli - Javier Sorribas (2010)
    # Modificacion: Luciano Ponzellini Marinelli (2015)
    # Traducción a Python: Gianluca Fassio (2023)
    # Traducción a Python y revisión: Jerónimo Neder (2023)


import math

def SerieSeno(x, tol=5e-9, n=15):

    term = x  # Inicializa la serie
    ssum = term
    print('Valor aproximado de la función seno ({})\n\n  n   término     serie'.format(x))
    print('{:3d} {:11.3e} {:12.8f}'.format(1, term, ssum))

    for k in range(3, 2*n, 2):
        term = -term * x**2 / (k * (k-1))  # Próximo término en la serie
        ssum += term
        print('{:3d} {:11.3e} {:12.8f}'.format(k, term, ssum))
        if abs(term / ssum) < tol:  # Verifica convergencia
            break

    print('\n Error Total incluyendo {} términos es {}\n\n'.format((k+1)//2, abs(ssum-math.sin(x))))

    return ssum
