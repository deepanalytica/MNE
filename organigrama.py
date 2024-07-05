import streamlit as st
from pyvis.network import Network
import networkx as nx

# Crear el grafo
G = nx.DiGraph()

# Información de colaboradores
colaboradores = [
    {"Nombre": "Directorio", "Funciones": "Supervisa la gestión general de la empresa, estableciendo objetivos y estrategias a largo plazo. Toma decisiones clave sobre inversiones, fusiones y adquisiciones, y vela por el cumplimiento de las leyes y regulaciones.", "ReportaA": "N/A"},
    {"Nombre": "Gerencia General", "Funciones": "Dirige y coordina todas las actividades de la empresa, asegurando la implementación de las estrategias definidas por el Directorio. Supervisa a los gerentes de área y toma decisiones operativas y financieras importantes.", "ReportaA": "Directorio"},
    {"Nombre": "Comité Ejecutivo", "Funciones": "Compuesto por gerentes de alto nivel, asesora a la Gerencia General en la toma de decisiones estratégicas. Analiza el desempeño de la empresa, identifica oportunidades y riesgos, y propone soluciones.", "ReportaA": "Gerencia General"},
    {"Nombre": "Asesor Jurídico", "Funciones": "Brinda asesoramiento legal a la empresa en todas las áreas, incluyendo contratos, litigios, cumplimiento normativo y asuntos laborales. Revisa documentos legales y asegura que las operaciones se realicen dentro del marco legal.", "ReportaA": "Comité Ejecutivo"},
    {"Nombre": "Gerencia de Seguridad Minera", "Funciones": "Responsable de implementar y supervisar los programas de seguridad en todas las operaciones mineras. Identifica y evalúa riesgos, capacita al personal, investiga incidentes y asegura el cumplimiento de las normas de seguridad.", "ReportaA": "Comité Ejecutivo"},
    {"Nombre": "Gerencia Administrativa", "Funciones": "Gestiona las funciones administrativas y financieras de la empresa, incluyendo contabilidad, finanzas, recursos humanos, tecnología, compras y servicios generales. Supervisa el presupuesto, controla los gastos y asegura la eficiencia de las operaciones.", "ReportaA": "Comité Ejecutivo"},
    {"Nombre": "Sostenibilidad y Responsabilidad Social", "Funciones": "Desarrolla e implementa programas de sostenibilidad ambiental y responsabilidad social.  Asegura el cumplimiento de las regulaciones ambientales, promueve prácticas sostenibles en las operaciones y gestiona las relaciones con las comunidades.", "ReportaA": "Gerencia Administrativa"},
    {"Nombre": "Tecnología e Innovación", "Funciones": "Investiga, evalúa e implementa nuevas tecnologías para optimizar las operaciones mineras. Desarrolla soluciones innovadoras para mejorar la eficiencia, seguridad y sostenibilidad de la empresa.", "ReportaA": "Gerencia Administrativa"},
    {"Nombre": "Contabilidad", "Funciones": "Lleva el registro contable de las transacciones financieras de la empresa, elabora estados financieros, gestiona la facturación y los pagos, y asegura el cumplimiento de las obligaciones tributarias.", "ReportaA": "Gerencia Administrativa"},
    {"Nombre": "Asistente de Contabilidad", "Funciones": "Apoya al departamento de contabilidad en tareas como registro de transacciones, conciliaciones bancarias, archivo de documentos y atención a proveedores.", "ReportaA": "Contabilidad"},
    {"Nombre": "RRHH", "Funciones": "Gestiona los recursos humanos de la empresa, incluyendo reclutamiento, selección, contratación, capacitación, desarrollo, compensación, beneficios y relaciones laborales.", "ReportaA": "Gerencia Administrativa"},
    {"Nombre": "Asistente de RRHH", "Funciones": "Apoya al departamento de recursos humanos en tareas como publicación de ofertas de trabajo, entrevistas telefónicas, gestión de expedientes del personal y control de asistencia.", "ReportaA": "RRHH"},
    {"Nombre": "Gerencia de Operaciones", "Funciones": "Planifica, dirige y controla las operaciones mineras, incluyendo extracción, procesamiento y transporte de minerales. Supervisa al personal operativo, asegura la producción eficiente y cumple con los estándares de calidad.", "ReportaA": "Comité Ejecutivo"},
    {"Nombre": "Supervisor", "Funciones": "Supervisa y coordina al equipo de trabajo en las operaciones mineras, asigna tareas, controla el uso de equipos y herramientas, y asegura el cumplimiento de las normas de seguridad.", "ReportaA": "Gerencia de Operaciones"},
    {"Nombre": "Geología", "Funciones": "Realiza estudios geológicos para identificar y evaluar recursos minerales. Interpreta datos geofísicos y geoquímicos, elabora mapas y modelos geológicos, y estima el potencial minero.", "ReportaA": "Gerencia General"},
    {"Nombre": "Laboratorio Análisis y Simulación", "Funciones": "Analiza muestras de minerales para determinar su composición química y propiedades físicas. Realiza simulaciones de procesos para optimizar la extracción y el procesamiento de minerales.", "ReportaA": "Geología"},
    {"Nombre": "Mineros", "Funciones": "Operan equipos y herramientas para la extracción de minerales, siguiendo las instrucciones del supervisor y cumpliendo con las normas de seguridad.", "ReportaA": "Supervisor"},
    {"Nombre": "Ayudantes de Minero", "Funciones": "Apoyan a los mineros en las tareas de extracción, cargando y descargando materiales, preparando explosivos y manteniendo limpia el área de trabajo.", "ReportaA": "Mineros"},
    {"Nombre": "Bodega", "Funciones": "Recibe, almacena y despacha materiales e insumos para las operaciones mineras. Controla el inventario, gestiona las solicitudes de materiales y asegura el orden y la limpieza del almacén.", "ReportaA": "Supervisor"},
    {"Nombre": "Depto. Mecánica y Electricidad", "Funciones": "Realiza el mantenimiento preventivo y correctivo de los equipos y maquinarias utilizados en las operaciones mineras. Diagnostica y repara fallas mecánicas y eléctricas, y asegura la disponibilidad de los equipos.", "ReportaA": "Bodega"}
]

