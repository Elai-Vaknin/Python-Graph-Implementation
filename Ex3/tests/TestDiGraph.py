from random import randint

from src.DiGraph import DiGraph
import unittest

class TestDiGraph(unittest.TestCase):
    def test_graph(self):
        a = randint(50, 100)
        b = randint(500, 1000)
        graph = DiGraph()
        i = 1

        while graph.ver_size < a:
            graph.add_node(i, (randint(1, 5), randint(1, 5), randint(1, 5)))
            i += 1

        while graph.edges_size < b:
            graph.add_edge(randint(1, i - 1), randint(1, i - 1), randint(1, 100))

        self.assertEqual(graph.ver_size, a)
        self.assertEqual(graph.edges_size, b)

        return graph

    def test_addremove(self):
        graph = self.test_graph()

        a = randint(1,50)
        target = graph.ver_size - a

        while graph.ver_size > target:
            graph.remove_node(randint(1,50))

        self.assertEqual(graph.ver_size, target)

        while graph.ver_size < target:
            graph.add_node(randint(1,50), (randint(1,5), randint(1,5), randint(1,5)))

        self.assertEqual(graph.ver_size, target)

