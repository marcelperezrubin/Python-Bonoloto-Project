#Esto es un programa que genera 1 combinación de 5 numeros del 1 al 25 de Bono-Loto que no han salido
# basandose en un archivo historico, tambien genera 1 combinación de 1 numero del 26 al 49 que no han salido.
# Se llama combinacion 5-1

import random
import csv

# Abrir el archivo csv y leer los números del historial
with open('Histórico-de-Resultados-Bonoloto.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Saltar la primera fila que contiene encabezados
    numeros_historial = set()
    for fila in lector_csv:
        numeros_historial.update(fila[1:7])

# Generar combinación de 5 números que no estén en el historial
numeros_disponibles = set(range(1, 26)) - numeros_historial
combinacion_5_numeros = random.sample(list(numeros_disponibles), 5)

# Generar combinación de 1 número que no estén en el historial
numeros_disponibles = set(range(26, 50)) - numeros_historial
combinacion_1_numeros = random.sample(list(numeros_disponibles), 1)

# Mostrar las combinaciones generadas
print(f'Combinación de 5 números: {combinacion_5_numeros}')
print(f'Combinación de 1 número: {combinacion_1_numeros}')

