# Librerías necesarias
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import os
import base64
from st_aggrid import AgGrid, GridOptionsBuilder, AgGridTheme

# Definir los colores
colors = {
    "sidebar_bg": "#152F54",  # Color para la barra lateral
    "content_bg": "#FFFFFF",
    "text_color": "#000000",  # Color negro para el texto
    "sidebar_text_color": "#FFFFFF",  # Color blanco para el texto de la barra lateral
    "button_bg": "#688D98",  # Color para los botones
    "button_hover_bg": "#327378"  # Color de los botones al pasar el ratón
}

# Aplicar paleta de colores a la interfaz
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
    </style>
    """,
    unsafe_allow_html=True
)
#Barra Lateral

# Imagen en la barra lateral
st.sidebar.image("logos/rio.png", width=300)

# Título y descripción en la barra lateral
st.sidebar.title("Gobernanza del Agua en la Comunidad Yaqui de Vícam, México")
st.sidebar.markdown("""
    <div style='color: #FFFFFF;'>
    Explora información clave sobre la cuenca del río Yaqui y la comunidad Yaqui de Vícam, Sonora. Aquí encontrarás datos sociodemográficos, análisis detallados de la gobernanza del agua local, y un resumen de las leyes de protección del agua en México.
    </div>
""", unsafe_allow_html=True)


# Inicializar la variable de estado para la navegación
if "navigation" not in st.session_state:
    st.session_state.navigation = "📍Introducción-Zona de estudio"

# Crear los botones de navegación
st.sidebar.markdown("---")
if st.sidebar.button("📍Introducción-Zona de estudio"):
    st.session_state.navigation = "📍 Introducción-Zona de estudio"
if st.sidebar.button("📊 Análisis Sociodemográfico"):
    st.session_state.navigation = "📊 Análisis Sociodemográfico"
if st.sidebar.button("🗺️ Análisis Geográfico"):
    st.session_state.navigation = "🗺️ Análisis Geográfico"
if st.sidebar.button("💦 Leyes del Agua en México"):
    st.session_state.navigation = "💦 Leyes del Agua en México"
st.sidebar.markdown("---")


# Mostrar contenido basado en la selección del menú de navegación ZONA DE ESTUDIO
if st.session_state.navigation == "📍Introducción-Zona de estudio":
    st.markdown("<h2 style='color: #000000;'>Cuenca del Río Yaqui</h2>", unsafe_allow_html=True)  # Título en letras negras
    
    # Mostrar el mapa en un tamaño más grande
    st.image("mapas/cuenca_rio_yaqui.png", use_column_width=True)
    
    # Colocar el texto explicativo debajo del gráfico
    st.markdown(
        """
        <div style="color: #000000; font-size: 14px;">
        El mapa muestra la cuenca del Río Yaqui en el noroeste de México, destacando tres subcuencas: A. Sahuaral (azul oscuro), Álvaro Obregón (azul medio) y Vícam (azul claro). El río principal, el Yaqui, está marcado en rojo y fluye desde el noreste hacia el suroeste, desembocando en el Golfo de California. La red hidrográfica, representada por líneas blancas, ilustra los ríos y arroyos que alimentan al Yaqui. Además, se observa una cuadrícula en la parte inferior que  indica áreas urbanas, proporcionando una visión detallada de la distribución y el flujo de agua en la región.
        </div>
        """, unsafe_allow_html=True
    )

    # Crear una fila para los KPIs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Área total de la cuenca hidrográfica", value="Área total de la cuenca", delta="2%")
    
    with col2:
        st.metric(label="Área de cada subcuenca", value="Área de cada subcuenca", delta="1%")
    
    with col3:
        st.metric(label="Longitud total del Río Yaqui", value="Longitud total del Río Yaqui", delta="5%")

    # Aplicar estilos CSS para ajustar el tamaño de la fuente de las métricas
    st.markdown(
        """
        <style>
        div[data-testid="stMetric"] > label {
            font-size: 14px;
        }
        div[data-testid="stMetric"] > div {
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Mostrar contenido basado en la selección del menú de navegación ANÁLISIS SOCIODEMOGRÁFICO
elif st.session_state.navigation == "📊 Análisis Sociodemográfico":
    st.markdown("<h2 style='color: #000000;'>Territorio Yaqui Localidades</h2>", unsafe_allow_html=True)  # Título en letras negras
    
    # Mostrar el mapa de Territorio Yaqui Localidades
    st.image("mapas/territorio_yaqui.png", use_column_width=True)
    
    # Texto explicativo del mapa
    st.markdown(
        """
        <div style="color: #000000; font-size: 14px;">
        Este mapa de Sonora incluye varios municipios: Bácum, Cajeme, Empalme, Guaymas y San Ignacio Río Muerto. El mapa está delimitado por coordenadas geográficas, con latitudes que van desde aproximadamente 26.5 a 29.5 grados norte, y longitudes desde -111.5 a -109 grados oeste.
        Un aspecto destacado de éste análisis es una línea azul que delimita el "Territorio Yaqui", una región que parece extenderse a través de varios municipios.
        Hay numerosos puntos amarillos dispersos por todo el mapa, que representan "Localidades", indicando asentamientos o poblaciones. Estas localidades varían en tamaño, desde pequeños asentamientos con uno o dos hogares hasta grandes localidades con 200 hogares.
        Los diferentes municipios están representados por colores distintos, siendo Guaymas el más grande, ocupando gran parte del área central y costera del mapa.
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("<hr style='border:1px solid #688C98;'>", unsafe_allow_html=True)

    # Título de análisis sociodemográfico y texto introductorio
    st.markdown("<h2 style='color: #000000;'>Análisis Sociodemográfico</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="color: #000000; font-size: 14px;">
        Los datos presentados en esta sección provienen del Censo de Población y Vivienda 2020, realizado por el Instituto Nacional de Estadística y Geografía (INEGI) de México. Este gráfico es uno de los varios que se muestran y proporciona una visión detallada de la distribución de la población por género en los municipios de Cajeme, Guaymas, Empalme, Bácum y San Ignacio Río Muerto. Los datos reflejan la composición demográfica en cada municipio.
        </div>
        """, unsafe_allow_html=True
    )

    # Definir la ruta base para las imágenes
    base_path = "sociodemografico"
    
    # Listado de imágenes y títulos con textos explicativos
    images = [
        {
            "file": "Poblacion_genero.png", 
            "title": "Población Género",
            "description": "Este gráfico proporciona una visión detallada de la distribución de la población por género en los municipios de Cajeme, Guaymas, Empalme, Bácum y San Ignacio Río Muerto. Los datos reflejan la composición demográfica de estas áreas, destacando la cantidad de habitantes masculinos y femeninos en cada municipio."
        },
        {
            "file": "Poblacion_rangoetario.png", 
            "title": "Población Rango Etario",
            "description": "Este gráfico muestra la distribución de la población por rangos etarios en los municipios de Cajeme, Guaymas, Empalme, Bácum y San Ignacio Río Muerto. Proporciona información sobre la cantidad de personas en diferentes grupos de edad, ayudando a entender la estructura demográfica de la región."
        },
        {
            "file": "Vivienda_comunicacion.png", 
            "title": "Medios de Comunicación",
            "description": "Este gráfico ilustra el acceso y uso de diferentes medios de comunicación en los municipios de Cajeme, Guaymas, Empalme, Bácum y San Ignacio Río Muerto. Muestra datos sobre la disponibilidad de televisión, radio, internet y otros medios, destacando las diferencias en el acceso a la información entre las localidades."
        },
        {
            "file": "Vivienda_servicios.png", 
            "title": "Servicios",
            "description": "Este gráfico proporciona información sobre la disponibilidad y acceso a diferentes servicios en los municipios de Cajeme, Guaymas, Empalme, Bácum y San Ignacio Río Muerto. Incluye datos sobre servicios básicos como agua, electricidad y saneamiento, mostrando las condiciones de vida en estas áreas."
        }
    ]
    
    # Mostrar las imágenes principales con descripciones y separadores
    for image in images:
        image_path = os.path.join(base_path, image["file"])
        if os.path.exists(image_path):
            st.markdown(f"<h3 style='color: #000000;'>{image['title']}</h3>", unsafe_allow_html=True)
            st.image(image_path, caption=image["title"], use_column_width=True)
            st.markdown(
                f"""
                <div style="color: #000000; font-size: 14px;">
                {image["description"]}
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.error(f"Error opening '{image_path}'")

    # Separador antes de los gráficos de dona
    st.markdown("<hr style='border:1px solid #688C98;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #000000;'>Actividad Económica</h2>", unsafe_allow_html=True)

    # Gráficos de dona con descripciones y separadores
    dona_images = [
        {
            "file": "Dona_Ingresos_Bácum.png", 
            "title": "Ingresos Bácum",
            "description": "Este gráfico de dona muestra la distribución de ingresos en el municipio de Bácum. Proporciona una visión clara de las diferencias económicas entre los habitantes, destacando los distintos niveles de ingresos en la región."
        },
        {
            "file": "Dona_Ingresos_Cajeme.png", 
            "title": "Ingresos Cajeme",
            "description": "Este gráfico de dona muestra la distribución de ingresos en el municipio de Cajeme. Proporciona una visión clara de las diferencias económicas entre los habitantes, destacando los distintos niveles de ingresos en la región."
        },
        {
            "file": "Dona_Ingresos_Empalme.png", 
            "title": "Ingresos Empalme",
            "description": "Este gráfico de dona muestra la distribución de ingresos en el municipio de Empalme. Proporciona una visión clara de las diferencias económicas entre los habitantes, destacando los distintos niveles de ingresos en la región."
        },
        {
            "file": "Dona_Ingresos_Guaymas.png", 
            "title": "Ingresos Guaymas",
            "description": "Este gráfico de dona muestra la distribución de ingresos en el municipio de Guaymas. Proporciona una visión clara de las diferencias económicas entre los habitantes, destacando los distintos niveles de ingresos en la región."
        },
        {
            "file": "Dona_Ingresos_San_Ignacio_Rio_Muerto.png", 
            "title": "Ingresos San Ignacio Río Muerto",
            "description": "Este gráfico de dona muestra la distribución de ingresos en el municipio de San Ignacio Río Muerto. Proporciona una visión clara de las diferencias económicas entre los habitantes, destacando los distintos niveles de ingresos en la región."
        }
    ]
    
    # Mostrar los gráficos de dona con descripciones y separadores
    for image in dona_images:
        image_path = os.path.join(base_path, image["file"])
        if os.path.exists(image_path):
            st.markdown(f"<h3 style='color: #000000;'>{image['title']}</h3>", unsafe_allow_html=True)
            st.image(image_path, caption=image["title"], use_column_width=True)
            st.markdown(
                f"""
                <div style="color: #000000; font-size: 14px;">
                {image["description"]}
                </div>
                """, unsafe_allow_html=True
            )
        else:
            continue  # Simplemente ignora las imágenes que no se encuentran sin mostrar el error

# Mostrar contenido basado en la selección del menú de navegación ANÁLISIS GEOGRÁFICO
elif st.session_state.navigation == "🗺️ Análisis Geográfico":
    st.markdown("<h2 style='color: #000000;'>Análisis Geográfico</h2>", unsafe_allow_html=True)  # Título principal

    # Primera imagen y texto
    st.image("geografico/mapa_fisico.png", use_column_width=True)
    st.markdown(
        """
        <div style="color: #000000; font-size: 14px;">
        Este mapa físico muestra la topografía de la región del Río Yaqui en Sonora, México. Se destacan las elevaciones y depresiones del terreno, así como las principales características geográficas que influencian el flujo y la distribución del agua en la cuenca.
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("<hr style='border:1px solid #688C98;'>", unsafe_allow_html=True)

    # Subtítulo, segunda imagen y texto
    st.markdown("<h3 style='color: #000000;'>Mapa de Uso del Suelo</h3>", unsafe_allow_html=True)
    st.image("geografico/uso_suelo.png", use_column_width=True)
    st.markdown(
        """
        <div style="color: #000000; font-size: 14px;">
        El mapa de uso del suelo muestra cómo se distribuyen diferentes tipos de uso del terreno en la región, incluyendo áreas urbanas, agrícolas y naturales. Esta información es crucial para entender las dinámicas económicas y ambientales del área de estudio.
        </div>
        """, unsafe_allow_html=True
    )


elif st.session_state.navigation == "💦 Leyes del Agua en México":
    # Función para incrustar PDF en Streamlit
    def show_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    # Mostrar título y descripción
    st.markdown("<h1 style='color: #000000;'><b>Leyes de Protección del Agua en México</b></h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="color: #000000;">
        Aquí encontrarás una recopilación de las leyes y regulaciones más importantes relacionadas con la protección del agua en México. Estos documentos son fundamentales para entender el marco legal que rige la gestión y conservación de los recursos hídricos en el país.
        </div>
        """, unsafe_allow_html=True
    )

    # Ruta al archivo Excel
    excel_path = "proteccion_leyes/Leyes.xlsx"

    # Verificar si el archivo existe y leerlo
    if os.path.exists(excel_path):
        df_excel = pd.read_excel(excel_path)
        st.markdown("<h2 style='color: #000000;'><b>Resumen de Leyes</b></h2>", unsafe_allow_html=True)
        gb = GridOptionsBuilder.from_dataframe(df_excel)
        gb.configure_default_column(cellStyle={'color': colors["sidebar_text_color"], 'backgroundColor': colors["button_bg"]})
        gb.configure_column("Ley/ Norma/ Constitución/ Programas", headerStyle={'fontWeight': 'bold', 'color': colors["text_color"]})
        gb.configure_column("Artículo", headerStyle={'fontWeight': 'bold', 'color': colors["text_color"]})
        gb.configure_column("¿Qué establece?", headerStyle={'fontWeight': 'bold', 'color': colors["text_color"]})
        gb.configure_column("Link", headerStyle={'fontWeight': 'bold', 'color': colors["text_color"]})
        gridOptions = gb.build()
        AgGrid(df_excel, gridOptions=gridOptions, theme='streamlit')
    else:
        st.error(f"Error al leer el archivo Excel: {excel_path} no se encontró.")

    # Mostrar PDFs
    st.markdown("<h2 style='color: #000000;'><b>Documentos en PDF</b></h2>", unsafe_allow_html=True)
    pdf_folder = "proteccion_leyes"
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        st.markdown(f"<h3 style='color: #000000;'>{pdf_file}</h3>", unsafe_allow_html=True)
        show_pdf(os.path.join(pdf_folder, pdf_file))
# Sección Contacto
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

