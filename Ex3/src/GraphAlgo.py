from collections import deque

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.NodeData import NodeData

import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

from json import JSONEncoder
import json
import sys


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = None):
        self.graph = g
        self.Time = 0

    def get_graph(self):
        if self.graph is None:
            return DiGraph()

        return self.graph

    def save_to_json(self, file_name):
        try:
            with open(file_name, 'w') as f:
                edges_list = []
                nodes_list = []

                v = self.graph.get_all_v()

                for key in v.keys():
                    node: NodeData = v[key]
                    (x, y, z) = node.pos
                    pos = "{},{},{}".format(x, y, z)
                    node_dict = {"pos": pos, "id": key}
                    nodes_list.append(node_dict)

                edges = self.graph.edges
                i = 1
                if edges is not None:
                    for src in edges:
                        if edges[src] is None:
                            continue

                        for dest in edges[src].keys():
                            w = edges[src][dest]

                            print("Edge:", src, dest, w)
                            edge_dict = {"src": src, "w": w, "dest": dest}
                            # print(edge_dict)
                            edges_list.append(edge_dict)

                print(edges_list)

                dict_graph = {"Edges": edges_list, "Nodes": nodes_list}
                print(dict_graph)

                json.dump(dict_graph, fp=f)
        except:
            print("Error occured while saving!")

    def load_from_json(self, file_name):
        graph = DiGraph()

        try:
            with open(file_name, 'r') as f:
                dictionary = json.load(fp=f)

                for ver in dictionary["Nodes"]:
                    key: int = ver["id"]

                    args = ver["pos"].split(",")

                    x = float(args[0])
                    y = float(args[1])
                    z = float(args[2])

                    print(key, ver["pos"], ver["pos"][0])
                    graph.add_node(key, (x, y, z))

                for edge in dictionary["Edges"]:
                    src = edge["src"]
                    dest = edge["dest"]
                    weight = edge["w"]

                    graph.add_edge(src, dest, weight)
        except:
            print("Error occured while loading!")

        return graph

    def shortest_path(self, source, dest):
        infinity = float('inf')

        v = self.graph.get_all_v()

        previous = {}
        shortest_distance = {}
        unseen_nodes = dict(v)
        path = []

        for node in unseen_nodes:
            shortest_distance[node] = infinity
            previous[node] = -1

        shortest_distance[source] = 0;

        while unseen_nodes:
            min_node = None

            for node in unseen_nodes:
                if min_node is None:
                    min_node = node

                elif shortest_distance[node] < shortest_distance[min_node]:
                    min_node = node

            neighbours: {int: float} = self.graph.all_out_edges_of_node(min_node)

            if min_node == dest:
                break

            if neighbours is not None:
                for ni in neighbours:
                    cost = neighbours[ni]

                    if cost + shortest_distance[min_node] < shortest_distance[ni]:
                        shortest_distance[ni] = cost + shortest_distance[min_node]
                        previous[ni] = min_node

            unseen_nodes.pop(min_node)

        path.append(dest)

        distance = shortest_distance[dest]

        if distance == float('inf'):
            return -1, None

        while previous[dest] is not source:
            dest = previous[dest]
            path.append(dest)

        final = [source]

        while len(path):
            final.append(path.pop())

        return distance, final

    def connected_component(self, id1: int) -> list:
        v: {int: NodeData} = self.graph.get_all_v()

        if id1 not in v:
            return []

        if len(v) == 1:
            return [id1]

        for key in v.keys():
            node: NodeData = v[key]
            node.set_tag(0)

        dq = deque()

        v[id1].set_tag(1)

        dq.append(id1)

        list_out = []

        while dq:
            curr = dq.popleft()
            
            if v[curr].get_tag():
                edges_out_of = self.graph.all_out_edges_of_node(curr)

                if edges_out_of is not None:
                    for j in edges_out_of:
                        if v[j].tag == 0:
                            dq.append(j)
                            v[j].tag = 1

            list_out.append(curr)

            v[curr].tag = 2

        for key in v.keys():
            v[key].tag = 0

        v[id1].set_tag(1)

        dq.append(id1)

        my_list_in = []

        while dq:
            curr = dq.popleft()

            if v[curr].tag == 1:
                edges_out_of = self.graph.all_in_edges_of_node(curr)

                if edges_out_of is not None:
                    for j in edges_out_of:
                        if v[j].tag == 0:
                            dq.append(j)
                            v[j].tag = 1

            my_list_in.append(curr)
            v[curr].tag = 2

        return list(set(list_out) & set(my_list_in))

    def connected_components(self):
        if self.graph is None:
            return []

        visited = {}
        result = []

        v = self.graph.get_all_v()

        for ver in v.keys():
            if ver not in visited:
                list = self.connected_component(ver)

                for j in list:
                    visited[j] = j

                result.append(list)

        return result

    def plot_graph(self):
        if self.graph is None:
            return None

        v = self.graph.get_all_v()

        list_x = []
        list_y = []

        min_value = float('inf')
        max_value = float('-inf')

        for key in v.keys():
            edges: {int: float} = self.graph.all_out_edges_of_node(key)

            node: NodeData = v[key]

            pos = node.get_pos()

            x: float = pos[0]
            y: float = pos[1]

            if x > max_value:
                max_value = x
            if y > max_value:
                max_value = y
            if x < min_value:
                min_value = x
            if y < min_value:
                min_value = y

            list_x.append(x)
            list_y.append(y)

            if edges is not None:
                for dest in edges:
                    dest_node: NodeData = v[dest]

                    (x2, y2, z2) = dest_node.get_pos()

                    plt.annotate(text='', xy=(x2, y2), xytext=(x, y), zorder=1,
                                 arrowprops=dict(color="black", width=0.5, headwidth=5.0))

            text = plt.text(x, y, key, zorder=2, color="green", weight="bold")
            text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='white'), path_effects.Normal()])

        plt.plot(list_x, list_y, 'ro')

        min_value -= 0.15
        max_value += 0.15

        plt.axis([min_value, max_value, min_value, max_value])
        plt.show()


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
