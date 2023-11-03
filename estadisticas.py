import pandas as pd
import random

# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv('Histórico-de-Resultados-Bonoloto.csv')

# Convierte la columna de números a valores numéricos y filtra los valores nulos
df[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']] = df[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']].apply(pd.to_numeric, errors='coerce')
df = df.dropna(subset=['N1', 'N2', 'N3', 'N4', 'N5', 'N6'])

# Crea una lista de combinaciones que ya existen en el archivo CSV
combinaciones_existentes = set(zip(df['N1'], df['N2'], df['N3'], df['N4'], df['N5'], df['N6']))

# Función que genera estadísticas sobre los números que han salido en el histórico de la lotería Bonoloto
def estadisticas_numeros():
    numeros = {}
    for i in range(1, 50):
        numeros[i] = 0
    for c in combinaciones_existentes:
        for n in c:
            if pd.notnull(n):
                numeros[int(n)] += 1
    numeros_bajos = sum(numeros[i] for i in range(1, 26))
    numeros_altos = sum(numeros[i] for i in range(26, 50))
    print(f"Números que más han salido: {sorted(numeros, key=numeros.get, reverse=True)[:6]}")
    print(f"Números del 1 al 25 han salido {numeros_bajos} veces")
    print(f"Números del 26 al 49 han salido {numeros_altos} veces")

# Genera dos combinaciones aleatorias que no existen en el archivo CSV
combinaciones_nuevas = []
while len(combinaciones_nuevas) < 2:
    nueva_combinacion = tuple(random.sample(range(1, 50), 6))
    if nueva_combinacion not in combinaciones_existentes:
        combinaciones_nuevas.append(nueva_combinacion)

# Imprime las dos combinaciones aleatorias que no existen en el archivo CSV
print("Dos combinaciones aleatorias que no existen en el archivo histórico son:")
for c in combinaciones_nuevas:
    c_ordenada = tuple(sorted(c))
    print(c_ordenada)

# Genera estadísticas sobre los números que han salido en el histórico de la lotería Bonoloto
estadisticas_numeros()
