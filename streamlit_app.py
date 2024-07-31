# Librerías necesarias
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import os
import base64
from st_aggrid import AgGrid, GridOptionsBuilder, AgGridTheme

# Definir los colores de toda la web
colors = {
    "sidebar_bg": "#152F54",  # Color para la barra lateral
    "content_bg": "#FFFFFF",
    "text_color": "#000000",  # Color negro para el texto
    "sidebar_text_color": "#FFFFFF",  # Color blanco para el texto de la barra lateral
    "button_bg": "#688C98",  # Color para los botones
    "button_hover_bg": "#327378"  # Color de los botones al pasar el ratón
}

# Aplicar colores personalizados a la interfaz
st.markdown(
    f"""
    <style>
    /* Estilo general de la aplicación */
    .stApp {{
        background-color: {colors["content_bg"]};
        color: {colors["text_color"]};
    }}

    /* Estilos de la barra lateral */
    .css-1d391kg, .css-1lcbmhc.e1fqkh3o3, .css-1e5imcs, .css-qrbaxs {{
        background-color: {colors["sidebar_bg"]};
        color: {colors["sidebar_text_color"]};
    }}

    /* Estilos de botones */
    .stButton > button {{
        color: {colors["sidebar_text_color"]} !important;
        background-color: {colors["button_bg"]} !important;
        width: 100% !important;
        height: 50px !important;
        border-radius: 5px !important;
        font-size: 16px !important;
        border: none !important;
        transition: background-color 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: {colors["button_hover_bg"]} !important;
    }}

    /* Estilos para selectbox, multiselect, y otros widgets */
    .css-1vbkxwb, .css-1avcm0n, .css-1v3fvcr {{
        background-color: {colors["button_bg"]} !important;
        color: {colors["sidebar_text_color"]} !important;
        border-color: {colors["button_bg"]} !important;
    }}
    .css-1vbkxwb:hover, .css-1avcm0n:hover, .css-1v3fvcr:hover {{
        background-color: {colors["button_hover_bg"]} !important;
        border-color: {colors["button_hover_bg"]} !important;
    }}

    /* Estilos para títulos y texto en la barra lateral */
    .sidebar .sidebar-content {{
        background-color: {colors["sidebar_bg"]};
    }}
    .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {{
        color: {colors["sidebar_text_color"]};
        font-family: Arial, sans-serif;
    }}
    .sidebar .sidebar-content p, .sidebar .sidebar-content div {{
        color: {colors["sidebar_text_color"]};
        font-family: Arial, sans-serif;
    }}

    /* Estilos para los enlaces en la barra lateral */
    .sidebar .sidebar-content a {{
        color: {colors["sidebar_text_color"]};
        text-decoration: none;
    }}
    .sidebar .sidebar-content a:hover {{
        text-decoration: underline;
    }}

    /* Estilos para los separadores */
    hr {{
        border-color: {colors["button_bg"]};
    }}

    /* Estilos para los títulos en el contenido principal */
    .main .block-container h1, .main .block-container h2, .main .block-container h3 {{
        color: {colors["text_color"]};
        font-family: Arial, sans-serif;
    }}

    /* Ajustes adicionales para mejorar la legibilidad */
    .stTextInput > div > div > input {{
        color: {colors["text_color"]};
    }}
    .stTextInput > label {{
        color: {colors["text_color"]};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Logo en la barra lateral
st.sidebar.image("logos/rio.png", width=300)

# Título y descripción en la barra lateral
st.sidebar.title("Gobernanza del Agua Yaqui Vícam México")
st.sidebar.markdown("""
    <div style='color: #FFFFFF; font-family: Arial, sans-serif; font-size: 14px;'>
    Descubre información esencial sobre la cuenca del río Yaqui y la comunidad Yaqui de Vícam, Sonora. Aquí encontrarás datos sociodemográficos actualizados, análisis de la gestión hídrica local y detalles sobre los desafíos y oportunidades en el manejo del agua en esta región.
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<hr style='border-color: #688C98;'>", unsafe_allow_html=True)


# Inicializar la variable de estado para la navegación
if "navigation" not in st.session_state:
    st.session_state.navigation = "📖 Introducción"

# Crear los botones de navegación principales
if st.sidebar.button("📖 Introducción"):
    st.session_state.navigation = "📖 Introducción"
if st.sidebar.button("📍Zona de estudio"):
    st.session_state.navigation = "📍Zona de estudio"
if st.sidebar.button("📊 Análisis Sociodemográfico"):
    st.session_state.navigation = "📊 Análisis Sociodemográfico"
if st.sidebar.button("🌿 Cobertura del Suelo"):
    st.session_state.navigation = "🌿 Cobertura del Suelo"
if st.sidebar.button("🏞️ Clasificación histórica"):
    st.session_state.navigation = "🏞️ Clasificación histórica"
if st.sidebar.button("💨 Evapotranspiración"):
    st.session_state.navigation = "💨 Evapotranspiración"
if st.sidebar.button("💧 Acumulaciones"):
    st.session_state.navigation = "💧 Acumulaciones"
if st.sidebar.button("💦 Leyes del Agua en México"):
    st.session_state.navigation = "💦 Leyes del Agua en México"

st.sidebar.markdown("---")

#Sección Introducción ZONA DE ESTUDIO
# Función para crear tarjetas de métricas
def create_metric_card(title, value, delta, icon):
    return f"""
    <div style="
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 10px;
        text-align: center;
        transition: transform 0.3s ease-in-out;
    ">
        <h4 style="font-size: 16px; color: #666; margin-bottom: 10px;">{title}</h4>
        <div style="font-size: 28px; font-weight: bold; color: #1B2F54; margin-bottom: 10px;">
            {icon} {value}
        </div>
        <div style="font-size: 14px; color: {'#D6ECEF' if float(delta.strip('%')) > 0 else '#D6ECEF'};">
            {delta}
        </div>
    </div>
    """

# Mostrar contenido basado en la selección del menú de navegación "📖 Introducción"
if st.session_state.navigation == "📖 Introducción":
    st.markdown(
        """
        <h2 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Introducción</h2>
        <div style="color: #000000; font-size: 14px;">
        Uno de los temas centrales para la supervivencia de la humanidad es la forma en que nos relacionamos con todas las formas de vida y las interacciones que se generan en el tiempo y espacio que habitan. En este contexto, la gobernanza del agua es crucial, especialmente para comunidades como la tribu Yaqui de Vícam, México. Este proyecto explora cómo la Inteligencia Artificial puede ser una herramienta útil para la toma de decisiones sobre el uso de los recursos naturales, específicamente el agua, y como un instrumento político para contrarrestar la confrontación con el Estado y evitar el despojo de sus recursos.
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Gobernanza del Agua</h2>
        <div style="color: #000000; font-size: 14px;">
        La gobernanza del agua es un tema fundamental que se vuelve cada vez más relevante en un planeta con recursos finitos. Al final del siglo pasado, cuando se hizo evidente que el crecimiento económico constante no es sostenible, se hizo necesario "cambiar de rumbo" y avanzar hacia un desarrollo económico sostenible. En 1992, durante la cumbre internacional ECO 92, los gobiernos participantes acordaron una serie de documentos clave que sentaron las bases para una nueva política global sobre la gobernanza de los recursos naturales. Entre estos documentos se encuentran la Declaración de Río sobre el Medio Ambiente y el Desarrollo, la Agenda 21 y las convenciones sobre el cambio climático y la biodiversidad.
        En 2015, la conceptualización de lo que implica el desarrollo sostenible se reflejó en la creación de la Agenda 2030, que estableció 17 Objetivos de Desarrollo Sostenible (ODS). Estos objetivos abarcan desde la erradicación de la pobreza y el hambre hasta la acción por el clima y la vida en ecosistemas terrestres y acuáticos. Al mismo tiempo, en 2011, nació la Alianza para el Gobierno Abierto (OGP) con el objetivo de lograr formas de gobernanza más democráticas basadas en metodologías innovadoras acordadas por la sociedad civil, el gobierno y el sector empresarial. A pesar de los acuerdos y compromisos firmados, la implementación efectiva de estas políticas sigue siendo un desafío, especialmente en la vinculación de los ODS con los derechos humanos reconocidos.
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Primera Fase del Proyecto</h2>
        <div style="color: #000000; font-size: 14px;">
        La primera etapa del proyecto se enfoca en establecer las bases para un enfoque innovador y transformador en la gobernanza de los recursos naturales. Inspirado por la cita de Goethe en Fausto, "¿Cómo te he de aprehender, Naturaleza infinita?", esta fase busca romper con la fragmentación y división tradicionales, promoviendo un conocimiento integral basado en la experiencia, los sentidos y las emociones. Priorizamos la construcción colectiva a través del diálogo y la escucha, alejándose de prácticas coloniales y extractivistas de datos e información. 
        Las metodologías empleadas incluyen la educación popular, el arte comunitario y la ternura radical, fomentando relaciones intergeneracionales que enriquecen la perspectiva del proyecto. 
        La autodeterminación de la comunidad es fundamental, permitiendo decidir qué datos compartir y construyendo un horizonte común basado en una cultura narrada y compartida. 
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <h2 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Actividades</h2>

    <h3 style='font-family: Arial, sans-serif; font-size: 18px; color: #1B2F54;'>El paisaje de Vícam</h3>
    <div style="color: #000000; font-size: 14px;">
    Esta actividad respondía a las preguntas: ¿Cómo es el paisaje de la comunidad? ¿Cómo se ha modificado a través del tiempo? Pasado y presente.
    Lxs personxs realizaron dos dibujos, el primero mostraba lo que contaban los abuelos que era Vícam, y el segundo lo que es ahora. Estos dos dibujos permitirán ver una comparación del paisaje de años atrás y actual, enfatizando en la degradación del ecosistema. Esta actividad abre el diálogo intergeneracional al preguntarse entre ellas cómo era antes y cómo es ahora.
    </div>
    """, unsafe_allow_html=True
    )

    # Mostrar las imágenes correspondientes
    col1, col2 = st.columns(2)

    with col1:
        st.image("etapa1/36_antes.jpg", caption="Vícam Antes", width=280)

    with col2:
        st.image("etapa1/36_ahora.jpg", caption="Vícam Ahora", width=280)
    st.markdown(
    """
    <h3 style='font-family: Arial, sans-serif; font-size: 18px; color: #1B2F54;'>La memoria de Vícam</h3>
    <div style="color: #000000; font-size: 14px;">
    Lxs personxs participantes hicieron un juego nombrando las especies de flora y fauna que existieron y existen en la comunidad.
    Con esta actividad se genera un mapeo de cómo han desaparecido algunas especies debido a la degradación del ecosistema en el territorio.
    </div>

    <h3 style='font-family: Arial, sans-serif; font-size: 18px; color: #1B2F54;'>Carta al río Yaqui</h3>
    <div style="color: #000000; font-size: 14px;">
    Realizamos una carta al río Yaqui, nombrando cuál es el significado del río para cada integrante, haciendo conciencia de su valor dentro de la comunidad y de la historia de lucha y resistencia que existe alrededor de él.
    </div>

    <h3 style='font-family: Arial, sans-serif; font-size: 18px; color: #1B2F54;'>Violentómetro</h3>
    <div style="color: #000000; font-size: 14px;">
    En esta actividad lxs participantes nombran las múltiples violencias que aquejan a la comunidad, el grado de afectación que provocan y las mayores preocupaciones. Esta dinámica revela problemas que en muchos casos no se nombran o se ocultan y se consideran de índole privada. Socializamos los problemas ynos permitimos imaginar algunas soluciones posibles.
    </div>

    <h3 style='font-family: Arial, sans-serif; font-size: 18px; color: #1B2F54;'>Canción al río Yaqui</h3>
    <div style="color: #000000; font-size: 14px;">
    Recopilamos narrativas que describen el territorio y sus cambios a lo largo de la historia hechos por las presas, empresas y acueductos.
    </div>
    """, 
    unsafe_allow_html=True
    )
# Mostrar la imagen correspondiente
    st.image("etapa1/cancion.png", caption="Canción al río Yaqui", use_column_width=True)

# Función actualizada para crear tarjetas de métricas sin porcentajes
def create_metric_card(title, value, icon):
    return f"""
    <div style="
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    ">
        <h4 style="color: #1B2F54; margin-bottom: 10px;">{title}</h4>
        <p style="font-size: 24px; font-weight: bold; margin: 0;">{icon} {value}</p>
    </div>
    """

# Sección Zona de estudio
if st.session_state.navigation == "📍Zona de estudio":
    st.markdown(
        """
        <h2 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Cuenca del Río Yaqui</h2>
        <div style="color: #000000; font-size: 14px;">
        El mapa muestra la cuenca del Río Yaqui en el noroeste de México, destacando tres subcuencas: A. Sahuaral (azul oscuro), Álvaro Obregón (azul medio) y Vícam (azul claro). El río principal, el Yaqui, está marcado en rojo y fluye desde el noreste hacia el suroeste, desembocando en el Golfo de California. La red hidrográfica, representada por líneas blancas, ilustra los ríos y arroyos que alimentan al Yaqui. Además, se observa una cuadrícula en la parte inferior que indica áreas urbanas, proporcionando una visión detallada de la distribución y el flujo de agua en la región.
        </div>
        """, unsafe_allow_html=True
    )
    # Mostrar el mapa en un tamaño más grande
    st.image("mapas/cuenca_rio_yaqui.png", use_column_width=True)
    
    # Rediseñar la fila de KPIs
    st.markdown("<h3 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54; margin-bottom: 20px;'>Indicadores Importantes </h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(create_metric_card("Área total de la cuenca", "72,540 km²", "🌊"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_metric_card("Área promedio de subcuenca", "24,180 km²", "🗺️"), unsafe_allow_html=True)
    with col3:
        st.markdown(create_metric_card("Longitud del Río Yaqui", "320 km", "🏞️"), unsafe_allow_html=True)
    
    # Agregar una descripción general de los KPIs
    st.markdown("""
    <div style="
        background-color: #f0f8ff;
        border-left: 5px solid #1B2F54;
        padding: 15px;
        margin-top: 20px;
        font-size: 14px;
        color: #333;
    ">
        <strong>Análisis de KPIs:</strong> Estos indicadores muestran las dimensiones clave de la cuenca del Río Yaqui.
        El área total de la cuenca y el área promedio de las subcuencas proporcionan una idea de la extensión del sistema hidrológico,
        mientras que la longitud del Río Yaqui indica el alcance del río principal en la región.
    </div>
    """, unsafe_allow_html=True)


# Sección ANALISIS SOCIODEMOGRAGICO
elif st.session_state.navigation == "📊 Análisis Sociodemográfico":
    st.markdown("<h2 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54;'>Territorio Yaqui Localidades</h2>", unsafe_allow_html=True)
    
    # Mostrar el mapa de Territorio Yaqui Localidades
    st.image("mapas/territorio_yaqui.png", use_column_width=True)
    
    # Texto explicativo del mapa
    
    st.markdown("<hr style='border:1px solid #688C98;'>", unsafe_allow_html=True)

    # Título de análisis sociodemográfico y texto introductorio
    st.markdown("<h2 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54;'>Análisis Sociodemográfico</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="font-size: 14px; color: #333; margin-top: 20px; margin-bottom: 20px;">
        Esta sección presenta datos extraídos del Censo de Población y Vivienda 2020, llevado a cabo por el Instituto Nacional de Estadística y Geografía (INEGI) de México.
        Los datos proporcionados reflejan la realidad demográfica de la región, ofreciendo una base sólida para análisis socioeconómicos y planificación de políticas públicas.
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
            "description": "La distribución demográfica por rangos etarios en cinco municipios clave de Sonora, Cajeme, Guaymas, Empalme, Bácum y San Ignacio Río Muerto. Esta representación visual desglosa la población en diversos grupos de edad, proporcionando una perspectiva integral de la estructura demográfica de cada localidad. Al ilustrar la cantidad de habitantes en diferentes etapas de vida, el gráfico facilita la comprensión de patrones generacionales significativos, como la proporción de jóvenes, adultos en edad laboral y personas mayores. Esta información resulta vital para el análisis comparativo entre municipios, ofreciendo insights valiosos para la planificación urbana, el diseño de políticas públicas y la previsión de necesidades sociales específicas de cada grupo etario en la región."
        },
        {
            "file": "Vivienda_comunicacion.png", 
            "title": "Medios de Comunicación",
            "description": "El acceso y uso de diversos medios de comunicación en cinco municipios de Sonora, se analizan mediante una representación visual detallada. Esta visualización ilustra la disponibilidad de tecnologías como celular e internet, así como otros medios informativos, revelando patrones distintivos entre las localidades. Los datos expuestos facilitan un examen profundo de las diferencias digitales y mediáticas en la región."
        },
        {
            "file": "Vivienda_servicios.png", 
            "title": "Servicios",
            "description": "La disponibilidad y el acceso a servicios esenciales en cinco municipios clave de Sonora - Cajeme, Guaymas, Empalme, Bácum y San Ignacio Río Muerto - se examinan en detalle mediante una representación visual comprehensiva. Este análisis abarca servicios básicos fundamentales como el suministro de agua potable, la cobertura eléctrica y los sistemas de drenaje, ofreciendo una perspectiva clara de las condiciones de vida en estas localidades. Los datos presentados permiten una evaluación comparativa de la infraestructura municipal, revelando disparidades y áreas de oportunidad en la prestación de servicios"
        }
    ]
# Mostrar las imágenes principales con descripciones y separadores
    for image in images:
        image_path = os.path.join(base_path, image["file"])
        st.markdown(f"<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>{image['title']}</h3>", unsafe_allow_html=True)
        st.image(image_path, caption=image["title"], use_column_width=True)
        st.markdown(
            f"""
            <div style="background-color: #f0f8ff; border-left: 5px solid #1B2F54; padding: 15px; margin-top: 20px; font-size: 14px; color: #333;">
            {image["description"]}
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("<hr style='border:1px solid #688C98;'>", unsafe_allow_html=True)

    # Título de Actividad Económica
    st.markdown("<h2 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54;'>Actividad Económica</h2>", unsafe_allow_html=True)

    # Gráficos de dona con descripciones y separadores
    dona_images = [
        {
            "file": "Dona_Ingresos_Bácum.png", 
            "title": "Ingresos Económicos  Bácum",
            "description": "La distribución de ingresos económicos en el municipio de Bácum revela una estructura económica diversificada, con un total de ingresos de 1,177 millones de pesos. Esta distribución ofrece una visión clara de las actividades económicas predominantes en la región.El comercio minorista se posiciona como el sector líder, generando 524 millones de pesos, lo que representa el 44.5% del total de ingresos. Este dato subraya la importancia del comercio local en la economía de Bácum. La manufactura ocupa el segundo lugar, aportando 318 millones de pesos, equivalente al 27% de los ingresos totales. Este sector demuestra una pre sencia industrial significativa en el municipio. El sector agropecuario y agroindustrial contribuye con 191 millones de pesos, representando el 16.2% de los ingresos. Esta cifra refleja la relevancia de las actividades agrícolas y ganaderas en la economía local. Otras actividades diversas generan 144 millones de pesos, constituyendo el 12.3% restante de los ingresos. Esta categoría probablemente incluye servicios y otras industrias no especificadas en detalle. Esta distribución de ingresos muestra una economía municipal con un fuerte énfasis en el comercio minorista, respaldada por sectores manufactureros y agrícolas significativos. La diversificación de las fuentes de ingresos sugiere una base económica relativamente equilibrada para Bácum."
        },
        {
            "file": "Dona_Ingresos_Cajeme.png", 
            "title": "Ingresos Económicos Cajeme",
            "description": "El gráfico circular y la tabla adjunta ilustran la distribución de ingresos económicos en el municipio de Cajeme, ofreciendo una visión detallada de su estructura económica. Con un total de ingresos de 108,204 millones de pesos, Cajeme muestra una diversificación significativa en sus actividades económicas. La manufactura emerge como el sector dominante, generando 35,250 millones de pesos, lo que representa el 32.6 %  del total de ingresos. Este dato subraya la importancia de la industria en la economía local. El comercio, tanto minorista como mayorista, constituye una parte sustancial de la economía de Cajeme. El comercio minorista aporta 29,178 millones de pesos (27% del total), mientras que el comercio mayorista contribuye con 26,940 millones (24.9%). Juntos, estos sectores comerciales representan más de la mitad de los ingresos del municipio. Otras actividades diversas generan 16,836 millones de pesos, constituyendo el 15.6% restante de los ingresos. Esta categoría probablemente incluye servicios, agricultura y otras industrias no especificadas en detalle. Esta distribución de ingresos revela una economía municipal equilibrada, con una base industrial sólida complementada por un robusto sector comercial. La diversificación de las fuentes de ingresos sugiere una resiliencia económica potencial frente a fluctuaciones en sectores específicos."
        },
        {
            "file": "Dona_Ingresos_Empalme.png", 
            "title": "Ingresos Económicos Empalme",
            "description": "La distribución de ingresos económicos en el municipio de Empalme revela una estructura económica claramente dominada por el sector manufacturero, con un total de ingresos de 11,197 millones de pesos. La manufactura se posiciona como el sector líder indiscutible, generando 6,909 millones de pesos, lo que representa el 61.7% del total de ingresos. Este dato subraya la importancia crucial de la industria en la economía de Empalme. El comercio minorista ocupa el segundo lugar, aportando 1,772 millones de pesos, equivalente al 15.8% de los ingresos totales. Aunque significativamente menor que la manufactura, este sector aún juega un papel importante en la economía local. La construcción contribuye de manera similar al comercio minorista, con 1,735 millones de pesos, representando el 15.5% de los ingresos. Este sector indica una actividad considerable en el desarrollo de infraestructura y proyectos de edificación en el municipio. Otras actividades diversas generan 781 millones de pesos, constituyendo el 7% restante de los ingresos. Esta categoría probablemente incluye servicios y otras industrias no especificadas en detalle. Esta distribución de ingresos muestra una economía municipal fuertemente orientada hacia la manufactura, complementada por sectores de comercio y construcción significativos. La marcada predominancia del sector manufacturero sugiere que Empalme es un importante centro industrial en la región."
        },
        {
            "file": "Dona_Ingresos_Guaymas.png", 
            "title": "Ingresos Económicos Guaymas",
            "description": "La economía de Guaymas presenta una diversificación notable, con ingresos totales que ascienden a 38,126 millones de pesos. Este robusto panorama económico se sustenta en cuatro pilares fundamentales: el comercio mayorista, que emerge como el sector dominante con una participación del 30.2% y una contribución de 11,528 millones; seguido por un versátil segmento de otros que aporta el 24.1% de los ingresos. El comercio minorista y la manufactura completan este cuadro económico, representando el 23.7% y 22% respectivamente, lo que subraya una estructura equilibrada que combina la fuerza del comercio con una base industrial significativa. Esta distribución refleja una economía local dinámica y diversa, capaz de adaptarse a las fluctuaciones del mercado y sostener el crecimiento a través de múltiples canales."
        },
        {
            "file": "Dona_Ingresos_San_Ignacio_Rio_Muerto.png", 
            "title": "Ingresos Económicos San Ignacio Río Muerto",
            "description": "En San Ignacio Río Muerto, con ingresos totales de 1,311 millones de pesos, se caracteriza por una marcada especialización en el sector agropecuario y agroindustrial, que domina con un impresionante 68.1% de participación y 893 millones en ingresos. Este robusto pilar se complementa con un sector comercial diversificado, donde el comercio minorista destaca con un 19% y 250 millones, seguido por el mayorista con 8.1% y 106 millones. La estructura económica se completa con otras actividades que, aunque minoritarias con un 4.8%, aportan 63 millones, reflejando así una economía local agrícola. "
        }
    ]

# Mostrar los gráficos de dona con descripciones y separadores
    for image in dona_images:
        image_path = os.path.join(base_path, image["file"])
        st.markdown(f"<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>{image['title']}</h3>", unsafe_allow_html=True)
        st.image(image_path, caption=image["title"], use_column_width=True)
        st.markdown(
            f"""
            <div style="background-color: #f0f8ff; border-left: 5px solid #1B2F54; padding: 15px; margin-top: 20px; font-size: 14px; color: #333;">
            {image["description"]}
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("<hr style='border:1px solid #688C98;'>", unsafe_allow_html=True)


#SECCIÓN ANALISIS GEOGRAFICO 

#Función para reporducir los gifs
def gif_to_html(gif_path):
    with open(gif_path, "rb") as file:
        contents = file.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    return f'<img src="data:image/gif;base64,{data_url}" alt="GIF animado" style="width: 100%;">'

#SECCIÓN COBERTURA DEL SUELO
if st.session_state.navigation == '🌿 Cobertura del Suelo':
    st.markdown("<h2 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54;'>Evolución de la Cobertura del Suelo en la Cuenca del Río Yaqui</h2>", unsafe_allow_html=True)

    # Intentar usar toggle_switch, si falla, usar st.checkbox con estilo personalizado
    try:show_gif = toggle_switch(
        label="Mostrar GIF animado",
        #default_value=False,
        #label_after=True,
        #inactive_color="#BFC0A6",
        #active_color="#83DADD",
        #track_color="#3279C1",
        #label_style={'color': 'blue', 'font-weight': 'bold'}  # Estilo para texto negro y negrita
    )
    except:
        show_gif = st.checkbox("**Mostrar GIF animado**")


    # Primera imagen/GIF y texto
    if show_gif:
        gif_html = gif_to_html("geografico/dinamico.gif")
        st.markdown(gif_html, unsafe_allow_html=True)
    else:
        st.image("geografico/landcover_sub.png", use_column_width=True)

    st.markdown(
        """
        <div style="font-size: 14px; color: #333; margin-top: 20px; margin-bottom: 20px;">
        Este mapa físico muestra la cobertura del terreno en la región del Río Yaqui en Sonora, México, destacando las distintas clases de uso del suelo para el periodo 2023-2024. Se ilustran las principales características geográficas que influencian el flujo y la distribución del agua en la cuenca, como elevaciones, depresiones y tipos de vegetación. Las diferentes clases de uso del suelo, representadas por colores distintos, incluyen arbustos, cultivos, árboles, suelo expuesto, agua, construcciones y pasto. Este análisis proporciona una visión detallada de cómo el terreno y su uso impactan la gestión del agua en la cuenca.
        La animación muestra la cobertura del terreno en la región del Río Yaqui desde 2015 hasta 2024. Esta visualización dinámica permite observar los cambios en el uso del suelo a lo largo del tiempo, destacando las variaciones en la distribución de agua, vegetación y áreas urbanas en la cuenca. Es una herramienta valiosa para entender cómo los diferentes factores geográficos y climáticos han influido en la evolución del paisaje en esta región.
        </div>
        """, unsafe_allow_html=True
    )

    if show_gif:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("geografico/serie_de_tiempo.png", use_column_width=True)
        with col2:
            st.markdown("<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Cobertura por clase (%) 2015 - 2024</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size: 14px; color: #333;">
                Este gráfico muestra la evolución de la cobertura de diferentes clases de uso del suelo en la región del Río Yaqui desde 2015 hasta 2024. Permite observar tendencias y cambios en la distribución de tipos de terreno a lo largo del tiempo, proporcionando insights sobre los patrones de cambio en el uso del suelo y sus implicaciones para la gestión del agua en la cuenca.
                </div>
                """, unsafe_allow_html=True
            )
    else:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("geografico/cobertura_promedio.png", use_column_width=True)
        with col2:
            st.markdown("<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Cobertura promedio 2023-2024</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size: 14px; color: #333;">
                Este gráfico de barras ilustra la distribución promedio de las diferentes clases de cobertura del suelo en la región del Río Yaqui para el periodo 2023-2024. Proporciona una visión clara de la proporción de cada tipo de uso del suelo, permitiendo una comprensión rápida de la composición del paisaje en la cuenca y sus implicaciones para la gestión del agua.
                </div>
                """, unsafe_allow_html=True
            )
#SECCIÓN CLASIFICACIÓN HISTORICA
elif st.session_state.navigation == '🏞️ Clasificación histórica':
    st.markdown("<h2 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54;'>Clasificación histórica de la Cobertura del Suelo</h2>", unsafe_allow_html=True)
# Código existente para Cobertura del Suelo
    # Intentar usar toggle_switch, si falla, usar st.checkbox con estilo personalizado
    try:
        show_gif = toggle_switch(
            label="Mostrar GIF animado",
            default_value=False,
            label_after=True,
            inactive_color="#BFC0A6",
            active_color="#83DADD",
            track_color="#3279C1"
        )
    except:
        show_gif = st.checkbox("Mostrar GIF animado")

    # Primera imagen/GIF y texto
    if show_gif:
        gif_html = gif_to_html("geografico/jrc_waterg.gif")
        st.markdown(gif_html, unsafe_allow_html=True)
    else:
        st.image("geografico/jrc_water.png", use_column_width=True)

    st.markdown(
        """
        <div style="font-size: 14px; color: #333; margin-top: 20px; margin-bottom: 20px;">
        Este mapa muestra la clasificación histórica del agua en la región del Río Yaqui en Sonora, México, para el año 1992. Se destacan tres clases principales: sequía, agua estacional y agua permanente, representadas por colores distintos. El mapa proporciona una visión detallada de la distribución del agua en la cuenca durante este periodo, ayudando a entender las variaciones temporales y espaciales en los recursos hídricos de la región. Estas clasificaciones son esenciales para analizar los cambios a lo largo del tiempo y planificar la gestión sostenible del agua.
        </div>
        """, unsafe_allow_html=True
    )

    if show_gif:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("geografico/jrc_serie.png", use_column_width=True)
        with col2:
            st.markdown("<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Serie de Tiempo</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size: 14px; color: #333;">
                La evolución del área de las diferentes clases de agua en la región del Río Yaqui desde 1992 hasta 2021. Las tres categorías representadas son agua estacional, agua permanente y sequía, con sus respectivas áreas medidas en kilómetros cuadrados. El análisis temporal permite observar cómo han cambiado las áreas de estas clases de agua a lo largo del tiempo, proporcionando una visión detallada de las tendencias y patrones en la disponibilidad de agua en la cuenca.
                </div>
                """, unsafe_allow_html=True
            )
    else:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("geografico/jrc_area.png", use_column_width=True)
        with col2:
            st.markdown("<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Área</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size: 14px; color: #333;">
                Este gráfico de barras ilustra la distribución del área de las diferentes clases de agua en la región del Río Yaqui. Se representan tres categorías: agua estacional, agua permanente y sequía, con áreas de 343.1 km², 208.1 km² y 154.3 km² respectivamente. Este análisis proporciona una visión clara de la extensión de cada tipo de cobertura de agua en la región, lo que es crucial para entender la disponibilidad y gestión de los recursos hídricos.
                </div>
                """, unsafe_allow_html=True
            )


elif st.session_state.navigation == '💨 Evapotranspiración':
    st.markdown("<h2 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54;'>Análisis de Evapotranspiración</h2>", unsafe_allow_html=True)
   
    # Estilo personalizado con !important para forzar el color negro
    st.markdown("""
        <style>
        .stCheckbox, .stCheckbox > label, .css-1wivap2, .css-1wivap2 > label {
            color: black !important;
            font-weight: bold !important;
        }
        </style>
    """, unsafe_allow_html=True)
   
    # Usar solo st.checkbox con estilo forzado a negro
    show_gif = st.checkbox("Mostrar GIF animado", key="show_gif_checkbox")

    # Primera imagen/GIF y texto
    if show_gif:
        gif_html = gif_to_html("geografico/annual_g.gif")
        st.markdown(gif_html, unsafe_allow_html=True)
    else:
        st.image("geografico/annual_Subcuencasg.png", use_column_width=True)
   
    # ... (resto del código sin cambios)
    st.markdown(
        """
        <div style="font-size: 14px; color: #333; margin-top: 20px; margin-bottom: 20px;">
        Este mapa muestra la evapotranspiración anual en la región del Río Yaqui en Sonora, México. La evapotranspiración es un proceso crucial en el ciclo hidrológico que combina la evaporación del agua desde la superficie terrestre y la transpiración de las plantas. El mapa utiliza una escala de colores para representar los diferentes niveles de evapotranspiración en la cuenca, proporcionando una visión detallada de cómo varía este fenómeno en diferentes áreas de la región. Esta información es esencial para entender el balance hídrico y planificar la gestión sostenible del agua en la cuenca del Río Yaqui.
        </div>
        """, unsafe_allow_html=True
    )
    
    if show_gif:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("geografico/area_time_series.png", use_column_width=True)
        with col2:
            st.markdown("<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Serie de Tiempo</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size: 14px; color: #333;">
                Este gráfico muestra la evolución temporal de la evapotranspiración en la región del Río Yaqui. La serie de tiempo permite observar las tendencias y patrones en la evapotranspiración a lo largo de los años. Se pueden apreciar las variaciones estacionales y anuales, lo que es crucial para entender cómo los cambios climáticos y otros factores ambientales afectan la disponibilidad de agua en la cuenca. Esta información es valiosa para la planificación de recursos hídricos y la adaptación a largo plazo de las prácticas de gestión del agua en la región.
                </div>
                """, unsafe_allow_html=True
            )


elif st.session_state.navigation == '💧 Acumulaciones':
    st.markdown("<h2 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54;'>Acumulaciones de Caudales</h2>", unsafe_allow_html=True)
    
    # Mostrar la imagen del mapa
    st.image("geografico/flow.png", use_column_width=True)
   
    st.markdown(
        """
        <div style="font-size: 14px; color: #333; margin-top: 20px; margin-bottom: 20px;">
        Este mapa muestra las acumulaciones de caudales en la región del Río Yaqui en Sonora, México. Las acumulaciones de caudales son cruciales para entender cómo se distribuye y acumula el agua a lo largo de la cuenca hidrográfica. El mapa utiliza una escala de colores para representar los diferentes niveles de acumulación de agua, proporcionando una visión detallada de cómo varía este fenómeno en diferentes áreas de la región. Esta información es esencial para la gestión de recursos hídricos, la planificación de infraestructuras y la prevención de inundaciones en la cuenca del Río Yaqui.
        </div>
        """, unsafe_allow_html=True
    )
# Mostrar la imagen correspondiente
    st.image("geografico/flow2.png", caption="titulo", use_column_width=True)



# SECCIÓN LEYES 
elif st.session_state.navigation == "💦 Leyes del Agua en México":
    # Función para incrustar PDF en Streamlit
    def show_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    # Mostrar título y descripción
    st.markdown("<h2 style='font-family: Arial, sans-serif; font-size: 24px; color: #1B2F54;'>Leyes de Protección del Agua en México</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="font-size: 14px; color: #333; margin-top: 20px; margin-bottom: 20px;">
        Aquí encontrarás una recopilación de las leyes y regulaciones más importantes relacionadas con la protección del agua en México. Estos documentos son fundamentales para entender el marco legal que rige la gestión y conservación de los recursos hídricos en el país.
        </div>
        """, unsafe_allow_html=True
    )

    # Ruta al archivo Excel
    excel_path = "proteccion_leyes/Leyes.xlsx"

    # Verificar si el archivo existe y leerlo
    if os.path.exists(excel_path):
        df_excel = pd.read_excel(excel_path)
        st.markdown("<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54;'>Resumen de Leyes</h3>", unsafe_allow_html=True)

        gb = GridOptionsBuilder.from_dataframe(df_excel)
        gb.configure_default_column(cellStyle={'color': '#333', 'backgroundColor': '#FFFFFF'})
        gb.configure_column("Ley/ Norma/ Constitución/ Programas", headerStyle={'fontWeight': 'bold', 'color': '#1B2F54'})
        gb.configure_column("Artículo", headerStyle={'fontWeight': 'bold', 'color': '#1B2F54'})
        gb.configure_column("¿Qué establece?", headerStyle={'fontWeight': 'bold', 'color': '#1B2F54'})
        gb.configure_column("Link", headerStyle={'fontWeight': 'bold', 'color': '#1B2F54'})
        gridOptions = gb.build()

        AgGrid(df_excel, 
               gridOptions=gridOptions, 
               theme='streamlit', 
               custom_css={
                   ".ag-header-cell-label": {"color": "#1B2F54 !important"},
                   ".ag-header": {"background-color": "#f0f8ff !important"},
                   ".ag-row-even": {"background-color": "#ffffff !important"},
                   ".ag-row-odd": {"background-color": "#f0f8ff !important"}
               })
    else:
        st.error(f"Error al leer el archivo Excel: {excel_path} no se encontró.")

    # Mostrar PDFs
    st.markdown("<h3 style='font-family: Arial, sans-serif; font-size: 20px; color: #1B2F54; margin-top: 40px;'>Documentos en PDF</h3>", unsafe_allow_html=True)
    pdf_folder = "proteccion_leyes"
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        with st.expander(f"{pdf_file}", expanded=False):
            st.markdown(f"<h4 style='font-family: Arial, sans-serif; font-size: 16px; color: #1B2F54;'>{pdf_file}</h4>", unsafe_allow_html=True)
            show_pdf(os.path.join(pdf_folder, pdf_file))

    st.markdown("<hr style='border:1px solid #688C98;'>", unsafe_allow_html=True)



# Sección Contacto
st.sidebar.markdown("<h3 style='color: white; font-family: Arial, sans-serif;'>Contacto</h3>", unsafe_allow_html=True)

# Estilo para los enlaces de correo
email_style = """
    color: white;
    text-decoration: none;
    font-family: Arial, sans-serif;
    font-size: 14px;
    display: block;
    margin-bottom: 5px;
"""

st.sidebar.markdown(
    f"""
    <div>
        <a href="mailto:tech@tecnicasrudas.org" style="{email_style}">
            <i class="fas fa-envelope"></i> tech@tecnicasrudas.org
        </a>
        <a href="mailto:hello@diversa.studio" style="{email_style}">
            <i class="fas fa-envelope"></i> hello@diversa.studio
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Separador
st.sidebar.markdown("<hr style='border:3 px;'>", unsafe_allow_html=True)

# Logos
st.sidebar.markdown("<h4 style='color: white; font-family: Arial, sans-serif; text-align: center;'></h4>", unsafe_allow_html=True)

# Contenedor para los logos
logo_container = st.sidebar.container()

# Función para centrar y redimensionar logos
def centered_logo(file_path, width=150):
    col1, col2, col3 = logo_container.columns([1, 2, 1])
    with col2:
        logo = Image.open(file_path)
        st.image(logo, width=width, use_column_width=True)

# Logo Yaqui centrado y más grande
centered_logo("logos/yaqui.png")

# Dos logos en la misma línea, centrados
col1, col2 = logo_container.columns(2)
with col1:
    logo1 = Image.open("logos/logo1.png")
    st.image(logo1, width=100, use_column_width=True)
with col2:
    logo2 = Image.open("logos/logo2.png")
    st.image(logo2, width=100, use_column_width=True)
# Texto "Con el apoyo de" en blanco y tercer logo comentados
#logo_container.markdown("<div style='text-align: center; margin: 20px 0; color: white;'>Con el apoyo de</div>", unsafe_allow_html=True)
#centered_logo("logos/logo3.png")