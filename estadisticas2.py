import csv
import pandas as pd

# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv('Histórico-de-Resultados-Bonoloto.csv')

def contar_combinaciones(csv_file):
    # Inicializamos los contadores
    contador_4numeros = 0
    contador_2numeros = 0
    
    # Leemos el archivo CSV
    with open(csv_file, newline='') as archivo:
        lector_csv = csv.DictReader(archivo)
        
        # Iteramos sobre todas las filas del archivo
        for fila in lector_csv:
            # Extraemos los datos de las columnas que necesitamos
            numeros = []
            for i in range(1, 7):
                valor = fila[f'N{i}']
                if valor:
                    numeros.append(int(valor))
            
            # Contamos cuántos números hay del 1 al 25
            contador_1_25 = 0
            for numero in numeros:
                if numero <= 25:
                    contador_1_25 += 1
            
            # Si hay 4 números del 1 al 25, incrementamos el contador de combinaciones de 4-2
            if contador_1_25 == 4:
                contador_4numeros += 1
            
            # Contamos cuántos números hay del 26 al 49
            contador_26_49 = 0
            for numero in numeros:
                if numero >= 26:
                    contador_26_49 += 1
            
            # Si hay 2 números del 26 al 49, incrementamos el contador de combinaciones de 4-2
            if contador_26_49 == 2:
                contador_2numeros += 1
    
    # Imprimimos los resultados
    print(f"Combinación 4-2: {contador_4numeros} veces")
    print(f"Combinación 2-4: {contador_2numeros} veces")

# Ejemplo de uso
contar_combinaciones("Histórico-de-Resultados-Bonoloto.csv")
