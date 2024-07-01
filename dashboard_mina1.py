import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Proyecto Minero", layout="wide")
st.title("Planificación Proyecto Minero")

# Datos del Proyecto
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
        "Día 1", "Día 4", "Día 8", "Día 15", "Día 46", "Día 52"
    ],
    "Fin": [
        "Día 3", "Día 7", "Día 45", "Día 84", "Día 51", "Día 150" # Ejemplo de fin de proyecto
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

# Convertir las columnas "Inicio" y "Fin" a datetime
df_gantt["Inicio"] = pd.to_datetime(df_gantt["Inicio"], format="Día %d")
df_gantt["Fin"] = pd.to_datetime(df_gantt["Fin"], format="Día %d")

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
st.header("Diagrama de Gantt")
fig = px.timeline(df_gantt, x_start="Inicio", x_end="Fin", y="Tarea", color="Recursos",
                  title="Cronograma del Proyecto")
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

st.header("Recursos del Proyecto")
for categoria, items in recursos.items():
    st.subheader(categoria)
    for item in items:
        st.markdown(f"- {item}")

st.header("Presupuesto y Costos")
st.warning("Para visualizar el presupuesto y costos, por favor proporciona la información detallada de costos de mano de obra, materiales, combustibles, arriendos, seguros, etc.")
st.markdown("Puedes subir un archivo CSV con la información o utilizar la librería `pandas` para crear un DataFrame directamente en el código.")
