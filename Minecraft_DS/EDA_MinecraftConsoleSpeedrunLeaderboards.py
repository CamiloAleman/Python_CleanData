import pandas as pd
import re
pd.options.display.max_columns = None
#pd.set_option("large_repr", "info")


df = pd.read_csv('mce.csv')
list = df.values.tolist()
for i in range(5):
    print(list[i])
    print('\n')

#Para saber el porcentaje de valores nulos por columna
nanValues = df.isnull().sum() * 100/ len(df)
nanValdf = pd.DataFrame({'column': df.columns , 'percent': nanValues})
nanValdf['percent'] = nanValdf['percent'].apply(lambda x: f'{x:.4f}%')

print('Missing values percentage per column:')
print(nanValdf, '\n')

#Información general acerca de los tipos de datos
print(df.info(), '\n')

#Remover espacios innecesarios de valores String
df = df.map(lambda x: re.sub(r'\s+', ' ', str(x).strip()))

#Para fechas de verificación - separación de fechas y horas
df['verify_date'] = pd.to_datetime(df['verify_date'])
df['verify_shortDate'] = pd.to_datetime(df['verify_date']).dt.date
df['verify_day'] = pd.to_datetime(df['verify_date']).dt.day
df['verify_month'] = pd.to_datetime(df['verify_date']).dt.month
df['verify_year'] = pd.to_datetime(df['verify_date']).dt.year
df['verify_hour'] = pd.to_datetime(df['verify_date']).dt.hour

#Para las fechas y horas de submisión
df['submitted_date'] = pd.to_datetime(df['submitted_date'])
df['submitted_shortDate'] = pd.to_datetime(df['submitted_date']).dt.date
df['submitted_day'] = pd.to_datetime(df['submitted_date']).dt.day
df['submitted_month'] = pd.to_datetime(df['submitted_date']).dt.month
df['submitted_year'] = pd.to_datetime(df['submitted_date']).dt.year
df['submitted_hour'] = pd.to_datetime(df['submitted_date']).dt.hour

#Para las fechas y horas de Creación de cuenta de los usuarios
df['player_signup_date'] = pd.to_datetime(df['player_signup_date'])
df['player_signup_shortDate'] = pd.to_datetime(df['player_signup_date']).dt.date
df['player_signup_day'] = pd.to_datetime(df['player_signup_date']).dt.day
df['player_signup_month'] = pd.to_datetime(df['player_signup_date']).dt.month
df['player_signup_year'] = pd.to_datetime(df['player_signup_date']).dt.year
df['player_signup_hour'] = pd.to_datetime(df['player_signup_date']).dt.hour

#Limpieza de strigs vacíos
df['player_id'].fillna("Non avaible", inplace=True)
df['verify_date'].fillna("Non avaible", inplace=True)
df['examiner_id'].fillna("Non avaible", inplace=True)
df['level_id'].fillna("Non avaible", inplace=True)
df['level_name'].fillna("Non avaible", inplace=True)
df['player_name'].fillna("Non avaible", inplace=True)
df['player_country'].fillna("Non avaible", inplace=True)
df['player_pronouns'].fillna("Non avaible", inplace=True)

#Limpieza de números vacíos
df['level_rules'].fillna(0, inplace=True)

cleandf = df
cleandf.to_csv('cleanmce.csv')

print(df.head(10), '\n')



