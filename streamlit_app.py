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
st.sidebar.title("Gobernanza del Agua en el Pueblo Yaqui de Vícam-Sonora México")
st.sidebar.markdown("""
    <div style='color: #FFFFFF;'>
    Este dashboard muestra datos sobre la cuenca del río Yaqui, además de datos sociodemográficos de la comunidad Yaqui de Vicam en Sonora, México.
    </div>
""", unsafe_allow_html=True)

navigation = st.sidebar.radio(
    "Home",
    [
        "🏠 Análisis Sociodemográfico",
        "🗺️ Análisis Geográfico",
        "💦 Leyes de Agua",
        "🗺️ Basemaps"
    ]
)

# Mostrar contenido basado en la selección del menú de navegación
if navigation == "🏠 Home":
    st.write("Has seleccionado Home")
elif navigation == "📷 Timelapse":
    st.write("Has seleccionado Timelapse")
elif navigation == "🏡 U.S. Housing":
    st.write("Has seleccionado U.S. Housing")
elif navigation == "🗺️ Split Map":
    st.write("Has seleccionado Split Map")
elif navigation == "🔥 Heatmap":
    st.write("Has seleccionado Heatmap")
elif navigation == "📍 Marker Cluster":
    st.write("Has seleccionado Marker Cluster")
elif navigation == "🗺️ Basemaps":
    st.write("Has seleccionado Basemaps")

# Filtros
st.sidebar.header("Filtro")
municipios = st.sidebar.selectbox('Municipios', ['Municipio 1', 'Municipio 2', 'Municipio 3'])
subcuencas = st.sidebar.selectbox('Subcuencas', ['Subcuenca 1', 'Subcuenca 2', 'Subcuenca 3'])

# Contenido principal
if navigation == "🏠 Home":
    st.header("Mapa Dinamic World Sonora")
    st.image("mapas/dw_5municipios.png", use_column_width=True)
    st.markdown(
        """
        Este mapa muestra la cobertura del suelo en cinco municipios de la región de Sonora. Los colores representan diferentes tipos de cobertura del suelo, como áreas urbanas, vegetación, cuerpos de agua y áreas agrícolas. Esta información es crucial para la gestión de recursos naturales y la planificación territorial en la región.
        """, unsafe_allow_html=True
    )

# Sección Contact
st.sidebar.header("Contacto")
st.sidebar.markdown(
    """
    <div style="color: white;">
         tec@tecnicasrudas.org </a> 
         hello@diversa.studio </a> 
    </div>
    """, 
    unsafe_allow_html=True
)