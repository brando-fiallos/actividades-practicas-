import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Librerías cargadas correctamente.")
df = pd.read_csv('Life Expectancy Data.csv')
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas.")
#Explorar los datos
df.head()
df.info()
df.describe()
#Limpiar datos
df['Life expectancy'].fillna(df['Life expectancy'].mean(), inplace=True)
df.drop_duplicates(inplace=True)
df.info()# Filtrar y agrupar
df_ecuador = df[df['Country'] == 'Ecuador']
avg_life_by_region = df.groupby('Region')['Life expectancy'].mean().sort_values(ascending=False)
#Visualizar
#Línea (Ecuador)
plt.figure(figsize=(10,6))
sns.lineplot(data=df_ecuador, x='Year', y='Life expectancy', marker='o')
plt.title('Esperanza de Vida en Ecuador')
plt.show()
#Barras (Regiones)
avg_life_by_region.plot(kind='bar', color=sns.color_palette('coolwarm', len(avg_life_by_region)))
plt.title('Esperanza de Vida Promedio por Región')
plt.show()

# 1. Filtrar datos para los años 2000 y 2015
df_2000 = df[df['Year'] == 2000][['Country', 'Life expectancy']]
df_2015 = df[df['Year'] == 2015][['Country', 'Life expectancy']]

# 2. Unir los datos y calcular la diferencia
df_diff = pd.merge(df_2000, df_2015, on='Country', suffixes=('_2000', '_2015'))
df_diff['Life_Increase'] = df_diff['Life expectancy_2015'] - df_diff['Life expectancy_2000']

# 3. Ordenar y mostrar los 5 países con mayor aumento
top_5_increase = df_diff.sort_values('Life_Increase', ascending=False).head(5)

print("Top 5 países con mayor aumento en esperanza de vida (2000-2015):")
print(top_5_increase[['Country', 'Life_Increase']].to_string(index=False))

# Opcional: Visualización
plt.figure(figsize=(10,6))
sns.barplot(data=top_5_increase, x='Country', y='Life_Increase', palette='viridis')
plt.title('Top 5 Países con Mayor Aumento en Esperanza de Vida (2000-2015)')
plt.ylabel('Aumento en años de esperanza de vida')
plt.xticks(rotation=45)
plt.show()