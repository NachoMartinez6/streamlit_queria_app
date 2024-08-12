
import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import os





################################################### FRONTEND ###################################################


# CSS para la imagen de fondo
page_bg_img = '''
<style>
body {{
    background-image: url("https://images.pexels.com/photos/33493/windrader-wind-power-fichtelberg-wind-park.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
    background-size: cover;
    background-attachment: fixed;
}}
</style>
'''

# Aplicar el CSS para la imagen de fondo
st.markdown(page_bg_img, unsafe_allow_html=True)

# Creamos el sidebar para esta pestaña
st.sidebar.success("Select a page above.")

# Título de la aplicación
# st.title('Data Analysis: Situación del mercado energético UE')
st.markdown(f'<h1>Data Analysis: <span style="color:dodgerblue">Situación del mercado energético UE</span>', unsafe_allow_html=True)
# st.markdown(f'<h1><span style="color:dodgerblue">Data Analysis:</span> Situación del mercado energético UE', unsafe_allow_html=True)

# st.markdown(f'<h1>Bienvenido a Quer<span style="color:dodgerblue">IA</span>!', unsafe_allow_html=True)


# # Cargar los datos desde el archivo CSV
# file_path = 'data/energy_dataset.csv'
# try:
#     energy_dataset = pd.read_csv(file_path, sep=';', on_bad_lines='skip')
#     st.write("Archivo cargado correctamente")
# except pd.errors.ParserError as e:
#     st.write("Error al cargar el archivo CSV:", e)



# st.markdown('### Dashboard: Situación del mercado energético en España, Portugal, Italia, Francia y Alemania')

# Introducción y texto inicial
st.write("""Este proyecto analiza las tendencias del mercado energético en Europa.

En este sentido, se centrará en la producción, consumo, importación y exportación de energía en países clave como España, Francia, Italia, Portugal y Alemania.

A través de una serie de gráficas, se examinan los cambios en el mix energético, destacando la transición hacia fuentes renovables y los esfuerzos por mejorar la seguridad energética.

El estudio resalta cómo estos países están adaptando sus estrategias energéticas para cumplir con los objetivos de sostenibilidad, mostrando tanto los avances logrados como los desafíos restantes en el camino hacia un sistema energético más limpio y eficiente.""")

# Ruta a la carpeta de imágenes
image_folder = 'QuerIA Graphics'

# Mostrar cada imagen con su descripción y espacio para texto entre las gráficas
st.markdown("## Análisis del Mercado Energético Europeo")
st.image(f"{image_folder}/G1_energy_prices.png", use_column_width=True)
st.markdown("""
En los últimos años, el mercado energético europeo ha experimentado significativas transformaciones, influenciado por la transición hacia energías renovables y una serie de factores económicos y geopolíticos. A través del análisis detallado, podemos observar cómo estos elementos han impactado en los precios de la electricidad y el gas, tanto para consumidores residenciales como no residenciales.

- **Gráfica 1: Precio de Electricidad en el Sector Residencial**

    Desde 2011, los precios de la electricidad para el sector residencial han mostrado una tendencia ascendente. Este aumento refleja principalmente las inversiones sustanciales en infraestructura para energías renovables y los costos asociados a la integración de estas fuentes en las redes eléctricas existentes. Aunque estas inversiones han elevado los costos inicialmente, actualmente han contribuido a la reducción de precios a medida que las tecnologías se amortizan y se optimiza la eficiencia del sistema. En el contexto actual, tras los picos observados durante la crisis energética de 2022, los precios se han estabilizado gracias a una mayor generación de energías renovables y a mejoras en eficiencia energética.

- **Gráfica 2: Precio de Electricidad en el Sector No Residencial**

    El sector no residencial ha experimentado una variabilidad en los precios de la electricidad debido a su sensibilidad frente a políticas económicas y ambientales.
    La implementación de impuestos al carbono y otras regulaciones medioambientales ha influido en estos costos.
    Sin embargo, a medida que las energías renovables ganan terreno en el mix energético, se espera que los precios se estabilicen, facilitando una transición más uniforme para los consumidores comerciales.

- **Gráfica 3: Precio de Gas en el Sector Residencial**

    Los precios del gas para los consumidores residenciales han sido volátiles, reflejando la dependencia de importaciones y las fluctuaciones en los mercados globales.
    Las tensiones geopolíticas, particularmente en torno al suministro desde Rusia, han exacerbado esta volatilidad.
    Sin embargo, las estrategias de diversificación de la Unión Europea están comenzando a aliviar algunas de estas presiones.
    A futuro, se espera que la demanda de gas disminuya a medida que se acelera la adopción de energías renovables, lo que podría estabilizar, aún más, los precios.

- **Gráfica 4: Precio de Gas en el Sector No Residencial**

    El mercado de gas no residencial ha sido particularmente sensible a las fluctuaciones globales y a los contratos específicos del sector industrial.
    La liberalización del mercado europeo de gas ha facilitado la competencia, ayudando a mitigar algunos aumentos de precios recientes.
    Con la adaptación a nuevas fuentes y tecnologías, se anticipa una mejora en la estabilidad de los precios, beneficiando a los consumidores no residenciales a largo plazo.

### Conclusión General

En conclusión, el mercado energético europeo está en una fase de transición hacia un sistema más sostenible, influenciado por la interacción de diversos factores económicos, políticos y tecnológicos.
A pesar de los desafíos iniciales y la volatilidad del mercado, las inversiones en energías renovables y las políticas de eficiencia energética están comenzando a estabilizar los precios.
Esto sienta las bases para un futuro energético más sostenible y económico, en línea con los objetivos climáticos de la Unión Europea.

""")



