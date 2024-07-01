import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Proyecto Minero", layout="wide")
st.title("Planificación Proyecto Minero")

# Datos del Gantt 
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
        "2024-01-08", "2024-01-11", "2024-01-15", "2024-01-22", "2024-03-11", "2024-03-18"
    ],
    "Fin": [
        "2024-01-10", "2024-01-15", "2024-02-22", "2024-03-29", "2024-03-20", "2024-07-29"
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
    "Personal": ["Jefe de Operaciones", "Supervisor", "Minero (x4)", "Ayudante (x4)", "Mecánico", "Guardia (x2)", "Bodeguero"]
}

# --- SIDEBAR ---
# ... (Código del sidebar igual que antes)

# --- MAIN PAGE --- 
# ... (Código de Etapas del Proyecto igual que antes)

# --- DIAGRAMA DE GANTT ---
st.header("4. Diagrama de Gantt")

# Crear figura Gantt con escala de tiempo
fig = px.timeline(df_gantt, x_start="Inicio", x_end="Fin", y="Tarea", color="Recursos",
                  title="Cronograma del Proyecto")

# Ajustar escala del eje X (tiempo)
fig.update_xaxes(
    type='date',
    tickformat="%d/%m/%Y",  # Formato de las etiquetas del eje X
    dtick="M1",             # Mostrar marcas cada mes 
    range=["2024-01-01", "2024-08-31"]  # Ajusta el rango de fechas según tu proyecto 
)

fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

# --- RECURSOS DEL PROYECTO ---
# ... (Código de Recursos del Proyecto igual que antes)

# --- PRESUPUESTO Y COSTOS ---
# ... (Código de Presupuesto y Costos igual que antes)

# --- CONSIDERACIONES ADICIONALES ---
# ... (Código de Consideraciones Adicionales igual que antes)
