import streamlit as st
from pyvis.network import Network
import networkx as nx

# ... (Tu código para crear el grafo 'G') ...

net = Network(height='800px', width='100%', directed=True, bgcolor='#222222', font_color='white')
net.from_nx(G)
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

# Función JavaScript fuera del JSON
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

net.add_node("Directorio", title="Información del nodo", physics=False)

# Agregar la función JavaScript al HTML generado
net.show("organigrama.html")
with open("organigrama.html", "r") as f:
    html_content = f.read()
    html_content = html_content.replace("</body>", f"<script>{showNodeInfo_js}</script></body>")
with open("organigrama.html", "w") as f:
    f.write(html_content)

st.title("Organigrama de la Empresa Minera")
st.components.v1.html(open('organigrama.html', 'r').read(), height=800, scrolling=True)
