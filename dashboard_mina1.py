import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Proyecto Minero", layout="wide")
st.title("Planificación Proyecto Minero")

# Datos del Gantt (Asegúrate de que estas fechas tengan sentido para tu proyecto)
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
st.sidebar.title("Resumen del Proyecto")

st.sidebar.markdown("**Descripción:**")
st.sidebar.write(
    "Este proyecto minero consiste en la habilitación de un nuevo punto de extracción "
    "de mineral. Se requiere la construcción de caminos de acceso, instalación de "
    "faena, saneamiento de un pique existente, construcción de un nuevo túnel "
    "de producción y la posterior explotación del yacimiento."
)

st.sidebar.markdown("**Subcontratos:**")
st.sidebar.markdown("- Empresa de obras menores (Instalación de faena)")
st.sidebar.markdown("- Empresa proveedora de explosivos")

# --- MAIN PAGE ---

st.header("1. Etapas del Proyecto")
st.write("**Etapa 1: Preparación (7 días)**")
st.write("- Día 1-3: Construcción de caminos de acceso.")
st.write("- Día 4-7: Instalación de faena (Subcontrato a empresa de Obras Menores).")

st.write("**Etapa 2: Exploración y Preparación (38 días)**")
st.write("- Día 8 - 45: Saneamiento de pique (38 días, considerando los domingos).")
st.write("- Día 15 - 84: Construcción del túnel principal de producción (70 días, en paralelo al saneamiento del pique).")
st.write("- Día 46 - 51: Habilitación nivel de exploración (6 días hábiles, considerando sábado).")

st.write("**Etapa 3: Producción (En curso)**")
st.write("- Día 52 - Fin del proyecto: Inicio de la producción.")

# --- DIAGRAMA DE GANTT ---
st.header("4. Diagrama de Gantt")
fig = px.timeline(df_gantt, x_start="Inicio", x_end="Fin", y="Tarea", color="Recursos",
                  title="Cronograma del Proyecto")
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

# --- RECURSOS DEL PROYECTO ---
st.header("2. Recursos")
for categoria, items in recursos.items():
    st.subheader(categoria)
    for item in items:
        st.markdown(f"- {item}")

# --- PRESUPUESTO Y COSTOS ---
st.header("5. Presupuesto")
st.warning("Se necesita información detallada sobre costos de mano de obra, materiales, combustibles, arriendos, seguros, etc. para elaborar un presupuesto preciso.")
st.markdown("Puedes subir un archivo CSV con la información o utilizar la librería `pandas` para crear un DataFrame directamente en el código.")

# --- CONSIDERACIONES ADICIONALES ---
st.header("6. Consideraciones Adicionales")
st.markdown("- **Seguridad y salud ocupacional:** Implementar un plan de seguridad y salud ocupacional para prevenir accidentes y enfermedades profesionales.")
st.markdown("- **Medio ambiente:** Cumplir con la normativa ambiental vigente y minimizar el impacto del proyecto sobre el entorno.")
st.markdown("- **Relaciones comunitarias:** Mantener una comunicación fluida y transparente con las comunidades cercanas al proyecto.")
