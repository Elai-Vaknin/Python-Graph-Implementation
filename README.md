# Directed Weighted Graph implementation in python
Project by Elai Vaknin & Daniel Tzafrir

# Data Structures:
## NodeData:
The class that represents a node in the graph.</br>
id = each node has a key.</br>
tag = a float type attribute to help with algorithms.</br>
info = a string type attribute to help with algorithms.</br>
pos = 3d tuple to store position.</br>

## DiGraph:
The class that represents a graph structure.</br>
ver_size = numbers of vertices in the graph.</br>
edges_size = number of edges in the graph.</br>
mode_count = number of modifications that has been made in the graph.</br>
v = a dictionary containing all keys and data of nodes in the graph. ({key: NodeData}).</br>
edges = a dictionary containing all edges in the graph out of node. ({src: {dest: weight}}).</br>
inedges = a dictionary containing all edges in the graph in of node. ({dest: {src: weight}}).</br>

## GraphAlgo:
The class that holds the entire algorithms that can be performed on a graph.</br>
init(graph: DiGraph) = inits the GraphAlgo object to perform the algorithms on the specific graph.</br>
save_to_json(path: str) = saves the graph as json format to specific file path.</br>
load_from_json(path: str) = loads a graph out of a saved json file.</br>
shortest_path(source, dest) = performs Dijkrstra algorithm to find the shortest path from source to dest.</br>
connected_component(source) = find the strongly connected component group of the source node.</br>
connected_components() = find all the strongly connected component groups in the graph.</br>
