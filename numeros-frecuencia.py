import pandas as pd

# Carga el archivo csv en un DataFrame de Pandas
df = pd.read_csv("Histórico-de-Resultados-Bonoloto.csv")

# Crea una serie que contiene todos los números que han salido
numeros = pd.concat([df["N1"], df["N2"], df["N3"], df["N4"], df["N5"], df["N6"]], ignore_index=True)

# Calcula la frecuencia de aparición de cada número
frecuencia_numeros = numeros.value_counts()

# Imprime los 6 números que más han salido
print("Los 6 números que más han salido son:")
print(frecuencia_numeros.head(6))

# Imprime los 6 números que menos han salido
print("Los 6 números que menos han salido son:")
print(frecuencia_numeros.tail(6))
