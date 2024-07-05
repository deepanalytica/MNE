import streamlit as st
import networkx as nx
import plotly.graph_objects as go

# --- CONFIGURACIÓN DE LA APLICACIÓN ---
st.set_page_config(
    page_title="Organigrama Interactivo",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# --- ESTILOS CSS PARA MEJORAR LA UI ---
st.markdown(
    """
    <style>
        /* ... (Estilos CSS anteriores) ... */ 
    </style>
    """,
    unsafe_allow_html=True
)

# --- DATOS DE LOS COLABORADORES ---
colaboradores = [
    # ... (Datos de los colaboradores) ... 
]

# --- CREAR ORGANIGRAMA CON PLOTLY ---
def crear_organigrama_plotly(colaboradores):
    """Crea un organigrama interactivo utilizando Plotly."""
    # ... (Código para crear el gráfico Plotly - igual que antes) ...

# --- APLICACIÓN PRINCIPAL ---
fig = crear_organigrama_plotly(colaboradores)
departamentos = {col["Nombre"]: col for col in colaboradores}

# --- Barra lateral ---
# ... (Código de la barra lateral - igual que antes) ...

# --- Mostrar el organigrama ---
st.title("Organigrama Interactivo")

# --- Insertar Font Awesome en el HTML del gráfico ---
st.components.v1.html(
    f"""
    <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body>
      {go.FigureWidget(fig).to_html(full_html=False)}
    </body>
    """,
    height=800,
)
