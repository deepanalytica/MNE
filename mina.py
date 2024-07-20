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

    # Unir datos de ensayos y litología
    gdf = gdf.merge(assay, on='BHID').merge(litho, on='BHID')

    # ----> CORRECCIÓN: Extraer coordenadas como columnas separadas
    gdf['lat'] = gdf.geometry.y
    gdf['lon'] = gdf.geometry.x

    # Visualización de datos
    st.header("Visualización de Datos")

    # Mapa de sondajes
    st.subheader("Mapa de Sondajes")
    fig = px.scatter_mapbox(gdf, 
                        lat="lat",  # Usar las columnas 'lat' y 'lon'
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

    # Resto del código (sin cambios)
    # ... 
else:
    st.warning("Por favor, cargue todos los archivos CSV para comenzar el análisis.")
