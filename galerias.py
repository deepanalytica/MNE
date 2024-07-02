import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- Cargar datos desde el archivo Excel ---
@st.cache_data 
def cargar_datos(archivo_excel):
    """Carga los datos del archivo Excel y realiza un procesamiento inicial."""
    df = pd.read_excel(archivo_excel, header=6)  # Saltar las primeras 6 filas del encabezado

    # Reemplazar "<0.005" con 0 para evitar errores de tipo
    df = df.replace("<0.005", 0)
    df = df.replace("<0.002", 0)
    df = df.replace(",,", 0)

    # Convertir las columnas de leyes a numéricas
    columnas_leyes = [
        "Au", "Ag", "Al", "As", "Ba", "Be", "Bi", "Ca", "Cd", "Ce",
        "Co", "Cr", "Cs", "Cu", "Fe", "Ga", "Ge", "Hf", "Hg", "In",
        "K", "La", "Li", "Mg", "Mn", "Mo", "Na", "Nb", "Ni", "P",
        "Pb", "Rb", "Re", "S", "Sb", "Sc", "Se", "Sn", "Sr", "Ta",
        "Te", "Th", "Ti", "Tl", "U", "V", "W", "Y", "Zn", "Zr"
    ]
    df[columnas_leyes] = df[columnas_leyes].apply(pd.to_numeric, errors='coerce')

    return df

# --- Subir archivo Excel ---
archivo_excel = st.sidebar.file_uploader("Cargar archivo Excel:", type=[".xls", ".xlsx"])

if archivo_excel is not None:
    df_muestras = cargar_datos(archivo_excel)

    # --- Interfaz de usuario de Streamlit ---
    st.sidebar.title("Visualización de Muestras 3D")

    # --- Opciones de visualización ---
    st.sidebar.header("Opciones de Visualización")
    ley_a_visualizar = st.sidebar.selectbox("Seleccionar Ley:", df_muestras.columns[4:])

    # --- Visualización 3D ---
    st.title("Visualización 3D de Muestras")

    # Calcular la longitud de los sondajes (asumiendo que todos tienen la misma)
    longitud_sondaje = 10  # Puedes ajustar este valor si es conocido

    # Crear la figura 3D
    fig = go.Figure()

    # Añadir cada muestra como un trazo con color según la ley
    for i, row in df_muestras.iterrows():
        fig.add_trace(
            go.Scatter3d(
                x=[row["Este"], row["Este"] + longitud_sondaje],
                y=[row["Norte"], row["Norte"]],
                z=[0, 0],  # Asumiendo que los sondajes están a la misma elevación (puedes ajustar)
                mode="lines+markers",
                line=dict(width=5, color=row[ley_a_visualizar], colorscale="Viridis"),
                marker=dict(size=8, color=row[ley_a_visualizar], colorscale="Viridis"),
                hovertext=f"Muestra: {row['DESCRIPTION']}<br>{ley_a_visualizar}: {row[ley_a_visualizar]}",
                showlegend=False,
            )
        )

    # Configuración del gráfico
    fig.update_layout(
        scene=dict(
            xaxis_title="Este",
            yaxis_title="Norte",
            zaxis_title="Elevación",
            aspectmode='data'  # Ajusta la relación de aspecto
        ),
        margin=dict(l=0, r=0, b=0, t=0)  # Eliminar márgenes
    )

    st.plotly_chart(fig)
else:
    st.warning("Por favor, carga un archivo Excel con las muestras y sus coordenadas.")
