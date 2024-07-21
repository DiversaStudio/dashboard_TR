
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
    "color1": "#D0DED4",
    "color2": "#E5E1C1",
    "color3": "#CAC3A9",
    "color4": "#D0E6EF",
    "color5": "#B0E2E7",
    "color6": "#70D3DC",
    "color7": "#8CA8AE",
    "color8": "#688D98",
    "color9": "#327378",
    "color10": "#4373B3",
    "color11": "#152F54"
}

# Aplicar colores personalizados a la interfaz
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {colors["content_bg"]};
        color: {colors["text_color"]};
    }}
    .css-1d391kg {{
        background-color: {colors["sidebar_bg"]};
        color: {colors["sidebar_text_color"]};
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
        background-color: {colors["color8"]} !important;
        width: 100% !important;
        height: 50px !important;
        border-radius: 5px !important;
        font-size: 16px !important;
    }}
    .stButton > button:hover {{
        background-color: {colors["color9"]} !important;
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

# Sidebar con menú de navegación
st.sidebar.title("Gobernanza del Agua Yaqui Vícam México")
st.sidebar.markdown("""
    <div style='color: #FFFFFF;'>
    Aquí podrás encontrar datos sobre la cuenca del río Yaqui, datos sociodemográficos de la comunidad Yaqui de Vícam en Sonora, México.
    </div>
""", unsafe_allow_html=True)

# Convertir el menú de navegación a botones
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

# Mostrar contenido basado en la selección del menú de navegación
#if navigation == "📘 Introducción, Zona de estudio":
#    st.write("Has seleccionado Introducción, Zona de estudio")
#elif navigation == "🗺️ Análisis Geográfico":
#    st.write("Has seleccionado Análisis Geográfico")
#elif navigation == "📊 Análisis Sociodemográfico":
 #   st.write("Has seleccionado Análisis Sociodemográfico")
#elif navigation == "💦 Leyes de Agua":
#    st.write("Has seleccionado Leyes de Agua")

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
col3, col4 = st.sidebar.columns(2)

with col3:
    logo1 = Image.open("logos/logo1.png")
    st.image(logo1, width=150)

with col4:
    logo2 = Image.open("logos/logo2.png")
    st.image(logo2, width=150)