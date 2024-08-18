import streamlit as st

# st.write("Hello World")

st.sidebar.success("Select a page above.")



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

