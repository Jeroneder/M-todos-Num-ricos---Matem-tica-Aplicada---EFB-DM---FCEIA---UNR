  # Script: ExpTaylor
  # Plotea como funcion de la cantidad de terminos n,
  # el error relativo del Taylor de exp(x):
  # T(e^x,0) = 1 + x + x^2/2! +...+ x^n/n!
  # 05.04.2015 (Sergio Preidikman)
  # 11.06.2017 (Luciano Ponzellini Marinelli)
  # Traducción a Python: Gianluca Fassio (2023)
  # Traducción a Python y revisión: Jerónimo Neder (2023)


import numpy as np
import matplotlib.pyplot as plt

nTerms = 50
xx = np.array([1, 5, 10, -1, -5, -10])

for i in range(len(xx)):
    x = xx[i]
    f = np.exp(x) * np.ones(nTerms)
    s = 1
    term = 1
    err = np.zeros(nTerms)
    for k in range(1, nTerms+1):
        term = x * term / k
        s += term
        err[k-1] = abs(f[k-1] - s)
    relerr = err / np.exp(x)
    plt.subplot(2, 3, i+1)
    plt.semilogy(np.arange(1, nTerms+1), relerr)
    plt.grid(True)
    plt.ylabel('Error Relativo Suma Parcial', fontsize=12)
    plt.xlabel('Orden Suma Parcial', fontsize=12)
    plt.title(f'x = {x:5.2f}')
    plt.axis([0, 50, 1e-20, 1e10])

plt.tight_layout()
plt.show()