st.write("## Análisis del Balance Energético por Categoría y País para 2022")
st.image(f"{image_folder}/G2_energy_category.png", use_column_width=True)
st.write("""
La gráfica de barras agrupadas ilustra el balance energético de diferentes categorías clave - Exportaciones, Consumo Interior Bruto, Importaciones, Suministro Total de Energía y Producción Primaria - en varios países europeos durante el año 2022. Esta representación permite visualizar cómo los países gestionan su suministro y demanda energética, así como la interdependencia en el mercado energético europeo.

- **Exportaciones e Importaciones:**

    Las exportaciones y las importaciones de energía varían significativamente entre los países, reflejando su capacidad para generar energía excedente y su dependencia de las importaciones.
    Alemania, por ejemplo, muestra altos niveles de exportación debido a su capacidad de producción, especialmente en energías renovables y combustibles fósiles.
    Por otra parte, países como España e Italia presentan una alta dependencia de las importaciones para satisfacer su demanda energética.

- **Consumo Interior Bruto y Suministro Total de Energía:**

    El Consumo Interior Bruto (Gross Inland Consumption) representa la cantidad de energía consumida dentro de un país, excluyendo el comercio internacional.
    Alemania y Francia, como grandes economías, tienen un consumo interior significativo, impulsado por su industria y población.
    El Suministro Total de Energía refleja la suma de la producción primaria y las importaciones, menos las exportaciones, subrayando la capacidad de cada país para satisfacer su demanda interna.
    Francia, por ejemplo, muestra un suministro energético considerable, gracias a su capacidad de generación nuclear.

- **Producción Primaria:**

    La Producción Primaria destaca la capacidad de un país para generar energía a partir de sus recursos naturales.
    Francia, con su sólida infraestructura nuclear, y Alemania, con su expansión de energías renovables, lideran en este aspecto.
    La diversificación de fuentes de energía primaria es clave para la seguridad energética y la estabilidad de precios, especialmente en contextos de volatilidad del mercado global.

### Conclusiones

En conclusión, la gráfica refleja cómo los países europeos equilibran sus necesidades energéticas a través de una combinación de producción interna y comercio internacional.
Las estrategias de diversificación y la transición hacia fuentes renovables están cambiando el panorama energético, buscando reducir la dependencia de importaciones y mejorar la sostenibilidad a largo plazo.
La capacidad de gestionar eficientemente el balance energético es crucial para cumplir con los objetivos climáticos de la Unión Europea y garantizar la seguridad energética en un entorno geopolítico incierto.
""")

