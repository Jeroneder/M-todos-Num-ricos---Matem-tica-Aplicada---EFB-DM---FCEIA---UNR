
  # Script: ZoomPoli
  # Plotea (x-1)^6 alrededor de x=1 con escala creciente
  # pero evaluado via x^6 - 6x^5 + 15x^4 - 20x^3 + 15x^2 - 6x +1
  # 05.04.2015 (Sergio Preidikman)
  # 29.10.2015 (Luciano Ponzellini Marinelli)
  # Traducción a Python: Gianluca Fassio (2023)
  # Traducción a Python y revisión: Jerónimo Neder (2023)


import numpy as np
import matplotlib.pyplot as plt

# Definir variables
k = 0
n = 100
deltas = [0.1, 0.01, 0.008, 0.007, 0.005, 0.003]

# Crear subplots
fig, axs = plt.subplots(2, 3, figsize=(10, 6))

# Plotear para cada valor de delta
for delta in deltas:
    x = np.linspace(1 - delta, 1 + delta, n)
    y = x ** 6 - 6 * x ** 5 + 15 * x ** 4 - 20 * x ** 3 + 15 * x ** 2 - 6 * x + 1
    y1 = (x - 1) ** 6
    k += 1
    ax = axs[(k-1)//3, (k-1)%3]
    ax.plot(x, y, label=r'$x^6 - 6x^5 + 15x^4 - 20x^3 + 15x^2 - 6x + 1$')
    ax.plot(x, y1, label=r'$(x-1)^6$')
    ax.plot(x, np.zeros_like(x), 'k--')
    ax.grid(True)
    ax.set_xlim(1 - delta, 1 + delta)
    ax.set_ylim(-np.max(np.abs(y)), np.max(np.abs(y)))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
   #ax.legend(loc='upper left')

plt.tight_layout()
#plt.savefig('ZoomPoli.png') # Guardar figura en el directorio actual
plt.show()