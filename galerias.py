import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- Cargar datos desde el archivo Excel ---
@st.cache_data
def cargar_datos(archivo_excel):
    """Carga los datos del archivo Excel y realiza un procesamiento inicial."""
    df = pd.read_csv(archivo_excel, sep="\t")

    # Reemplazar "<0.005" con 0 para evitar errores de tipo
    df = df.replace("<0.005", 0)
    df = df.replace("<0.002", 0)
    df = df.replace("<0.02", 0)

    # Eliminar posibles comas como separador de miles y convertir a numéricas
    for col in df.columns[2:]:  # Excluir "SAMPLE" y "DESCRIPTION"
        df[col] = df[col].str.replace(',', '', regex=True)
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

# --- Subir archivo Excel ---
archivo_excel = st.sidebar.file_uploader("Cargar archivo Excel:", type=[".xls", ".xlsx", ".csv", ".txt"])

if archivo_excel is not None:
    df_muestras = cargar_datos(archivo_excel)

    # --- Interfaz de usuario de Streamlit ---
    st.sidebar.title("Visualización de Muestras 3D")

    # --- Opciones de visualización ---
    st.sidebar.header("Opciones de Visualización")
    ley_a_visualizar = st.sidebar.selectbox("Seleccionar Ley:", df_muestras.columns[2:])
    inclinacion = st.sidebar.slider("Ángulo de Inclinación (grados):", 0, 90, 45)

    # --- Visualización 3D ---
    st.title("Visualización 3D de Muestras")

    # Crear la figura 3D
    fig = go.Figure()

    # Añadir cada muestra como un trazo con color según la ley
    for i in range(len(df_muestras) - 1):  # Iterar hasta la penúltima fila
        row1 = df_muestras.iloc[i]
        row2 = df_muestras.iloc[i + 1]

        # Calcular la distancia en 2D (proyección horizontal)
        distancia_2d = np.sqrt(((row2["Norte"] - row1["Norte"]) ** 2) + ((row2["Norte.1"] - row1["Norte.1"]) ** 2))

        # Calcular la distancia 3D usando la inclinación
        inclinacion_rad = np.radians(inclinacion)
        distancia_3d = distancia_2d / np.cos(inclinacion_rad)

        # Calcular la diferencia de altura (coordenada Z)
        diferencia_z = distancia_3d * np.sin(inclinacion_rad)

        fig.add_trace(
            go.Scatter3d(
                x=[row1["Norte"], row2["Norte"]],
                y=[row1["Norte.1"], row2["Norte.1"]],
                z=[0, diferencia_z],  # Coordenada Z usando la diferencia de altura
                mode="lines+markers",
                line=dict(width=5, color=row1[ley_a_visualizar], colorscale="Viridis"),
                marker=dict(size=8, color=row1[ley_a_visualizar], colorscale="Viridis"),
                hovertext=f"Muestra: {row1['SAMPLE']}<br>{ley_a_visualizar}: {row1[ley_a_visualizar]}<br>Distancia 3D: {distancia_3d:.2f} m",
                showlegend=False,
            )
        )

    # Configuración del gráfico
    fig.update_layout(
        scene=dict(
            xaxis_title="Norte",
            yaxis_title="Norte.1",
            zaxis_title="Elevación",
            aspectmode='data'
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )

    st.plotly_chart(fig)
else:
    st.warning("Por favor, carga un archivo Excel con las muestras y sus coordenadas.")