st.write("## Análisis de la Importación Energética por Clases de Interés en 2022")
st.image(f"{image_folder}/G3_energy_imports.png", use_column_width=True)
st.write("""
La siguiente serie, muestra la composición de las importaciones energéticas de cinco países europeos clave (Francia, España, Italia, Portugal y Alemania) para el año 2022. Estos gráficos ilustran la diversidad en las fuentes de energía importada, destacando cómo cada país maneja su dependencia energética en el contexto europeo.

- **Francia:**

    El gráfico de Francia muestra una mezcla diversa de importaciones energéticas, donde el gas natural y el petróleo ocupan un papel predominante.
    La dependencia de estos combustibles fósiles refleja la necesidad de abastecer su infraestructura energética, que aunque se centra en la generación nuclear, aún requiere apoyo de estas fuentes externas para equilibrar su mix energético.

- **España:**

    En España, las importaciones están dominadas por el gas natural, seguido de cerca por el petróleo.
    Este patrón subraya la dependencia de España en el gas para satisfacer su demanda energética, especialmente para la generación de electricidad y calefacción.
    La transición hacia energías renovables está en marcha y va ganando terreno a las energías fósiles, aunque todavía existe una dependencia de las importaciones fósiles.

- **Italia:**

    Italia también muestra una fuerte dependencia del gas natural, reflejando su uso extendido en el sector residencial e industrial.
    Las importaciones de petróleo son también altas, debido a la falta de recursos energéticos propios y la necesidad de satisfacer una demanda energética diversa.

- **Portugal:**

    El gráfico de Portugal destaca una dependencia notable del gas natural y el petróleo, con una menor diversidad en su mezcla de importaciones comparado con otros países.
    La transición hacia energías renovables en Portugal ha sido rápida, pero el país sigue siendo dependiente de combustibles fósiles importados para estabilizar su suministro energético.

- **Alemania:**

    Alemania presenta una composición diversa de importaciones, con el gas natural y el petróleo nuevamente liderando.
    Sin embargo, Alemania ha avanzado en la integración de energías renovables, reduciendo gradualmente su dependencia de fuentes importadas, aunque todavía juega un papel importante para la seguridad energética.

### Conclusiones

En conclusión, podemos ver cómo la dependencia de importaciones energéticas varía entre países europeos, influenciada por factores como la disponibilidad de recursos internos, la infraestructura energética existente y las políticas de transición hacia energías limpias.
A medida que Europa avanza hacia sus objetivos climáticos, la diversificación de las fuentes de energía y la reducción de la dependencia de importaciones fósiles se vuelven esenciales para asegurar la sostenibilidad energética a largo plazo.

""")


st.write("## Análisis de la Producción Energética por Clases de Interés en 2022")
st.image(f"{image_folder}/G4_energy_producction.png", use_column_width=True)
st.write("""
En esta serie, podemos apreciar la composición de la producción energética de nuestra muestra de países clave para el año 2022.
Estos gráficos destacan las fuentes de energía primaria que cada país utiliza para satisfacer sus necesidades energéticas internas, reflejando sus estrategias en el contexto del mercado energético europeo.

- **Francia:**

    Francia muestra una alta dependencia de la energía nuclear, que constituye una gran parte de su producción energética primaria.
    Esto subraya la posición de Francia como uno de los líderes mundiales en generación nuclear, lo cual le proporciona una fuente estable y relativamente baja en emisiones de carbono para su consumo energético.

- **España:**

    En España, la producción de energía está diversificada, con una notable contribución de las energías renovables como la eólica y la hidráulica.
    Esta diversificación refleja los esfuerzos del país por reducir la dependencia de combustibles fósiles y avanzar hacia un mix energético más sostenible.

- **Italia:**

    Italia tiene una producción energética primaria que se basa en una combinación de gas natural y renovables.
    A pesar de la dependencia de importaciones para satisfacer su demanda total, el país está incrementando la producción de energías renovables para reducir su huella de carbono y mejorar la seguridad energética.

- **Portugal:**

    Portugal destaca por su elevada producción de energías renovables, especialmente eólica e hidráulica.
    Esta estrategia ha permitido a Portugal ser uno de los países con mayor proporción de renovables en su mix energético, reduciendo la dependencia de fuentes fósiles y alineándose con los objetivos climáticos de la UE.

- **Alemania:**

    Alemania presenta una producción energética primaria diversa, con un enfoque significativo en las energías renovables como la eólica y la biomasa.
    Aunque el país todavía utiliza carbón y gas, el compromiso de Alemania de eliminar gradualmente las fuentes fósiles y aumentar la capacidad renovable es evidente en su mix energético actual.

### Conclusiones

En conclusión, los datos analizados revelan cómo los países europeos han estructurado sus estrategias de producción energética para abordar sus necesidades internas y objetivos climáticos. La transición hacia fuentes renovables es una tendencia común, impulsada por la necesidad de reducir emisiones y mejorar la sostenibilidad energética.
A medida que Europa avanza hacia un futuro más verde, la producción de energía limpia seguirá siendo una prioridad clave para asegurar un suministro estable y reducir la dependencia de combustibles fósiles.
""")


