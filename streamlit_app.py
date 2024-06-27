import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Definir los colores
colors = {
    "sidebar_bg": "#8C9584",
    "content_bg": "#CAD8D1",
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
    }}
    .css-1d391kg {{
        background-color: {colors["sidebar_bg"]};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar con título, descripción y filtros
st.sidebar.title("Gobernanza del Agua en Sonora")
st.sidebar.markdown("""
    Este dashboard muestra datos sobre la cuenca del río Yaqui, además de datos sociodemográficos de la comunidad Yaqui de Vicam en Sonora, México.
""")
st.sidebar.text_input("Filtro 1", key="filtro1")
st.sidebar.text_input("Filtro 2", key="filtro2")

# Contenido principal
st.markdown('<div class="content">', unsafe_allow_html=True)

# Datos de ejemplo
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'values': [5, 10, 15, 20, 25]
})

# Crear gráfico de barras con colores personalizados
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

# Mostrar el gráfico en Streamlit
st.altair_chart(chart, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)