# Diccionario para acceder a la información de los departamentos por nombre
departamentos = {col["Nombre"]: col for col in colaboradores}

# Crear la red
net = Network(height='800px', width='100%', directed=True, bgcolor='#222222', font_color='white')

for col in colaboradores:
    net.add_node(col["Nombre"], title=f"<b>{col['Nombre']}</b><br>Funciones: {col['Funciones']}<br>Reporta a: {col['ReportaA']}", shape="box", borderWidth=1, borderWidthSelected=2, color="lightblue")

for col in colaboradores:
    if col["ReportaA"] != "N/A":
        net.add_edge(col["ReportaA"], col["Nombre"])

net.hrepulsion(node_distance=200)
net.set_options(
    """
    {
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
        "tooltip": {
          "enabled": false 
        },
        "navigationButtons": true,
        "clickToUse": true 
      },
      "physics": {
        "hierarchicalRepulsion": {
          "nodeDistance": 150
        }
      }
    }
    """
)


showNodeInfo_js = """
function showNodeInfo(node) {
  var infoDiv = document.getElementById("node-info");
  if (!infoDiv) {
    infoDiv = document.createElement("div");
    infoDiv.id = "node-info";
    infoDiv.style.position = "absolute";
    infoDiv.style.backgroundColor = "white";
    infoDiv.style.padding = "10px";
    infoDiv.style.border = "1px solid #ccc";
    document.body.appendChild(infoDiv);
  }

  infoDiv.innerHTML = node.title; 

  var nodePosition = network.canvas.nodes[node.id].getBoundingClientRect();
  infoDiv.style.top = (nodePosition.top + nodePosition.height) + "px";
  infoDiv.style.left = nodePosition.left + "px";
}
""" 

net.show("organigrama.html")
with open("organigrama.html", "r") as f:
    html_content = f.read()
    html_content = html_content.replace("</body>", f"<script>{showNodeInfo_js}</script></body>")
with open("organigrama.html", "w") as f:
    f.write(html_content)

st.title("Organigrama de la Empresa Minera")
st.components.v1.html(open('organigrama.html', 'r').read(), height=800, scrolling=True)

st.sidebar.title("Información del Departamento")

# Función para mostrar información del departamento
def mostrar_info_departamento(nombre_depto):
    if nombre_depto in departamentos:
        depto = departamentos[nombre_depto]
        st.sidebar.header(depto["Nombre"])
        st.sidebar.markdown(f"**Funciones:** {depto['Funciones']}")
        st.sidebar.markdown(f"**Reporta a:** {depto['ReportaA']}")
    else:
        st.sidebar.write("Selecciona un departamento en el organigrama.")

# Llamar a la función al hacer clic en un nodo (esto no está implementado 
# directamente con pyvis, necesitarías usar JavaScript para detectar el clic 
# y actualizar Streamlit)
nombre_depto_seleccionado = "Directorio" # Ejemplo inicial
mostrar_info_departamento(nombre_depto_seleccionado) 
