import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Proyecto Minero", layout="wide")
st.title("Planificación Proyecto Minero")

# Datos del Gantt (Fechas actualizadas)
data_gantt = {
    "Tarea": [
        "Construcción de caminos de acceso",
        "Instalación de faena (Subcontrato)",
        "Saneamiento de pique",
        "Construcción del túnel principal",
        "Habilitación nivel de exploración",
        "Explotación y transporte de mineral"
    ],
    "Inicio": [
        "2024-10-01", "2024-10-04", "2024-10-08", "2024-10-15", "2024-11-25", "2024-12-02"
    ],
    "Fin": [
        "2024-10-03", "2024-10-08", "2024-11-15", "2024-12-24", "2024-11-29", "2025-04-02"
    ],
    "Duración (días)": [3, 4, 38, 70, 6, "-"],
    "Recursos": [
        "Maquinaria, Mano de obra",
        "Empresa de Obras Menores",
        "2 Mineros, 2 Ayudantes",
        "2 Mineros, 2 Ayudantes (4 Mineros, 4 Ayudantes a partir del día 46)",
        "4 Mineros, 4 Ayudantes",
        "4 Mineros, 4 Ayudantes"
    ]
}
df_gantt = pd.DataFrame(data_gantt)
df_gantt["Inicio"] = pd.to_datetime(df_gantt["Inicio"])
df_gantt["Fin"] = pd.to_datetime(df_gantt["Fin"])

# Recursos del Proyecto
recursos = {
    "Vehículos": ["Camioneta 4x4", "Camioneta Jefatura", "Bobcat", "Retroexcavadora"],
    "Maquinaria": ["Generador", "Compresores (x2)", "Estanque Agua Industrial (x2)", "Estanque Agua Potable"],
    "Herramientas": ["Equipos de protección personal (EPP)", "Herramientas manuales y eléctricas"],
    "Personal": ["Jefe de Operaciones", "Supervisor de Minería", "Minero (x4)", "Ayudante (x4)", "Mecánico", "Guardia (x2)", "Bodeguero"]
}

# --- SIDEBAR ---
# ... (Código del sidebar igual que antes)

# --- MAIN PAGE --- 
# ... (Código de Etapas del Proyecto igual que antes)

# --- DIAGRAMA DE GANTT ---
st.header("4. Diagrama de Gantt")

fig = px.timeline(df_gantt, x_start="Inicio", x_end="Fin", y="Tarea", color="Recursos",
                  title="Cronograma del Proyecto")

# Ajustes para una mejor visualización en móvil y escritorio
fig.update_xaxes(
    type='date',
    tickformat="%d/%b",      # Formato día/mes abreviado
    dtick="D7",              # Mostrar una marca cada 7 días (una semana)
    range=["2024-09-25", "2025-04-07"], # Rango ajustado para mejor visualización
    showgrid=True,          # Mostrar líneas de grid
    gridcolor="lightgrey", 
    gridwidth=1,
)
fig.update_yaxes(autorange="reversed")

# Ajustar el tamaño de la figura para mejor visualización
fig.update_layout(
    height=500,  # Ajusta la altura según sea necesario
    margin=dict(l=20, r=20, t=40, b=20),
)

st.plotly_chart(fig, use_container_width=True)

# --- RECURSOS DEL PROYECTO ---
# ... (Código de Recursos del Proyecto igual que antes)

# --- PRESUPUESTO Y COSTOS ---
# ... (Código de Presupuesto y Costos igual que antes)

# --- CONSIDERACIONES ADICIONALES ---
# ... (Código de Consideraciones Adicionales igual que antes)
