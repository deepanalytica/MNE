import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata

# --- Parámetros de la Visualización ---
LONGITUD_SONDAJE = 100  # Ajusta según la escala que desees
DIAMETRO_SONDAJE = 5  # Diámetro de los cilindros que representan los sondajes

# --- Leer y Procesar Datos ---
@st.cache_data  # Cachear los datos para mayor velocidad
def cargar_datos(archivo_datos):
    df = pd.read_excel(archivo_datos, skiprows=7)
    df = df.rename(columns={'DESCRIPTION': 'Norte', 'Norte': 'Este'})
    df['Norte'] = df['Norte'].str.replace('.', '').astype(float)
    df['Este'] = df['Este'].str.replace('.', '').astype(float)

    # Reemplazar "<0.005" y valores similares con 0 para evitar errores
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(0)
    return df

uploaded_file = st.file_uploader("Cargar archivo Excel", type=['xlsx'])
if uploaded_file is not None:
    df_sondajes = cargar_datos(uploaded_file)

    # --- Interfaz de usuario de Streamlit ---
    st.sidebar.title("Visualización de Sondajes 3D")

    # --- Opciones de visualización ---
    st.sidebar.header("Opciones de Visualización")
    ley_a_visualizar = st.sidebar.selectbox("Seleccionar Ley Mineral:",
                                            df_sondajes.columns[3:])  # Excluye las primeras 3 columnas
    mostrar_sondajes = st.sidebar.checkbox("Mostrar Sondajes", value=True)

    # --- Visualización ---
    st.title("Visualización 3D de Sondajes")

    # --- Gráfico 3D ---
    fig = go.Figure()

    # --- Añadir Sondajes al Gráfico ---
    if mostrar_sondajes:
        for i in range(len(df_sondajes)):
            fila = df_sondajes.iloc[i]
            x0, y0 = fila['Este'], fila['Norte']  # Coordenadas iniciales del sondaje
            z0 = 0  # Los sondajes comienzan en z=0

            # Crear un cilindro para representar el sondaje
            fig.add_trace(go.Cylinder(
                x0=x0, y0=y0, z0=z0,
                x1=x0, y1=y0, z1=z0 + LONGITUD_SONDAJE,
                radius=DIAMETRO_SONDAJE,
                colorscale='YlOrRd',  # Escala de colores amarillo-rojo
                intensity=[fila[ley_a_visualizar]],  # Valor de la ley para el color
                showscale=False,
                hovertext=f"{ley_a_visualizar}: {fila[ley_a_visualizar]}",
            ))

    # --- Ajustes del Gráfico ---
    fig.update_layout(
        scene=dict(
            xaxis_title="Este (m)",
            yaxis_title="Norte (m)",
            zaxis_title="Profundidad (m)",
            aspectmode='data'  # Ajusta la relación de aspecto para evitar deformaciones
        ),
        width=800,
        height=800,
        margin=dict(r=20, l=10, b=10, t=10)
    )

    st.plotly_chart(fig)
