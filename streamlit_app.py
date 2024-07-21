import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import os
import base64
from st_aggrid import AgGrid

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
        background-color: {colors["button_bg"]} !important;
        width: 100% !important;
        height: 50px !important;
        border-radius: 5px !important;
        font-size: 16px !important;
    }}
    .stButton > button:hover {{
        background-color: {colors["button_hover_bg"]} !important;
    }}
    .css-1vbkxwb, .css-1avcm0n, .css-1v3fvcr {{
        background-color: {colors["button_bg"]} !important;
        color: {colors["sidebar_text_color"]} !important;
        border-color: {colors["button_bg"]} !important;
    }}
    .css-1vbkxwb:hover, .css-1avcm0n:hover, .css-1v3fvcr:hover {{
        background-color: {colors["button_hover_bg"]} !important;
        color: {colors["sidebar_text_color"]} !important;
        border-color: {colors["button_hover_bg"]} !important;
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

elif navigation == "💦 Leyes de Agua":
    # Función para incrustar PDF en Streamlit
    def show_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    # Mostrar título y descripción
    st.markdown("<h1>Leyes de Protección del Agua en México</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        Aquí encontrarás una recopilación de las leyes y regulaciones más importantes relacionadas con la protección del agua en México. Estos documentos son fundamentales para entender el marco legal que rige la gestión y conservación de los recursos hídricos en el país.
        """
    )

    # Ruta al archivo Excel
    excel_path = "proteccion_leyes/Leyes .xlsx"

    # Verificar si el archivo existe y leerlo
    if os.path.exists(excel_path):
        df_excel = pd.read_excel(excel_path)
        st.subheader("Resumen de Leyes")
        AgGrid(df_excel)
    else:
        st.error(f"Error al leer el archivo Excel: {excel_path} no se encontró.")

    # Mostrar PDFs
    st.subheader("Documentos en PDF")
    pdf_folder = "proteccion_leyes"
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        st.markdown(f"### {pdf_file}")
        show_pdf(os.path.join(pdf_folder, pdf_file))

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
    st.image(logo1, width=100)

with col4:
    logo2 = Image.open("logos/logo2.png")
    st.image(logo2, width=100)

# Nuevo logo centrado debajo de los otros dos logos
st.sidebar.markdown("<h2 style='color:white;'> </h2>", unsafe_allow_html=True)
logo3 = Image.open("logos/logo3.png")
st.sidebar.image(logo3, width=100)
