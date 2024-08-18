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




