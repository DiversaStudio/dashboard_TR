import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

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
    Este dashboard muestra datos sobre la cuenca del río Yaqui, además de datos sociodemográficos de la comunidad Yaqui de Vicam en Sonora, México.
""")
navigation = st.sidebar.radio("Navigation", ["Análisis Geográfico", "Análisis Sociodemográfico", "Leyes de Agua"])

# Filtros
st.sidebar.header("Filtro")
municipios = st.sidebar.selectbox('Municipios', ['Municipio 1', 'Municipio 2', 'Municipio 3'])
subcuencas = st.sidebar.selectbox('Subcuencas', ['Subcuenca 1', 'Subcuenca 2', 'Subcuenca 3'])

# Contenido principal basado en la selección del menú de navegación
if navigation == "Análisis Geográfico":
    col1, col2 = st.columns([2, 1])  # La primera columna será más ancha

    with col1:
        st.markdown("<h2 style='color: #000000;'>Mapa Dinamic World Sonora</h2>", unsafe_allow_html=True)
        st.image("mapas/dw_5municipios.png", use_column_width=True)

    with col2:
        st.markdown(
            f"""
            <div style="color: {colors['text_color']};">
                Este mapa muestra la cobertura del suelo en cinco municipios de la región de Sonora.
                Los colores representan diferentes tipos de cobertura del suelo, como áreas urbanas, vegetación, cuerpos de agua y áreas agrícolas.
                Esta información es crucial para la gestión de recursos naturales y la planificación territorial en la región.
            </div>
            """, unsafe_allow_html=True
        )

elif navigation == "Análisis Sociodemográfico":
    col1, col2 = st.columns([2, 1])  # La primera columna será más ancha

    with col1:
        st.markdown("**Análisis Sociodemográfico**")

        # Datos de ejemplo para el gráfico de barras usando Altair
        data = pd.DataFrame({
            'category': ['A', 'B', 'C', 'D', 'E'],
            'values': [5, 10, 15, 20, 25]
        })

        # Crear gráfico de barras con colores personalizados usando Altair
        chart = alt.Chart(data).mark_bar().encode(
            x='category',
            y='values',
            color=alt.condition(
                alt.datum.category == 'A',  # Cambiar esta condición según lo necesario
                alt.value(colors["color1"]),  # Color para la condición
                alt.value(colors["color2"])   # Color por defecto
            )
        ).properties(
            width=600,
            height=400
        )

        # Mostrar el gráfico en Streamlit usando Altair
        st.altair_chart(chart, use_container_width=True)

    with col2:
        st.markdown(
            f"""
            <div style="color: {colors['text_color']};">
                Este dashboard muestra datos sobre la cuenca del río Yaqui, además 
                datos sociodemográficos de la comunidad Yaqui de Vícam en Sonora México.
            </div>
            """, unsafe_allow_html=True
        )

elif navigation == "Leyes de Agua":
    st.markdown("### Leyes de Agua", unsafe_allow_html=True)
    st.markdown(
        """
        Aquí se presentan las leyes y regulaciones sobre el uso y la gestión del agua en la región de Sonora.
        **Ley 1: Ley General de Aguas**
        - Descripción de la ley y su impacto en la gestión del agua.

        **Ley 2: Reglamento de Uso de Aguas Nacionales**
        - Descripción del reglamento y cómo afecta a los usuarios del agua.

        **Ley 3: Normas Oficiales Mexicanas (NOM)**
        - Detalles sobre las normas y regulaciones específicas relacionadas con la calidad y uso del agua.
        """
    )

# Para ejecutar la aplicación de Streamlit, guarda este script como streamlit_app.py y ejecuta `streamlit run streamlit_app.py` desde tu terminal.
