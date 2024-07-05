import streamlit as st
from pyvis.network import Network
import networkx as nx

# ... (Código para definir `colaboradores` y crear el grafo `G` -  se mantiene igual) ...

# Crear la red interactiva
net = Network(height='800px', width='100%', directed=True, bgcolor='#222222', font_color='white')
net.from_nx(G)

# Configurar el layout jerárquico
net.hrepulsion(node_distance=200)

# Opciones de configuración con JavaScript para mostrar un div al hacer clic
net.set_options(
    """
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
        "tooltip": {
          "enabled": false // Deshabilitar tooltip por defecto
        },
        "navigationButtons": true,
        "clickToUse": true // Habilitar clic para seleccionar nodos
      },
      "physics": {
        "hierarchicalRepulsion": {
          "nodeDistance": 150
        }
      }
    };

    // Función para mostrar el div con la información del nodo
    function showNodeInfo(node) {
      // Crear un div para mostrar la información
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

      // Actualizar el contenido del div con la información del nodo
      infoDiv.innerHTML = node.title; 

      // Posicionar el div debajo del nodo
      var nodePosition = network.canvas.nodes[node.id].getBoundingClientRect();
      infoDiv.style.top = (nodePosition.top + nodePosition.height) + "px";
      infoDiv.style.left = nodePosition.left + "px";
    }

    // Manejar el evento click en los nodos
    network.on("click", function (params) {
      if (params.nodes.length > 0) { 
        var nodeId = params.nodes[0];
        var node = network.body.nodes[nodeId];
        showNodeInfo(node);
      } else {
        // Ocultar el div si no se hace clic en un nodo
        var infoDiv = document.getElementById("node-info");
        if (infoDiv) {
          infoDiv.style.display = "none";
        }
      }
    });

    """
)


# Guardar y mostrar la red en Streamlit
net.save_graph('network.html')
st.title("Organigrama de la Empresa Minera")
st.components.v1.html(open('network.html', 'r').read(), height=800, scrolling=True)
