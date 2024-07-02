import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- Cargar datos desde el texto (copiado y pegado) ---
@st.cache_data 
def cargar_datos_desde_texto(texto):
    """Procesa el texto pegado y lo convierte en un DataFrame."""
    from io import StringIO
    data = StringIO(texto)
    df = pd.read_csv(data, sep="\t")  # Asumiendo que los datos están separados por tabulaciones

    # Reemplazar "<0.005" con 0 para evitar errores de tipo
    df = df.replace("<0.005", 0)
    df = df.replace("<0.002", 0)
    df = df.replace("<0.02", 0)

    # Convertir las columnas de leyes a numéricas
    for col in df.columns[2:]:  # Excluir "SAMPLE" y "DESCRIPTION"
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

# --- Interfaz de usuario de Streamlit ---
st.sidebar.title("Visualización de Muestras 3D")

# --- Pegar datos ---
texto_datos = st.sidebar.text_area("Pega los datos aquí:", height=200)

if texto_datos:
    df_muestras = cargar_datos_desde_texto(texto_datos)

    # --- Opciones de visualización ---
    st.sidebar.header("Opciones de Visualización")
    ley_a_visualizar = st.sidebar.selectbox("Seleccionar Ley:", df_muestras.columns[2:])

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
                x=[row["Norte"], row["Norte"] + longitud_sondaje],  # Usando "Norte" como coordenada X
                y=[row["Norte.1"], row["Norte.1"]],  # Usando "Norte.1" como coordenada Y
                z=[0, 0],  # Asumiendo que los sondajes están a la misma elevación
                mode="lines+markers",
                line=dict(width=5, color=row[ley_a_visualizar], colorscale="Viridis"),
                marker=dict(size=8, color=row[ley_a_visualizar], colorscale="Viridis"),
                hovertext=f"Muestra: {row['SAMPLE']}<br>{ley_a_visualizar}: {row[ley_a_visualizar]}",
                showlegend=False,
            )
        )

    # Configuración del gráfico
    fig.update_layout(
        scene=dict(
            xaxis_title="Norte",  # Ajustar el título del eje X
            yaxis_title="Norte.1",  # Ajustar el título del eje Y
            zaxis_title="Elevación",
            aspectmode='data'  # Ajusta la relación de aspecto
        ),
        margin=dict(l=0, r=0, b=0, t=0)  # Eliminar márgenes
    )

    st.plotly_chart(fig)
else:
    st.warning("Por favor, pega los datos en el área de texto.")
