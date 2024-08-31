import pandas as pd
import re
pd.options.display.max_columns = None
#pd.set_option("large_repr", "info")

df = pd.read_csv('netflix_titles.csv')

print(df.head(10), '\n')

list = df.values.tolist()
for i in range(10):
    print(list[i])
    print()
print('\n')

#Para saber el porcentaje de valores nulos por columna
nanValues = df.isnull().sum() * 100/ len(df)
nanValdf = pd.DataFrame({'column': df.columns , 'percent': nanValues})
nanValdf['percent'] = nanValdf['percent'].apply(lambda x: f'{x:.4f}%')

print(nanValdf, "\n")

print(df.info(), "\n") 

#Limpieza de espacios en blanco para todas las columnas como cast o descripción
df = df.map(lambda x: re.sub(r'\s+', ' ', str(x).strip()))

#Limpieza de datos y separación de fechas en distintas columnas
df['date_added'] = pd.to_datetime(df['date_added'])
df['day_added'] = pd.to_datetime(df['date_added']).dt.day
df['month_added'] = pd.to_datetime(df['date_added']).dt.month
df['year_added'] = pd.to_datetime(df['date_added']).dt.year
df.fillna("Not Avaible")

#Inserción de datos en nuevo dataset
cleandf = df
cleandf.to_csv('cleanNetflix_df.csv')

print(cleandf.head(10), '\n')