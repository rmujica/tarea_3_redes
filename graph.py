import networkx as nx
import matplotlib.pyplot as plt

# inicializamos grafo
g = nx.Graph()

# rellenamos
edges = [
  ('PC', 'A', 3),
  ('A', 'B', 1),
  ('A', 'G', 4),
  ('A', 'I', 10),
  ('B', 'C', 9),
  ('B', 'E', 8),
  ('C', 'D', 2),
  ('D', 'E', 9),
  ('D', 'F', 4),
  ('D', 'I', 2),
  ('E', 'F', 2),
  ('E', 'I', 1),
  ('F', 'H', 6),
  ('G', 'H', 7),
  ('H', 'I', 3),
  ('I', 'SERVIDOR', 1)
]

paths = {}

g.add_weighted_edges_from(edges)

# calculamos usando bellman-ford
for node in g.nodes():
  if node == 'PC' or node == 'SERVIDOR':
    continue

  # ejecutamos el algoritmo para el nodo
  predecesor, distancias = nx.bellman_ford(g, node)
  
  # en predecesor hay un diccionario que se usa asi:
  # la llave representa el nodo al cual queremos ir
  # desde el nodo actual. el valor representa el nodo
  # por el cual debemos pasar. si utilizamos la misma
  # llave en el diccionario distancia obtenemos la
  # distancia que debemos recorrer para llegar al
  # nodo anterior.
  print "### NODO", node, " ###"
  print "# diccionario de predecesores:"
  print predecesor
  print "# diccionario de distancias:"
  print distancias, '\n'

  paths[node] = (predecesor, distancias)

# eliminamos el enlace
print "### ELIMINANDO NODO", '\n'
g.remove_edge('H', 'I')

# recalculamos solo los caminos que utilizaban el enlace
for node in paths:
  path = paths[node][0]
  for k in path:
    
    # verificamos si se utilizaba el camino H-I
    if k == 'H' and path[k] == 'I' or k == 'I' and path[k] == 'H':
      
      # volvemos a ejecutar bellman-ford
      print "### RUTAS DESDE NODO", node, "SE DEBEN RECALCULAR"
      predecesor, distancias = nx.bellman_ford(g, node)

      # verificamos si hay algun cambio en las distancias
      changed = set(distancias.items()) - set(paths[node][1].items())
      print "# RUTAS CAMBIADAS:"
      print changed, '\n'
      paths[node] = (predecesor, distancias)