import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from io import StringIO

# --- Datos proporcionados ---
datos_texto = """
SAMPLE				Recvd Wt.	Au	Ag	Al	As	Ba	Be	Bi	Ca	Cd	Ce	Co	Cr	Cs	Cu	Fe	Ga	Ge	Hf	Hg	In	K	La	Li	Mg	Mn	Mo	Na	Nb	Ni	P	Pb	Rb	Re	S	Sb	Sc	Se	Sn	Sr	Ta	Te	Th	Ti	Tl	U	V	W	Y	Zn	Zr
DESCRIPTION	Norte	Norte		kg	ppm	ppm	%	ppm	ppm	ppm	ppm	%	ppm	ppm	ppm	ppm	ppm	ppm	%	ppm	ppm	ppm	ppm	ppm	%	ppm	ppm	%	ppm	ppm	%	ppm	ppm	ppm	ppm	ppm	ppm	%	ppm	ppm	ppm	ppm	ppm	ppm	ppm	ppm	%	ppm	ppm	ppm	ppm	ppm	ppm	ppm
PCG0701	6.036.774.823	232.450.406		1,98	0,005	0,4	7,69	19,4	310	0,79	0,86	0,07	0,04	70,9	1,8	11	2,79	32,7	1,36	14,1	0,09	2,2	0,07	0,111	1,52	50,4	11,4	0,21	73	42,8	1,86	2,9	1,2	100	8,3	62,8	0,015	0,12	1,02	10,6	8	8,5	33,1	0,26	0,44	10,35	0,141	0,35	3,4	66	1	8	12	64,3
PCG0702	6.036.776.830	232.451.580		2,19	0,027	1,22	6,38	372	500	0,71	6,18	0,04	0,19	61,3	3,9	18	4,15	45,9	3,47	12,75	0,12	1,7	0,364	0,136	1,9	38,2	11,7	0,23	84	521	0,58	1,8	2,1	150	13,7	71,3	0,12	0,71	5,66	9,3	13	11,2	20	0,18	2,47	9,41	0,094	0,53	4,5	71	0,9	10,2	18	50,4
PCG0703	6.036.777.814	232.452.035		2,05	<0.005	0,29	8,7	5	200	1,1	0,78	0,18	1,32	94,4	7,6	10	2,07	18	1,74	14,6	0,12	2,3	0,03	0,062	1,11	50,3	5,6	0,15	58	5,82	3,45	3,6	3,7	90	10,2	50,7	0,177	1,59	0,35	11,4	2	5,7	61	0,38	0,37	10,5	0,158	0,31	6,7	58	0,6	17,6	12	68
PCG0704	6.036.779.859	232.453.019		2,06	<0.005	0,4	8,52	6,4	150	1,05	0,74	0,15	18,35	71,6	13,8	10	2,28	46,9	1,78	13,9	0,1	2,2	0,005	0,089	0,96	36	9,4	0,16	78	9,24	2,94	3,4	4,1	60	9,6	50,9	0,171	1,45	0,43	11,3	1	4,3	45,7	0,31	0,32	9,45	0,159	0,34	18,8	59	0,7	25,5	22	64,4
PCG0705	6.036.783.571	232.455.291		2,19	<0.005	0,16	8,33	8,4	500	0,91	0,48	0,09	1,26	64,6	3,4	11	4,17	7,1	1,81	15,45	0,1	2,3	0,007	0,131	2,36	31,8	8	0,3	69	23,2	1,64	3,1	3,2	50	6	99,6	0,114	1,41	0,39	10,6	1	7,3	25,6	0,29	0,33	9,13	0,139	0,51	3,5	69	1	11,8	23	66,8
PCG0706	6.036.786.979	232.457.033		1,89	<0.005	0,23	7,42	2,6	310	0,77	0,66	0,08	3,56	53,7	5,6	14	3,26	6,4	1,39	13,2	0,07	2,1	0,016	0,085	1,84	31,8	5,5	0,24	88	211	1,62	2,5	3,5	60	7,8	81,9	0,277	0,76	0,33	10,8	1	8	30,8	0,24	0,37	8,4	0,118	0,44	9,1	77	1,2	28,6	13	59,5
PCG0707	6.036.789.782	232.459.003		1,92	0,009	0,62	7,55	12	500	0,84	4,31	0,04	3,05	58,1	9	18	3,65	5,7	5,09	15,3	0,1	2,1	0,017	0,195	2,91	34,4	4,4	0,33	90	108	0,68	2,4	3,8	60	14,1	122,5	0,12	5,09	0,29	10,2	2	10,8	16,5	0,25	2,32	6,89	0,123	0,66	3,7	74	1,4	16,3	11	58,7
PCG0708	6.036.792.735	232.461.123		1,94	0,021	0,77	6,62	11	540	0,83	4,06	0,07	0,55	56,5	21,3	19	3,76	14,2	4,85	14,2	0,11	1,9	0,008	0,113	2,58	30,4	6,4	0,34	134	52,8	0,73	2	3	60	15,9	92	0,044	4,33	0,95	9,8	5	13,8	19,4	0,27	1,79	4,09	0,104	0,49	1,8	80	1	12,8	41	58
PCG0709	6.036.795.159	232.459.533		1,57	<0.005	0,5	7,76	5,3	370	1,19	0,72	0,21	0,5	66,1	17	11	2,81	84,2	2,38	14,55	0,1	2,4	0,021	0,118	1,74	35,6	8,4	0,44	211	4,37	3,38	3,3	1,5	50	19,5	79,3	0,002	0,88	0,29	10,2	1	4,6	69	0,33	0,48	8,84	0,162	0,56	2,6	53	0,8	14	40	68
PCG0710	6.036.796.106	232.458.283		3,16	0,012	0,63	6,45	29,2	740	0,91	4,29	0,03	0,08	27,1	2,5	9	3,44	38,5	6,83	17,05	0,08	2,2	0,042	0,193	2,89	15,2	10,2	0,32	75	12,8	0,31	1,5	1,8	210	14,6	121,5	<0.002	0,2	0,42	13,2	5	11,1	9,7	0,16	2,32	9,02	0,1	0,6	1,4	86	0,8	7,5	27	67,4
PCG0711	6.036.797.318	232.456.162		1,4	<0.005	0,27	8,4	3,1	260	0,99	0,59	0,16	0,1	42,1	6,9	7	2,59	13,6	1,05	14,55	0,06	2,4	0,071	0,066	1,16	28,2	6,3	0,12	58	3,32	3,27	3	1,9	70	26,4	54,3	<0.002	0,5	0,23	10,6	1	4,3	56,3	0,3	0,25	8,85	0,138	0,34	1,4	46	0,6	10,6	32	66,3
PCG0712	6.036.797.999	232.454.875		1,68	<0.005	0,13	7,42	10	570	0,78	0,53	0,02	<0.02	45,3	0,6	9	3,59	14,3	1,82	8,26	0,1	2,3	0,043	0,071	3,18	27,6	3	0,17	53	17,9	0,2	1,8	0,9	150	5,8	109,5	<0.002	0,01	0,29	9,8	1	8,6	15,6	0,2	0,22	7,17	0,09	0,52	1	72	1,1	6,2	17	62,7
PCG0713	6.036.799.211	232.453.436		1,71	<0.005	0,19	7,49	12,4	320	0,96	1,11	0,08	0,06	39,9	3,1	7	3,95	34,8	4,62	17,1	0,08	2,3	0,012	0,188	1,65	23,6	10,2	0,21	66	6,65	1,81	2,5	3,3	160	13,7	76,4	0,004	0,03	0,45	15,6	2	7,1	39,2	0,27	0,4	13,85	0,148	0,51	1,5	79	0,8	14,3	39	61,9
PCG0714	6.036.800.044	232.451.694		2,25	<0.005	0,13	7,08	44,7	410	0,93	1,26	0,06	0,1	41,9	2,9	9	5,11	26,1	5,3	15,1	0,06	2,2	<0.005	0,102	2,01	25,1	9,8	0,23	77	25,2	1,08	2	2,1	180	10,2	85	<0.002	0,06	0,57	11,4	3	12,7	70,9	0,19	0,42	14,6	0,096	0,54	1,4	66	0,7	10	33	62
PCG0715	6.036.801.711	232.449.952		1,54	<0.005	0,07	5,74	11,8	200	0,77	0,53	0,08	<0.02	31,6	0,8	10	2,79	18,9	3,1	12,6	0,05	2	0,024	0,074	1,17	20,9	9,6	0,15	74	5,5	1,87	1,9	1	140	6,4	58,9	<0.002	0,04	0,33	8,6	1	4,4	109	0,19	0,23	8,48	0,087	0,34	0,9	52	0,6	6,8	13	49,9
"""

# --- Cargar datos desde el texto ---
@st.cache_data
def cargar_datos_desde_texto(texto):
    """Procesa el texto y lo convierte en un DataFrame."""
    data = StringIO(texto)
    df = pd.read_csv(data, sep="\t")

    # Reemplazar "<0.005" con 0 para evitar errores de tipo
    df = df.replace("<0.005", 0)
    df = df.replace("<0.002", 0)
    df = df.replace("<0.02", 0)

    # Eliminar posibles comas como separador de miles y convertir a numéricas
    for col in df.columns[2:]:  # Excluir "SAMPLE" y "DESCRIPTION"
        df[col] = df[col].str.replace(',', '', regex=True)
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

# --- Cargar el DataFrame ---
df_muestras = cargar_datos_desde_texto(datos_texto)

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
for i in range(len(df_muestras) - 1):
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
            z=[0, diferencia_z],
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
