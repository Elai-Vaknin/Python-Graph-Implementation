from random import randint

from src.DiGraph import DiGraph
import TestDiGraph
import unittest

from src.GraphAlgo import GraphAlgo


class TestDiGraph(unittest.TestCase):
    def test_saveload(self):
        a = randint(50, 100)
        b = randint(500, 1000)

        graph = DiGraph()
        i = 1

        while graph.ver_size < a:
            graph.add_node(i, (randint(1, 5), randint(1, 5), randint(1, 5)))
            i += 1

        while graph.edges_size < b:
            graph.add_edge(randint(1, i - 1), randint(1, i - 1), randint(1, 100))

        a = GraphAlgo(graph)
        a.save_to_json("testsaveload.json");

        b:DiGraph = a.load_from_json("testsaveload.json")

        print(b)
        v1 = graph.get_all_v()
        v2 = b.get_all_v()

        e1 = graph.edges
        e2 = b.edges

        self.assertEqual(graph.ver_size, b.ver_size)
        self.assertEqual(graph.edges_size, b.edges_size)

        for key in v1.keys():
            self.assertEqual(True, v2.__contains__(key))

        for key in e1.keys():
            self.assertEqual(True, e2.__contains__(key))
            self.assertEqual(e1[key], e2[key])

    def test_algo(self):
        g = DiGraph()

        g.add_node(1, (1, 4, 0))
        g.add_node(2, (4, 4, 0))
        g.add_node(3, (2.5, 2.5, 0))
        g.add_node(4, (1, 1, 0))
        g.add_node(5, (4, 1, 0))

        g.add_edge(1, 2, 1.0)
        g.add_edge(2, 5, 8.0)
        g.add_edge(2, 3, 3.0)
        g.add_edge(3, 4, 1.0)
        g.add_edge(1, 4, 8.0)
        g.add_edge(4, 5, 3.0)
        g.add_edge(1, 3, 6.0)

        a = GraphAlgo(g)
        a.plot_graph()

        (value, path) = a.shortest_path(1, 5);
        self.assertEqual(value, 8)
        (value, path) = a.shortest_path(2, 1);
        self.assertEqual(value, -1)
        (value, path) = a.shortest_path(1, 3);
        self.assertEqual(value, 4)
        (value, path) = a.shortest_path(2, 5);
        self.assertEqual(value, 7)
        (value, path) = a.shortest_path(1, 4);
        self.assertEqual(value, 5)

        list1 = a.connected_component(1);

        self.assertEqual(list1, [1])

        g.add_edge(5, 3, 2.0)

        list3 = a.connected_component(3)

        self.assertEqual(list3, [3,4,5])

        list = a.connected_components()

        for key in g.get_all_v():
            self.assertEqual(True, list.__contains__(sorted(a.connected_component(key))))


