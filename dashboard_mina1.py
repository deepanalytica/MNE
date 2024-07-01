import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image  # Para cargar imágenes

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Dashboard Proyecto Minero", 
    layout="wide",
    initial_sidebar_state="expanded"  # Mostrar sidebar expandido al inicio
)

# --- ESTILOS CSS PARA MEJORAR UI ---
st.markdown("""
<style>
.titulo {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
}
.subtitulo {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}
.recuadro {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- DATOS DEL PROYECTO ---

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
        "2 Mineros, 2 Ayudantes\n(4 Mineros, 4 Ayudantes\na partir del día 46)",
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
st.sidebar.title("Dashboard del Proyecto Minero")
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
st.markdown('<p class="titulo">Planificación y Control del Proyecto Minero</p>', unsafe_allow_html=True)

# --- ETAPAS DEL PROYECTO ---
st.markdown('<p class="subtitulo">1. Etapas del Proyecto</p>', unsafe_allow_html=True)
st.markdown('<div class="recuadro">', unsafe_allow_html=True)
st.write("**Etapa 1: Preparación (7 días)**")
st.write("- Día 1-3: Construcción de caminos de acceso.")
st.write("- Día 4-7: Instalación de faena (Subcontrato a empresa de Obras Menores).")
st.write("**Etapa 2: Exploración y Preparación (38 días)**")
st.write("- Día 8 - 45: Saneamiento de pique (38 días, considerando los domingos).")
st.write("- Día 15 - 84: Construcción del túnel principal de producción (70 días, en paralelo al saneamiento del pique).")
st.write("- Día 46 - 51: Habilitación nivel de exploración (6 días hábiles, considerando sábado).")
st.write("**Etapa 3: Producción (En curso)**")
st.write("- Día 52 - Fin del proyecto: Inicio de la producción.")
st.markdown('</div>', unsafe_allow_html=True)

# --- DIAGRAMA DE GANTT ---
st.markdown('<p class="subtitulo">4. Diagrama de Gantt</p>', unsafe_allow_html=True)
st.markdown('<div class="recuadro">', unsafe_allow_html=True)
fig = px.timeline(df_gantt, x_start="Inicio", x_end="Fin", y="Tarea", color="Recursos",
                  title="Cronograma del Proyecto")
fig.update_xaxes(
    type='date',
    tickformat="%d/%m/%Y", 
    dtick="M1",              
    range=["2024-09-25", "2025-05-10"], # Rango ajustado para mostrar desde octubre
    showgrid=True, gridwidth=1, gridcolor='lightgray' # Agregar grilla al eje X
)
fig.update_yaxes(autorange="reversed")
fig.update_layout(
    xaxis_title="Fecha",
    yaxis_title="Tarea",
    font=dict(family="Arial", size=14),
    title_x=0.5  # Centrar el título del gráfico
)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- RECURSOS DEL PROYECTO ---
st.markdown('<p class="subtitulo">2. Recursos</p>', unsafe_allow_html=True)
st.markdown('<div class="recuadro">', unsafe_allow_html=True)
for categoria, items in recursos.items():
    st.subheader(categoria)
    for item in items:
        st.markdown(f"- {item}")
st.markdown('</div>', unsafe_allow_html=True)

# --- ORGANIGRAMA ---
st.markdown('<p class="subtitulo">Organigrama del Proyecto</p>', unsafe_allow_html=True)
st.markdown('<div class="recuadro">', unsafe_allow_html=True)

# Cargar imagen del organigrama
imagen_organigrama = Image.open("organigrama.png") # Reemplaza "organigrama.png" con la ruta de tu imagen

# Mostrar imagen 
st.image(imagen_organigrama, caption='Organigrama del Proyecto', use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PRESUPUESTO Y COSTOS ---
st.markdown('<p class="subtitulo">5. Presupuesto</p>', unsafe_allow_html=True)
st.markdown('<div class="recuadro">', unsafe_allow_html=True)
st.warning("Se necesita información detallada sobre costos de mano de obra, materiales, combustibles, arriendos, seguros, etc. para elaborar un presupuesto preciso.")
st.markdown("Puedes subir un archivo CSV con la información o utilizar la librería `pandas` para crear un DataFrame directamente en el código.")
st.markdown('</div>', unsafe_allow_html=True)

# --- CONSIDERACIONES ADICIONALES ---
st.markdown('<p class="subtitulo">6. Consideraciones Adicionales</p>', unsafe_allow_html=True)
st.markdown('<div class="recuadro">', unsafe_allow_html=True)
st.markdown("- **Seguridad y salud ocupacional:** Implementar un plan de seguridad y salud ocupacional para prevenir accidentes y enfermedades profesionales.")
st.markdown("- **Medio ambiente:** Cumplir con la normativa ambiental vigente y minimizar el impacto del proyecto sobre el entorno.")
st.markdown("- **Relaciones comunitarias:** Mantener una comunicación fluida y transparente con las comunidades cercanas al proyecto.")
st.markdown('</div>', unsafe_allow_html=True)
