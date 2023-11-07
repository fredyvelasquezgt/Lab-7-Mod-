#Inciso 3.
#Calcular el valor esperado de una variable aleatoria exponencial con λ = 1, utilizando el método estratificado. 
#Se escogen tres estratos (intervalos) de 0 a 1, de 1 a 3 y de 3 a ∞

import random

# Número de estratos
n_estratos = 3

# Límites de los estratos
limites_estratos = [0, 1, 3, float('inf')]

# Inicializa una lista para almacenar los valores esperados de cada estrato
valores_esperados_estratos = [0] * n_estratos

# Función de densidad de probabilidad de la exponencial
def pdf_exponencial(x, lmbda=1):
    return lmbda * 2.71828 ** (-lmbda * x)

# Genera números aleatorios en cada estrato y calcula los valores esperados
for i in range(n_estratos):
    a = limites_estratos[i]
    b = limites_estratos[i + 1]
    n = 10000  # Número de muestras en el estrato 

    valores = []
    for _ in range(n):
        u = random.random()  # Genera un número aleatorio uniforme en el intervalo [0, 1]
        x = a - (1 / 1) * (0 - 2.71828 ** (-1 * a) - u * (2.71828 ** (-1 * a) - 2.71828 ** (-1 * b)))
        valores.append(x)

    valores_esperados_estratos[i] = sum(valores) / n  # Calcula el valor esperado del estrato

# Calcula el valor esperado total promediando los valores de los estratos
valor_esperado_total = sum(valores_esperados_estratos) / n_estratos

# Imprime el resultado
print(" \nValor esperado total:\n", valor_esperado_total)
