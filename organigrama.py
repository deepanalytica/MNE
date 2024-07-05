import streamlit as st
import graphviz as gv

# Crear el grafo del organigrama
dot = gv.Digraph(format='png')

# Configuración global de nodos
dot.attr('node', shape='box', style='rounded, filled', color='lightblue', fontname='Helvetica', fontsize='10')

# Añadir nodos
dot.node('Directorio', 'Directorio')
dot.node('GerenciaGeneral', 'Gerencia General')
dot.node('ComiteEjecutivo', 'Comité Ejecutivo')
dot.node('AsesorJuridico', 'Asesor Jurídico')
dot.node('GerSeguridadMinera', 'Gerencia de Seguridad Minera')
dot.node('GerenciaAdministrativa', 'Gerencia Administrativa')
dot.node('Administracion', 'Administración')
dot.node('Sostenibilidad', 'Sostenibilidad y Responsabilidad Social')
dot.node('Tecnologia', 'Tecnología e Innovación')
dot.node('GerenciaOperaciones', 'Gerencia de Operaciones')
dot.node('Supervisor', 'Supervisor')
dot.node('Geologia', 'Geología')
dot.node('Laboratorio', 'Laboratorio Análisis y Simulación')
dot.node('Mineros', 'Mineros')
dot.node('AyudantesMineros', 'Ayudantes de Minero')
dot.node('Bodega', 'Bodega')
dot.node('MecanicaElectricidad', 'Depto. Mecánica y Electricidad')
dot.node('Contabilidad', 'Contabilidad')
dot.node('AsistenteContabilidad', 'Asistente')
dot.node('RRHH', 'RRHH')
dot.node('AsistenteRRHH', 'Asistente')

# Añadir conexiones
dot.edges([
    ('Directorio', 'GerenciaGeneral'),
    ('GerenciaGeneral', 'ComiteEjecutivo'),
    ('ComiteEjecutivo', 'AsesorJuridico'),
    ('ComiteEjecutivo', 'GerSeguridadMinera'),
    ('ComiteEjecutivo', 'GerenciaAdministrativa'),
    ('ComiteEjecutivo', 'GerenciaOperaciones'),
    ('GerenciaAdministrativa', 'Administracion'),
    ('Administracion', 'Sostenibilidad'),
    ('Administracion', 'Tecnologia'),
    ('Administracion', 'Contabilidad'),
    ('Administracion', 'RRHH'),
    ('GerenciaOperaciones', 'Supervisor'),
    ('Supervisor', 'Geologia'),
    ('Supervisor', 'Mineros'),
    ('Supervisor', 'Bodega'),
    ('Bodega', 'MecanicaElectricidad'),
    ('Geologia', 'Laboratorio'),
    ('Mineros', 'AyudantesMineros'),
    ('Contabilidad', 'AsistenteContabilidad'),
    ('RRHH', 'AsistenteRRHH')
])

# Configurar Streamlit
st.title("Organigrama de la Empresa Minera")
st.graphviz_chart(dot)
