
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


################################################### BACKEND - DATA ANALYSIS ###################################################

# Load our data
energy_dataset = pd.read_csv("data/energy_dataset.csv", sep=";")


################################ 1º Grafica
# Definimos una función para crear gráficos y llamarlos, para que estos tengan el mismo estilo
def plot_line_graphycs(data, axix_x, axix_y, hue_value, x_label, y_label, title, ax):
    sns.set_palette('pastel')
    sns.set_style('whitegrid')
    sns.lineplot(data=data, x=axix_x, y=axix_y, hue=hue_value, marker=".", ax=ax)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(title, fontsize=15, weight='bold', pad= 20)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.legend(bbox_to_anchor=(0.3, -0.1), loc='upper center', ncol=len(data[hue_value].unique()), borderaxespad=0., prop={'size': 6}, markerscale=1)

    # Ocultamos el marco y leyenda local de cada gráfico (se estorbaba por tamaño)
    ax.legend().remove()
    for spine in ax.spines.values():
        spine.set_visible(False)

# Creamos una figura con 4 subplots (graficos) y damos mas espacio entre ellos 
fig, axs = plt.subplots(2, 2, figsize=(14, 8))
fig.subplots_adjust(hspace=0.5, wspace=0.9)


# Primer gráfico: precio de electricidad para sector residencial
EPH = energy_dataset[
    (energy_dataset['data_type'] == 'Electricity price') &
    (energy_dataset['costumer'] == 'Medium size households')
]
plot_line_graphycs(
    EPH,
    'time_period',
    'electricity_price_eur/kWh',
    'country',
    '',
    '€/kWh',
    'Precio electricidad: Sector residencial',
    axs[0, 0]
)

# Segundo gráfico: precio de electricidad para sector no residencial
EPNH = energy_dataset[
    (energy_dataset['data_type'] == 'Electricity price') &
    (energy_dataset['costumer'] == 'Non-household, medium size consumers')
]
plot_line_graphycs(
    EPNH,
    'time_period',
    'electricity_price_eur/kWh',
    'country',
    '',
    '€/kWh',
    'Precio electricidad: Sector no residencial',
    axs[0, 1]
)

# Tercer gráfico: Precio de gas para sector residencial
GPH = energy_dataset[
    (energy_dataset['data_type'] == 'Gas price') &
    (energy_dataset['costumer'] == 'Medium size households')
]
plot_line_graphycs(
    GPH,
    'time_period',
    'gas_price_eur/GJ',
    'country',
    '',
    '€/GJ',
    'Precio gas: Sector residencial',
    axs[1, 0]
)

# Cuarto gráfico: Precio de gas para sector no residencial
GPNH = energy_dataset[
    (energy_dataset['data_type'] == 'Gas price') &
    (energy_dataset['costumer'] == 'Non-household, medium size consumers')
]
plot_line_graphycs(
    GPNH,
    'time_period',
    'gas_price_eur/GJ',
    'country',
    '',
    '€/GJ',
    'Precio gas: Sector no residencial',
    axs[1, 1]
)

# Ajustamos el diseño
plt.tight_layout()

# Obtenemos la leyenda del primer gráfico para mostrarla de forma genérica debajo de las gráficas
handles, labels = axs[0, 0].get_legend_handles_labels() # extraemos la leyeenda del primer gráfico
fig.legend(handles, labels, loc='lower center', ncol=4, bbox_to_anchor=(0.23, -0.1), fontsize=10)

# guardamos la imagen generada
os.makedirs('QuerIA Graphics', exist_ok=True)
plt.savefig('QuerIA Graphics/G1_energy_prices.png', dpi=300, bbox_inches='tight')

# plt.show()



################################ 2º Grafica
# Representamos las categorías de energía agrupados por pais para el año 2022


# Filtramos los datos para incluir solo aquellos con "Energy balance" en la columna data_type y año 2022


