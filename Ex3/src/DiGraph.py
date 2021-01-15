from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    def __init__(self):
        self.ver_size = 0
        self.edges_size = 0
        self.mode_count = 0
        self.v = {}
        self.edges = {}
        self.inedges = {}

    def add_node(self, node_id: int, pos: tuple = None):
        if not self.v.__contains__(node_id):
            node = NodeData(node_id)

            if pos is None:
                node.set_pos((0.0,0.0,0.0))
            else:
                node.set_pos(pos)

            self.v[node_id] = node
            self.ver_size += 1
            self.mode_count += 1

            return True
        else:
            return False

    def remove_node(self, node_id):
        if self.v.__contains__(node_id):
            del self.v[node_id]
            self.ver_size -= 1
            self.mode_count += 1

            return True

        return False

    def add_edge(self, id1: int, id2: int, weight):
        if id1 == id2:
            return False

        added = False

        if id1 in self.v.keys() and id2 in self.v.keys():
            ni = {}
            ni_in = {}

            if self.edges.__contains__(id1):
                ni = self.edges[id1]

                if not ni.__contains__(id2):
                    self.edges[id1][id2] = weight
                    self.edges_size += 1
                    added = True
            else:
                self.edges[id1] = {}

                self.edges[id1][id2] = weight

                self.edges_size += 1
                added = True

            if added:
                if self.inedges.__contains__(id2):
                    ni = self.inedges[id2]

                    if not ni.__contains__(id1):
                        self.inedges[id2][id1] = weight
                else:
                    self.inedges[id2] = {}
                    self.inedges[id2][id1] = weight

        return added

    def remove_edge(self, id1, id2):
        if id1 in self.v.keys() and id2 in self.v.keys():
            ni = self.edges[id1]

            if ni.__contains__(id2):
                del self.edges[id1][id2]

                self.edges_size -= 1
                self.mode_count += 1

                return True

        return False

    def all_in_edges_of_node(self, id1):
        if self.inedges.__contains__(id1):
            return self.inedges[id1]

        return None

    def all_out_edges_of_node(self, id1):
        if self.edges.__contains__(id1):
            return self.edges[id1]

        return None

    def get_all_v(self):
        return self.v

    def get_mc(self):
        return self.mode_count

    def v_size(self):
        return self.ver_size

    def e_size(self):
        return self.edges_size

    def __str__(self):
        return "Graph:\nNodes[{}]:{}\nEdges[{}]:{}".format(self.ver_size, self.v.keys(), self.edges_size, self.edges)
