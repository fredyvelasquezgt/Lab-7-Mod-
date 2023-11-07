#Inciso 3.
#Calcular el valor esperado de una variable aleatoria exponencial con λ = 1, utilizando el método estratificado. 
#Se escogen tres estratos (intervalos) de 0 a 1, de 1 a 3 y de 3 a ∞

# Parámetros del generador congruencial lineal
m = 2**32  # Módulo - 2^32 nos asegurarmos de que los números generados estén dentro del rango [0, 1].
a = 1664525  # Se utiliza en la ecuación para generar números pseudoaleatorios y debe ser un número entero positivo.
c = 1013904223  # Define el incremento.
seed = 12345  # Semilla inicial

# Función para generar números pseudoaleatorios entre 0 y 1
def generar_numero_aleatorio():
    global seed  # Declaración para indicar que la variable seed se refiere a la variable definida fuera de la función.
    seed = (a * seed + c) % m  # Definición de la ecuación del generador congruencial lineal.
    return seed / m  # La función devuelve el valor generado normalizado en el rango [0, 1) dividiendo la semilla actual por el módulo (m).

# Número de estratos
n_estratos = 3

# Límites de los estratos
limites_estratos = [0, 1, 3, float('inf')]

# Inicializa una lista para almacenar los valores esperados de cada estrato
valores_esperados_estratos = [0] * n_estratos

# Función de densidad de probabilidad de la exponencial con λ = 1
def pdf_exponencial(x, lmbda=1):
    return lmbda * 2.71828 ** (-lmbda * x)

# Genera números aleatorios en cada estrato y calcula los valores esperados
for i in range(n_estratos):
    a = limites_estratos[i]
    b = limites_estratos[i + 1]
    n = 10000  # Número de muestras en el estrato 

    valores = []
    for _ in range(n):
        u = generar_numero_aleatorio()  # Genera un número pseudoaleatorio
        x = a - (1 / 1) * (0 - 2.71828 ** (-1 * a) - u * (2.71828 ** (-1 * a) - 2.71828 ** (-1 * b)))
        valores.append(x)

    valores_esperados_estratos[i] = sum(valores) / n  # Calcula el valor esperado del estrato

# Imprime los valores esperados de los estratos con saltos de línea
for i, valor_estrato in enumerate(valores_esperados_estratos):
    limite_inferior = limites_estratos[i]
    limite_superior = limites_estratos[i + 1] if i < n_estratos - 1 else "∞"
    print(f"Valor esperado para el estrato {limite_inferior} a {limite_superior}: {valor_estrato}")


# Calcula el valor esperado total promediando los valores de los estratos
valor_esperado_total = sum(valores_esperados_estratos) / n_estratos

# Imprime el resultado
print("\nValor esperado total:", valor_esperado_total)