# Definimos la función para crear gráficos de barras agrupados
def plot_groupbar_graphics(data, axix_x, axix_y, hue_value, x_label, y_label, title, ax):
    sns.set_palette('pastel')
    sns.set_style('whitegrid')
    sns.barplot(data=data, x=axix_x, y=axix_y, hue=hue_value, ax=ax,errorbar=None)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(title, fontsize=15, weight='bold', pad= 20)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(bbox_to_anchor=(0.45, -0.1), loc='upper center', ncol=len(data[hue_value].unique()), borderaxespad=0., prop={'size': 12})

    # Ocultamos el marco
    for spine in ax.spines.values():
        spine.set_visible(False)

# Creamos una figura con un subplot
fig, ax = plt.subplots(figsize=(12, 5))

# Filtramos los datos que nos interesa mostrar
energy_balance_data = energy_dataset[
    (energy_dataset['data_type'] == 'Energy balance') & 
    (energy_dataset['time_period'] == 2022)  # Asegúrate de que el año esté en el formato correcto
]

# Filtramos las categorías que nos interesan Exportacion, Importación, Consumo, etc...
categories = [
    'Exports', 'Gross inland consumption',
    'Imports', 'Total energy supply', 'Primary production'
]
filtered_data = energy_balance_data[energy_balance_data['energy_category'].isin(categories)]

plot_groupbar_graphics(
    filtered_data,
    'country',
    'energy_GWh',
    'energy_category',
    '',
    'GWh',
    'Balance energético por categoría y país para 2022',
    ax
)

plt.tight_layout()

# guardamos la imagen generada
os.makedirs('QuerIA Graphics', exist_ok=True)
plt.savefig('QuerIA Graphics/G2_energy_category.png', dpi=300, bbox_inches='tight')

# plt.show()


################################ 3º Grafica
# Representamos las clases energéticas de interés que ha importado cada pais en el año 2022

# Definimos la función para crear gráficos circulares
def plot_imports_graphics(data, title, ax):
    sns.set_palette('pastel')
    sns.set_style('whitegrid')
    
    # Agrupamos y sumamos por clase de producto energético, excluyendo el Total y la fotovoltaica
    class_sums = data.groupby('energy_product_class')['energy_GWh'].sum()
    class_sums = class_sums[(class_sums.index != 'Total')&(class_sums.index != 'Solar photovoltaic')]
    
    # Creamos gráfico circular con etiquetas de datos dentro de los sectores
    wedges, texts, autotexts = ax.pie(
        class_sums, startangle=90, autopct='%1.1f%%')
    ax.set_title(title, fontsize=15, weight='bold')
    
    # Aseguramos que el gráfico es un círculo
    ax.axis('equal')
    
    # Personalizamos las etiquetas de los datos dentro de los sectores
    for autotext in autotexts:
        autotext.set_color('dimgray')  
        autotext.set_fontsize(14)      
    for spine in ax.spines.values():
        spine.set_visible(False)
    return wedges, class_sums.index

# Filtramos los datos para el año 2022, la categoría de importe de energía, y los países de interés
primary_production_data = energy_dataset[
    (energy_dataset['data_type'] == 'Energy balance') &
    (energy_dataset['time_period'] == 2022) &
    (energy_dataset['energy_category'] == 'Imports') &
    (energy_dataset['country'].isin(['France', 'Spain', 'Italy', 'Portugal', 'Germany']))
]

# Creamos una figura con 5 subplots (uno para cada país)
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Importación energécica por clases de interés durante el año 2022', fontsize=22, weight='bold')

# Creamos un gráfico circular para cada país y capturamos los wedges para la leyenda
wedges, labels = plot_imports_graphics(primary_production_data[primary_production_data['country'] == 'France'], 'France', axs[0, 0])
plot_imports_graphics(primary_production_data[primary_production_data['country'] == 'Spain'], 'Spain', axs[0, 1])
plot_imports_graphics(primary_production_data[primary_production_data['country'] == 'Italy'], 'Italy', axs[0, 2])
plot_imports_graphics(primary_production_data[primary_production_data['country'] == 'Portugal'], 'Portugal', axs[1, 0])
plot_imports_graphics(primary_production_data[primary_production_data['country'] == 'Germany'], 'Germany', axs[1, 1])

# Añadirmos una leyenda en el espacio vacío
axs[1, 2].axis('off')
axs[1, 2].legend(wedges, labels, loc='center', fontsize=14)

