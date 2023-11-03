#Esto es un programa que genera 1 combinación de 3 numeros de Bono-Loto que no han salido
# basandose en un archivo historico, tambien genera 1 combinación de 3 numeros que no han salido.
# Se llama combinacion 3-3

import random
import csv

# Abrir el archivo csv y leer los números del historial
with open('Histórico-de-Resultados-Bonoloto.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Saltar la primera fila que contiene encabezados
    numeros_historial = set()
    for fila in lector_csv:
        numeros_historial.update(fila[1:7])

# Generar combinación de 3 números que no estén en el historial (del 1 al 25)
numeros_disponibles_1 = set(range(1, 26)) - numeros_historial
combinacion_3_numeros_1 = random.sample(list(numeros_disponibles_1), 3)

# Generar combinación de 3 números que no estén en el historial (del 26 al 49)
numeros_disponibles_2 = set(range(26, 50)) - numeros_historial
combinacion_3_numeros_2 = random.sample(list(numeros_disponibles_2), 3)

# Mostrar las combinaciones generadas
print(f'Combinación de 3 números (1 al 25): {combinacion_3_numeros_1}')
print(f'Combinación de 3 números (26 al 49): {combinacion_3_numeros_2}')
