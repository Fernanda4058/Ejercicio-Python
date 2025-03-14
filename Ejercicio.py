import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


df = pd.read_csv('./housing.csv')


print(df.head())
print(df.tail())


column = "median_house_value"
media = df[column].mean()
mediana = df[column].median()
moda = df[column].mode()[0]  
rango = df[column].max() - df[column].min()
varianza = df[column].var()
desviacion = df[column].std()


tabla_frecuencias = df[column].value_counts().reset_index()
tabla_frecuencias.columns = [column, "Frecuencia"]


estadisticas = pd.DataFrame({
    "Métrica": ["Media", "Mediana", "Moda", "Rango", "Varianza", "Desviación Estándar"],
    "Valor": [media, mediana, moda, rango, varianza, desviacion]
})

print("\nEstadísticas Descriptivas de median_house_value:\n")
print(estadisticas.to_string(index=False))

print("Tabla de Frecuencias:")
print(tabla_frecuencias.head(10))  

plt.figure(figsize=(12, 6))
plt.bar(df.index[:50], df["median_house_value"][:50], label="Valor de Casa")
plt.bar(df.index[:50], df["population"][:50], alpha=0.5, label="Población")
plt.axhline(media, color="r", linestyle="--", label=f"Media: {media:.2f}")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.title("Comparación de median_house_value con población")
plt.legend()
plt.show()
