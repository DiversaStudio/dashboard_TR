import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

# Definir los colores
colors = {
    "sidebar_bg": "#152F54",  # Color para la barra lateral
    "content_bg": "#FFFFFF",
    "text_color": "#000000",  # Color negro para el texto
    "sidebar_text_color": "#FFFFFF",  # Color blanco para el texto de la barra lateral
    "button_bg": "#688D98",  # Color para los botones
    "button_hover_bg": "#327378"  # Color de los botones al pasar el ratón
}

# Aplicar colores personalizados a la interfaz
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {colors["content_bg"]};
        color: {colors["text_color"]};
        font-family: 'Arial', sans-serif;
    }}
    .css-1d391kg {{
        background-color: {colors["sidebar_bg"]};
        color: {colors["sidebar_text_color"]};
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }}
    .css-1lcbmhc.e1fqkh3o3 {{
        background-color: {colors["sidebar_bg"]};
        color: {colors["sidebar_text_color"]};
    }}
    .css-1e5imcs {{
        background-color: {colors["sidebar_bg"]};
        color: {colors["sidebar_text_color"]};
    }}
    .css-qrbaxs {{
        background-color: {colors["sidebar_bg"]};
        color: {colors["sidebar_text_color"]};
    }}
    .stButton > button {{
        color: #FFFFFF !important;
        background-color: {colors["button_bg"]} !important;
        width: 100% !important;
        height: 50px !important;
        border-radius: 5px !important;
        font-size: 16px !important;
        margin-bottom: 10px !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }}
    .stButton > button:hover {{
        background-color: {colors["button_hover_bg"]} !important;
    }}
    /* Ocultar la barra superior */
    #MainMenu {{
        visibility: hidden;
    }}
    footer {{
        visibility: hidden;
    }}
    header {{
        visibility: hidden;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Logo en la barra lateral
st.sidebar.image("logos/rio.png", width=175)

# Título y descripción en la barra lateral
st.sidebar.title("Gobernanza del Agua Yaqui Vícam México")
st.sidebar.markdown("""
    <div style='color: #FFFFFF;'>
    Aquí podrás encontrar datos sobre la cuenca del río Yaqui, datos sociodemográficos de la comunidad Yaqui de Vícam en Sonora, México.
    </div>
""", unsafe_allow_html=True)

# Convertir el menú de navegación a botones
st.sidebar.markdown("---")
if st.sidebar.button("📘 Introducción, Zona de estudio"):
    navigation = "📘 Introducción, Zona de estudio"
elif st.sidebar.button("🗺️ Análisis Geográfico"):
    navigation = "🗺️ Análisis Geográfico"
elif st.sidebar.button("📊 Análisis Sociodemográfico"):
    navigation = "📊 Análisis Sociodemográfico"
elif st.sidebar.button("💦 Leyes de Agua"):
    navigation = "💦 Leyes de Agua"
else:
    navigation = "📘 Introducción, Zona de estudio"  # Valor predeterminado
st.sidebar.markdown("---")

# Filtros
st.sidebar.header("Filtros")
municipios = st.sidebar.selectbox('Municipios', ['Municipio 1', 'Municipio 2', 'Municipio 3'])
subcuencas = st.sidebar.selectbox('Subcuencas', ['Subcuenca 1', 'Subcuenca 2', 'Subcuenca 3'])

# Mostrar contenido basado en la selección del menú de navegación
if navigation == "📘 Introducción, Zona de estudio":
    st.markdown("<h2 style='color: #000000;'>Cuenca Rio Yaqui</h2>", unsafe_allow_html=True)  # Título en letras negras
    col1, col2 = st.columns([3, 2])

    with col1:
        st.image("mapas/cuenca_rio_yaqui.png", use_column_width=True)

    with col2:
        st.markdown(
            """
            <div style="color: #000000; font-size: 14px;">
            El mapa muestra la cuenca del Río Yaqui en el noroeste de México, destacando tres subcuencas: A. Sahuaral (azul oscuro), Álvaro Obregón (azul medio) y Vicam (azul claro). El río principal, el Yaqui, está marcado en rojo y fluye desde el noreste hacia el suroeste, desembocando en el Golfo de California. La red hidrográfica, representada por líneas blancas, ilustra los ríos y arroyos que alimentan al Yaqui. También se observa una cuadrícula en la parte inferior que podría indicar áreas urbanas o agrícolas, proporcionando una visión detallada de la distribución y flujo de agua en la región.
            </div>
            """, unsafe_allow_html=True
        )

# Sección Contact
st.sidebar.header("Contacto")
st.sidebar.markdown(
    """
    <div style="color: white;">
         tech@tecnicasrudas.org </a> 
         hello@diversa.studio </a> 
    </div>
    """, 
    unsafe_allow_html=True
)

# Logos en la misma línea
st.sidebar.markdown("<h2 style='color:white;'> </h2>", unsafe_allow_html=True)
col3, col4, col5 = st.sidebar.columns(3)

with col3:
    logo1 = Image.open("logos/logo1.png")
    st.image(logo1, width=100)

with col4:
    logo2 = Image.open("logos/logo2.png")
    st.image(logo2, width=100)

with col5:
    logo3 = Image.open("logos/logo3.png")
    st.image(logo3, width=100)

# Sección de visualizaciones existentes
st.header("Visualizaciones de Datos Existentes")
existing_data_files = os.listdir('data')
for file in existing_data_files:
    if file.endswith('.pdf'):
        st.subheader(file)
        st.write("Archivo PDF subido")
