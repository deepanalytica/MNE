import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from io import StringIO
import geopandas as gpd
from shapely.geometry import Point

# Título de la aplicación
st.title("Exploración Aurífera en Cerro Pillay")

# Descripción de la aplicación
st.write("Esta aplicación permite analizar datos de exploración y visualizar el potencial aurífero del yacimiento Cerro Pillay.")

# Subir archivos CSV
st.header("Cargar Datos")
collar_file = st.file_uploader("Archivo Collar (CSV)", type="csv")
survey_file = st.file_uploader("Archivo Survey (CSV)", type="csv")
assay_file = st.file_uploader("Archivo Ensayos (CSV)", type="csv")
litho_file = st.file_uploader("Archivo Litología (CSV)", type="csv")

# Leer archivos CSV
if collar_file and survey_file and assay_file and litho_file:
    collar = pd.read_csv(StringIO(collar_file.getvalue().decode("utf-8")))
    survey = pd.read_csv(StringIO(survey_file.getvalue().decode("utf-8")))
    assay = pd.read_csv(StringIO(assay_file.getvalue().decode("utf-8")))
    litho = pd.read_csv(StringIO(litho_file.getvalue().decode("utf-8")))

    # Combinar datos de collar y survey
    data = pd.merge(collar, survey, on='BHID')

    # Convertir coordenadas a GeoDataFrame (para otros usos)
    geometry = [Point(xy) for xy in zip(data['XCOLLARWGS84'], data['YCOLLARWGS84'])]
    gdf = gpd.GeoDataFrame(data, geometry=geometry)

    # Unir datos de ensayos y litología, reiniciando el índice
    gdf = gdf.merge(assay, on='BHID').reset_index(drop=True)
    gdf = gdf.merge(litho, on='BHID').reset_index(drop=True)

    # Extraer coordenadas como columnas separadas
    gdf['lat'] = gdf.geometry.y
    gdf['lon'] = gdf.geometry.x

    # Reemplazar '<0.005' por 0.0025 y convertir a numérico
    gdf['Au'] = gdf['Au'].replace('<0.005', 0.0025)
    gdf['Au'] = pd.to_numeric(gdf['Au'])

    # Visualización de datos
    st.header("Visualización de Datos")

    # Mapa de sondajes
    st.subheader("Mapa de Sondajes")
    fig = px.scatter_mapbox(gdf, 
                        lat="lat", 
                        lon="lon",
                        color="Au", 
                        size="maxdepth",
                        hover_name="BHID", 
                        hover_data=["FROM", "TO", "LITHO"],
                        color_continuous_scale="Viridis", 
                        zoom=12, 
                        height=600)
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)

    # Gráficos de secciones transversales
    st.subheader("Secciones Transversales")
    selected_bhid = st.selectbox("Seleccionar Sondaje", gdf['BHID'].unique())
    section_data = gdf[gdf['BHID'] == selected_bhid]
    fig = px.scatter(section_data, x="AT", y="Au", color="LITHO", title=f"Sección Transversal {selected_bhid}")
    st.plotly_chart(fig)

    # Análisis estadístico
    st.header("Análisis Estadístico")
    st.write(gdf.describe())

    # Correlaciones multi-elemento
    st.subheader("Correlaciones Multi-elemento")
    selected_elements = st.multiselect("Seleccionar Elementos", gdf.columns)
    if len(selected_elements) > 1:
        fig = px.scatter_matrix(gdf, dimensions=selected_elements, color="LITHO", title="Matriz de Correlación")
        st.plotly_chart(fig)

    # Próximos pasos
    st.header("Próximos Pasos")
    st.write(
        """
        * **Mapeo geológico detallado:** Complementar el mapeo existente.
        * **Muestreo geoquímico sistemático:** Ampliar el muestreo.
        * **Sondajes adicionales:** Planificar y ejecutar sondajes.
        * **Estudios geofísicos:** Considerar magnetometría, IP, etc.
        """
    )

else:
    st.warning("Por favor, cargue todos los archivos CSV para comenzar el análisis.")