st.write("## Análisis de la Evolución de la Producción Solar Fotovoltaica por País")
st.image(f"{image_folder}/G5_solar_production.png", use_column_width=True)
st.write("""
Analizando en detalle la evolución de la producción de energía solar fotovoltaica en diferentes países europeos a lo largo del tiempo, podemos observar los avances en la adopción de energías renovables, especialmente la solar, como una parte crucial del mix energético en Europa.

- **Francia:**

    Francia ha experimentado un crecimiento constante en su capacidad de producción solar, aunque sigue dependiendo en gran medida de la energía nuclear.
    Sin embargo, la integración de la solar está en aumento, impulsada por políticas que fomentan las inversiones en energías limpias.

- **España:**

    España es uno de los líderes en la adopción de energía solar en Europa.
    El país ha visto un rápido crecimiento en la capacidad solar instalada, gracias a sus condiciones climáticas favorables y al apoyo gubernamental en forma de subsidios y regulaciones que facilitan la expansión de la infraestructura solar.

- **Italia:**

    Italia ha mostrado un notable crecimiento en la producción de energía solar, impulsado por políticas nacionales que promueven las energías renovables.
    La energía solar fotovoltaica se ha convertido en un componente importante del mix energético del país, ayudando a reducir la dependencia de combustibles fósiles importados.

- **Portugal:**

    Portugal ha incrementado significativamente su producción de energía solar en los últimos años.
    La expansión de esta capacidad refleja el compromiso del país con las energías renovables, complementando su ya considerable capacidad en energía eólica e hidráulica.

- **Alemania:**

    Alemania es uno de los pioneros en la adopción de energía solar en Europa.
    El país ha mantenido un crecimiento constante en su capacidad de producción solar, apoyado por una fuerte infraestructura y políticas gubernamentales que incentivan la transición hacia un mix energético más verde.

### Conclusiones

En conclusión, la producción de energía solar fotovoltaica en Europa ha mostrado un crecimiento notable, subrayando la importancia de esta fuente de energía renovable en la transición energética del continente.
A medida que los países europeos continúan invirtiendo en tecnologías solares, se espera que la energía solar juegue un papel cada vez más crucial en la reducción de emisiones de gases de efecto invernadero y en la mejora de la seguridad energética.

""")




st.write("## Análisis de la Evolución Energética en España a lo Largo del Tiempo")
st.image(f"{image_folder}/G6_spain_energy_balance.png", use_column_width=True)
st.write("""
En esta serie podemos observar una visión completa de la evolución de la producción, consumo, importación y exportación de energía en España.
Estos gráficos proporcionan un entendimiento detallado de cómo ha cambiado el balance energético del país en respuesta a los desarrollos tecnológicos, políticos y económicos.

- **Producción Energética:**

    España ha incrementado significativamente su producción de energía renovable, especialmente en el sector solar y eólico.
    Este aumento refleja los esfuerzos del país para diversificar su mix energético y reducir la dependencia de combustibles fósiles, alineándose con los objetivos de sostenibilidad de la Unión Europea.
    La inversión en infraestructura renovable ha sido clave para este crecimiento, permitiendo una mayor independencia energética.

- **Consumo Interior Bruto de Energía:**

    El consumo energético en España ha mostrado variaciones a lo largo de los años, influenciado por factores económicos y demográficos.
    El crecimiento en el uso de energías renovables ha ayudado a estabilizar el consumo energético, reduciendo las emisiones de carbono y mejorando la eficiencia energética en sectores clave como la industria y el transporte.

- **Importación Energética:**

    España ha sido históricamente un importador neto de energía, especialmente gas natural y petróleo.
    Sin embargo, la transición hacia fuentes renovables ha comenzado a reducir esta dependencia, aunque las importaciones siguen siendo necesarias para satisfacer la demanda energética en períodos de alta demanda o baja producción renovable.

- **Exportación Energética:**

    El crecimiento de la capacidad de producción renovable ha permitido a España aumentar sus exportaciones de energía, particularmente hacia países vecinos.
    Esto no solo ha mejorado la seguridad energética del país, sino que también ha contribuido a equilibrar el mercado energético regional, fortaleciendo la posición de España como proveedor energético en el sur de Europa.

### Conclusiones

En conclusión, España ha realizado avances significativos en la transición hacia un sistema energético más sostenible y diversificado.
La apuesta por las energías renovables ha permitido reducir la dependencia de las importaciones y mejorar la seguridad energética, mientras que el incremento en las exportaciones refuerza la economía y la posición estratégica del país en el mercado energético europeo.
La continuidad de estas tendencias será crucial para alcanzar los objetivos climáticos y asegurar un futuro energético sostenible.

""")






# Fuentes Citadas
st.write("## Fuentes Citadas")
st.write("""
- [European Electricity Review 2024 | Ember](https://ember-climate.org/commentary/2024/08/european-electricity-review-2024/)
- [Electricity 2024: Analysis and forecast to 2026 - European Commission](https://managenergy.ec.europa.eu/electricity-2024-analysis-and-forecast-2026_en)
- [Energy Prices 2024: Forecast & Market Trends | Diversegy](https://diversegy.com/blog/energy-market-price-forecasts-trends-predictions-for-2024/)
""")






