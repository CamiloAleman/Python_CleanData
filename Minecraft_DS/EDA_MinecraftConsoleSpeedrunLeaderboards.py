import pandas as pd
import re
pd.options.display.max_columns = None
#pd.set_option("large_repr", "info")

df = pd.read_csv('mce.csv')
list = df.values.tolist()
for i in range(5):
    print(list[i])
    print('\n')

print(df.head(10), '\n')


#Para saber el porcentaje de valores nulos por columna
nanValues = df.isnull().sum() * 100/ len(df)
nanValdf = pd.DataFrame({'column': df.columns , 'percent': nanValues})
nanValdf['percent'] = nanValdf['percent'].apply(lambda x: f'{x:.4f}%')

print('Missing values percentage per column:')
print(nanValdf, '\n')

#información general acerca de los tipos de datos
print(df.info())

#Remover espacios innecesarios de valores String
df = df.map(lambda x: re.sub(r'\s+', ' ', str(x).strip()))



