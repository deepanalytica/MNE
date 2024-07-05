import streamlit as st
from pyvis.network import Network
import networkx as nx

# Crear el grafo
G = nx.DiGraph()

# Información de colaboradores
colaboradores = [
    {"Nombre": "Directorio", "Funciones": "Supervisa la gestión de la empresa.", "ReportaA": "N/A"},
    {"Nombre": "Gerencia General", "Funciones": "Supervisa la operación total de la empresa y toma decisiones estratégicas.", "ReportaA": "Directorio"},
    {"Nombre": "Comité Ejecutivo", "Funciones": "Toma decisiones estratégicas y coordina las actividades de la empresa.", "ReportaA": "Gerencia General"},
    {"Nombre": "Asesor Jurídico", "Funciones": "Proporciona asesoramiento legal.", "ReportaA": "Comité Ejecutivo"},
    {"Nombre": "Gerencia de Seguridad Minera", "Funciones": "Responsable de la seguridad en todas las operaciones mineras.", "ReportaA": "Comité Ejecutivo"},
    {"Nombre": "Gerencia Administrativa", "Funciones": "Maneja las funciones administrativas y de soporte.", "ReportaA": "Comité Ejecutivo"},
    {"Nombre": "Sostenibilidad y Responsabilidad Social", "Funciones": "Asegura el cumplimiento de los estándares ambientales y sociales.", "ReportaA": "Gerencia Administrativa"},
    {"Nombre": "Tecnología e Innovación", "Funciones": "Implementa nuevas tecnologías y mejora continua de procesos.", "ReportaA": "Gerencia Administrativa"},
    {"Nombre": "Contabilidad", "Funciones": "Maneja las finanzas y la contabilidad de la empresa.", "ReportaA": "Gerencia Administrativa"},
    {"Nombre": "Asistente de Contabilidad", "Funciones": "Asiste en tareas contables.", "ReportaA": "Contabilidad"},
    {"Nombre": "RRHH", "Funciones": "Gestiona los recursos humanos de la empresa.", "ReportaA": "Gerencia Administrativa"},
    {"Nombre": "Asistente de RRHH", "Funciones": "Asiste en tareas de recursos humanos.", "ReportaA": "RRHH"},
    {"Nombre": "Gerencia de Operaciones", "Funciones": "Supervisa las operaciones mineras.", "ReportaA": "Comité Ejecutivo"},
    {"Nombre": "Supervisor", "Funciones": "Coordina las actividades operativas diarias.", "ReportaA": "Gerencia de Operaciones"},
    {"Nombre": "Geología", "Funciones": "Proporciona datos y análisis geológicos.", "ReportaA": "Gerencia General"},
    {"Nombre": "Laboratorio Análisis y Simulación", "Funciones": "Realiza estudios geológicos y simulaciones.", "ReportaA": "Geología"},
    {"Nombre": "Mineros", "Funciones": "Lidera las actividades mineras diarias.", "ReportaA": "Supervisor"},
    {"Nombre": "Ayudantes de Minero", "Funciones": "Apoya directamente a los mineros en sus tareas.", "ReportaA": "Mineros"},
    {"Nombre": "Bodega", "Funciones": "Maneja los suministros y materiales.", "ReportaA": "Supervisor"},
    {"Nombre": "Depto. Mecánica y Electricidad", "Funciones": "Mantenimiento y soporte técnico.", "ReportaA": "Bodega"}
]

# Añadir nodos y edges al grafo
for col in colaboradores:
    G.add_node(col["Nombre"], title=f"<b>{col['Nombre']}</b><br>Funciones: {col['Funciones']}<br>Reporta a: {col['ReportaA']}", shape="box", borderWidth=1, borderWidthSelected=2, color="lightblue")

for col in colaboradores:
    if col["ReportaA"] != "N/A":
        G.add_edge(col["ReportaA"], col["Nombre"])

# Crear una red interactiva con layout jerárquico vertical
net = Network(height='800px', width='100%', directed=True, bgcolor='#222222', font_color='white')
net.from_nx(G)

# Configurar el layout jerárquico
net.hrepulsion(node_distance=200)
net.set_options("""
var options = {
  "layout": {
    "hierarchical": {
      "enabled": true,
      "direction": "UD",
      "sortMethod": "directed"
    }
  },
  "nodes": {
    "borderWidth": 1,
    "shape": "box",
    "shapeProperties": {
      "borderRadius": 6
    },
    "color": {
      "background": "lightblue",
      "border": "#222222",
      "highlight": {
        "background": "#97C2FC",
        "border": "#2B7CE9"
      }
    },
    "font": {
      "color": "white",
      "size": 16,
      "face": "arial",
      "align": "center"
    }
  },
  "interaction": {
    "hover": true,
    "tooltipDelay": 200,
    "hideEdgesOnDrag": true
  },
  "physics": {
    "hierarchicalRepulsion": {
      "nodeDistance": 150
    }
  }
}
""")

# Guardar y mostrar la red en Streamlit
net.save_graph('network.html')
st.title("Organigrama de la Empresa Minera")
st.components.v1.html(open('network.html', 'r').read(), height=800, scrolling=True)

