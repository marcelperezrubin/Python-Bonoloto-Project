#Esto es un programa que genera 1 combinación de 2 numeros del 1 al 25 de Bono-Loto que no han salido
# basandose en un archivo historico, tambien genera 1 combinación de 4 numeros del 26 al 49 que no han salido.
# Se llama combinacion 2-4


import random
import csv

# Abrir el archivo csv y leer los números del historial
with open('Histórico-de-Resultados-Bonoloto.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Saltar la primera fila que contiene encabezados
    numeros_historial = set()
    for fila in lector_csv:
        numeros_historial.update(fila[1:7])

# Generar combinación de 2 números que no estén en el historial
numeros_disponibles = set(range(1, 26)) - numeros_historial
combinacion_2_numeros = random.sample(list(numeros_disponibles), 2)

# Generar combinación de 4 números que no estén en el historial
numeros_disponibles = set(range(26, 50)) - numeros_historial
combinacion_4_numeros = random.sample(list(numeros_disponibles), 4)

# Mostrar las combinaciones generadas
print(f'Combinación de 2 números: {combinacion_2_numeros}')
print(f'Combinación de 4 números: {combinacion_4_numeros}')
