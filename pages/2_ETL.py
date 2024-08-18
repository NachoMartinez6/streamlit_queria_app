import streamlit as st

# st.write("Hello World")

st.sidebar.success("Select a page above.")


############################## 1. Extracción de nuestra DATA

st.markdown("""# Proyecto QuerIA

## 1. Extracción de nuestra DATA

**Paso previo:** Recogida por parte de nuestro analista de los registros correspondientes a datos de electricidad, gas y otros aspectos del panorama energetico dentro de la Unión europea.

**Objetivo:** En este apartado se pretende subir los 3 datasets crudos, concatenarlos en un unico dataset final energy_dataset y transformar los datos, ya que el energy_dataset se cargará al servidor en la nube y tiene que ser facilmente interpretable por la IA para transformar nuestra consulta a lenguaje SQL y devolver una respuesta clara y precisa.""")



    
code = """ 
# Import our libraries
import pandas as pd
import warnings

warnings.filterwarnings(
    'ignore',
    '.*',
    UserWarning,
    'warnings_filter',
)
"""

st.code(code, language="python")


code = """ 
# Dataset 1: precios de electricidad
electricity_dataset=pd.read_csv('data/Electricity_prices_eu.csv')

# Cambiamos el nombre de la columna de OBS_VALUE para diferenciarla de cada dataset 
# Esto es debido a que representan valores distintos aunque compartan el mismo nombre
electricity_dataset.rename(columns={'OBS_VALUE': 'electricity_price_eur/kWh'}, inplace=True)
electricity_dataset
"""
st.code(code, language="python")





code = """ 
# Dataset 2: precios del gas
gas_dataset=pd.read_csv('data/Gas_prices_eu.csv', sep=';')

# cambiamos el nombre de la columna de OBS_VALUE para diferenciarla para cada dataset
gas_dataset.rename(columns={'OBS_VALUE': 'gas_price_eur/GJ'}, inplace=True)
gas_dataset
"""
st.code(code, language="python")


code = """ 
# Dataset 3: balance energético
balance_dataset=pd.read_csv('data/Energy_balance_eu.csv', sep=';')

# cambiamos el nombre de la columna de OBS_VALUE para diferenciarla para cada dataset
balance_dataset.rename(columns={'OBS_VALUE': 'energy_GWh'}, inplace=True)
balance_dataset
"""
st.code(code, language="python")




############################## 2. Tranformación de nuestra DATA

st.markdown("""## 2. Tranformación de nuestra DATA

Como en muchos casos de un proyecto de analitica de datos, los datos iniciales vienen con formatos distintos, por los que será necesario una transformación de los datos para que estos tengan el mismo formato y nos sean de utilidad.

**Tarea:** Para unir los 3 datasets en uno único (energy_dataset) tenemos que igualar el numero de columnas y completar los datos con Nulos
""")





code = """ 
# Filtramos las columnas de interés para cada dataset
electricity_dataset=electricity_dataset[['TIME_PERIOD','geo','product','indic_en', 'electricity_price_eur/kWh']]
gas_dataset=gas_dataset[['TIME_PERIOD','geo','product','indic_en','gas_price_eur/GJ']]
balance_dataset=balance_dataset[['TIME_PERIOD','geo','nrg_bal','siec','energy_GWh']]

# Creamos columnas extras con valores nulos para cada dataset, para que los 3 dataset contengan las mismas columnas
electricity_dataset['nrg_bal']=None
electricity_dataset['siec']=None
electricity_dataset['gas_price_eur/GJ']=None
electricity_dataset['energy_GWh']=None

gas_dataset['nrg_bal']=None
gas_dataset['siec']=None
gas_dataset['electricity_price_eur/kWh']=None
gas_dataset['energy_GWh']=None

balance_dataset['product']='Energy balance'
balance_dataset['indic_en']=None
balance_dataset['electricity_price_eur/kWh']=None
balance_dataset['gas_price_eur/GJ']=None

# Reordenamos columnas para que todos los df tengan el mismo formato
electricity_dataset=electricity_dataset[
    ['TIME_PERIOD',
     'geo',
     'product',
     'nrg_bal',
     'siec',
     'indic_en',
     'energy_GWh', 
     'electricity_price_eur/kWh', 
     'gas_price_eur/GJ']
]
gas_dataset=gas_dataset[
    ['TIME_PERIOD',
     'geo',
     'product',
     'nrg_bal',
     'siec',
     'indic_en',
     'energy_GWh', 
     'electricity_price_eur/kWh', 
     'gas_price_eur/GJ']
]
balance_dataset=balance_dataset[
    ['TIME_PERIOD',
     'geo',
     'product',
     'nrg_bal',
     'siec',
     'indic_en',
     'energy_GWh', 
     'electricity_price_eur/kWh', 
     'gas_price_eur/GJ']
]

# Unimos los 3 dataset en un solo energy_dataset concatenando los valores (se suma el numero de filas)
energy_dataset = pd.concat([electricity_dataset, gas_dataset, balance_dataset], ignore_index=True)

# Eliminamos los datos de total Europeo del dataset ya que no son de interés en este caso
energy_dataset = energy_dataset[energy_dataset['geo'] != 'EU27_2020']

# Comprobamos que se ha concatenado correctamente
energy_dataset
"""
st.code(code, language="python")


# Renombramos los encabezados para que la intepretación de las columnas por la IA sea mas sencilla

code = """ energy_dataset.rename(columns={
    'TIME_PERIOD': 'time_period',
    'geo': 'country', 
    'product': 'data_type',
    'nrg_bal': 'energy_category', 
    'siec': 'energy_product_class', 
    'indic_en': 'costumer'}, inplace=True)

energy_dataset
"""
st.code(code, language="python")



## POR AQUÍ VAMOS.
## FALTARIAN LAS IMAGENES







st.markdown("""## 3. Carga de la DATA

En esta etapa, guardaremos el dataset final en un fichero .csv dentro del mismo directorio que será cargado en la BBDD para la posterior interacción con la aplicación de IA.
""")