plt.tight_layout()
plt.subplots_adjust(top=0.9)

# guardamos la imagen generada
os.makedirs('QuerIA Graphics', exist_ok=True)
plt.savefig('QuerIA Graphics/G3_energy_imports.png', dpi=300, bbox_inches='tight')

# plt.show()


################################ 4º Grafica
# Representamos las clases energéticas de interés que ha producido cada pais en el año 2022

# Definimos la función para crear gráficos circulares
def plot_production_graphics(data, title, ax):
    sns.set_palette('pastel')
    sns.set_style('whitegrid')
    
    # Agrupamos y sumamos por clase de producto energético, excluyendo el Total y la fotovoltaica
    class_sums = data.groupby('energy_product_class')['energy_GWh'].sum()
    class_sums = class_sums[(class_sums.index != 'Total')&(class_sums.index != 'Solar photovoltaic')]
    
    # Creamos gráfico circular con etiquetas de datos dentro de los sectores
    wedges, texts, autotexts = ax.pie(
        class_sums, startangle=90, autopct='%1.1f%%')
    ax.set_title(title, fontsize=15, weight='bold')
    
    # Aseguramos que el gráfico es un círculo
    ax.axis('equal')
    
    # Personalizamos las etiquetas de los datos dentro de los sectores
    for autotext in autotexts:
        autotext.set_color('dimgray')  
        autotext.set_fontsize(14)      
    for spine in ax.spines.values():
        spine.set_visible(False)
    return wedges, class_sums.index

# Filtramos los datos para el año 2022, la categoría de importe de energía, y los países de interés
primary_production_data = energy_dataset[
    (energy_dataset['data_type'] == 'Energy balance') &
    (energy_dataset['time_period'] == 2022) &
    (energy_dataset['energy_category'] == 'Primary production') &
    (energy_dataset['country'].isin(['France', 'Spain', 'Italy', 'Portugal', 'Germany']))
]

# Creamos una figura con 5 subplots (uno para cada país)
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Producción energética por clases de interés durante el año 2022', fontsize=22, weight='bold')

# Creamos un gráfico circular para cada país y capturamos los wedges para la leyenda
wedges, labels = plot_production_graphics(primary_production_data[primary_production_data['country'] == 'France'], 'France', axs[0, 0])
plot_production_graphics(primary_production_data[primary_production_data['country'] == 'Spain'], 'Spain', axs[0, 1])
plot_production_graphics(primary_production_data[primary_production_data['country'] == 'Italy'], 'Italy', axs[0, 2])
plot_production_graphics(primary_production_data[primary_production_data['country'] == 'Portugal'], 'Portugal', axs[1, 0])
plot_production_graphics(primary_production_data[primary_production_data['country'] == 'Germany'], 'Germany', axs[1, 1])

# Añadirmos una leyenda en el espacio vacío
axs[1, 2].axis('off')
axs[1, 2].legend(wedges, labels, loc='center', fontsize=14)

plt.tight_layout()
plt.subplots_adjust(top=0.9)

# guardamos la imagen generada
os.makedirs('QuerIA Graphics', exist_ok=True)
plt.savefig('QuerIA Graphics/G4_energy_producction.png', dpi=300, bbox_inches='tight')

# plt.show()


################################ 5º Grafica
# Grafico de evolución de producción de energía solar fotovoltaica en todos los paises a lo largo del tiempo

# Definimos una función para crear gráficos y llamarlos, para que estos tengan el mismo estilo
def plot_1line_graphycs(data, axix_x, axix_y, hue_value, x_label, y_label, title):
    sns.set_palette('pastel')
    sns.set_style('whitegrid')
    sns.lineplot(data=data, x=axix_x, y=axix_y, hue=hue_value, marker="o")
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.title(title, fontsize=15, weight='bold', pad=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(bbox_to_anchor=(0.285, -0.1), loc='upper center', ncol=len(data[hue_value].unique()), borderaxespad=0., prop={'size': 12})

    # Ocultamos el marco
    sns.despine()

# Filtramos los datos para la producción solar fotovoltaica
solar_prod = energy_dataset[
    (energy_dataset['energy_category'] == 'Primary production') &
    (energy_dataset['energy_product_class'] == 'Solar photovoltaic')
]

# Creamos una figura para el gráfico
plt.figure(figsize=(12, 6))

# Llamamos a la función para crear el gráfico
plot_1line_graphycs(
    solar_prod,
    'time_period',   
    'energy_GWh',  
    'country',   
    '', 
    'GWh', 
    'Evolución de la producción solar fotovoltaica por país'
)

plt.tight_layout()

# guardamos la imagen generada
os.makedirs('QuerIA Graphics', exist_ok=True)
plt.savefig('QuerIA Graphics/G5_solar_production.png', dpi=300, bbox_inches='tight')

# plt.show()



################################ 6º Grafica
# Evolución de la producción, consumo, exportación e importación energética en España a lo largo del tiempo

# Definimos una función para crear gráficos y llamarlos, para que estos tengan el mismo estilo
def plot_line_graphycs_prod(data, axix_x, axix_y, hue_value, x_label, y_label, title, ax):
    sns.set_palette('pastel')
    sns.set_style('whitegrid')
    sns.lineplot(data=data, x=axix_x, y=axix_y, hue=hue_value, marker=".", ax=ax)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(title, fontsize=15, weight='bold', pad= 20)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', ncol=1, borderaxespad=0., prop={'size': 8}, markerscale=1)

    # Ocultamos el marco y leyenda local de cada gráfico (se estorbaba por tamaño)
    ax.legend().remove()
    for spine in ax.spines.values():
        spine.set_visible(False)

# Creamos una figura con 4 subplots (graficos)
fig, axs = plt.subplots(2, 2, figsize=(14, 8))

# Primer gráfico: 
Prod_Spain = energy_dataset[
    (energy_dataset['data_type'] == 'Energy balance') &
    (energy_dataset['energy_category']=='Primary production')&
    (energy_dataset['country']=='Spain')]

plot_line_graphycs_prod(
    Prod_Spain,
    'time_period',
    'energy_GWh',
    'energy_product_class',
    '',
    'GWh',
    'España: Histórico de producción energética',
    axs[0, 0]
)

# Segundo gráfico: 
Consum_Spain = energy_dataset[
    (energy_dataset['data_type'] == 'Energy balance') &
    (energy_dataset['energy_category']=='Gross inland consumption')&
    (energy_dataset['country']=='Spain')]

plot_line_graphycs_prod(
    Consum_Spain,
    'time_period',
    'energy_GWh',
    'energy_product_class',
    '',
    'GWh',
    'España: Histórico de consumo interior bruto de energía',
    axs[0, 1]
)


# Tercer gráfico: 
Import_Spain = energy_dataset[
    (energy_dataset['data_type'] == 'Energy balance') &
    (energy_dataset['energy_category']=='Imports')&
    (energy_dataset['country']=='Spain')]

plot_line_graphycs_prod(
    Import_Spain,
    'time_period',
    'energy_GWh',
    'energy_product_class',
    '',
    'GWh',
    'España: Histórico de importación energética',
    axs[1, 0]
)

# Cuarto gráfico: 
Export_Spain = energy_dataset[
    (energy_dataset['data_type'] == 'Energy balance') &
    (energy_dataset['energy_category']=='Exports')&
    (energy_dataset['country']=='Spain')]

plot_line_graphycs_prod(
    Export_Spain,
    'time_period',
    'energy_GWh',
    'energy_product_class',
    '',
    'GWh',
    'España: Histórico de exportación energética',
    axs[1, 1]
)

# Ajustamos el diseño y mostramos la leyenda global para todos los gráficos
plt.tight_layout()

handles, labels = axs[0, 0].get_legend_handles_labels() # extraemos la leyeenda del primer gráfico
fig.legend(handles, labels, loc='lower center', ncol=4, bbox_to_anchor=(0.38, -0.1), fontsize=10)
plt.tight_layout()

# guardamos la imagen generada
os.makedirs('QuerIA Graphics', exist_ok=True)
plt.savefig('QuerIA Graphics/G6_spain_energy_balance.png', dpi=300, bbox_inches='tight')

# plt.show()
