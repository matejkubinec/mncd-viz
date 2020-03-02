from parsers import parse_edge_list, Edge, Actor, Layer
import unittest


class EdgeListParserTests(unittest.TestCase):

    def test_edge_list_without_metadata(self):
        edge_list = "\n".join([
            "0 1",
            "0 2",
            "1 2"
        ])

        edges, actors, layers = parse_edge_list(edge_list)

        self.assertListEqual(edges, [
            Edge(0, 0, 1, 0, 1),
            Edge(0, 0, 2, 0, 1),
            Edge(1, 0, 2, 0, 1)
        ])
        self.assertListEqual(actors, [])
        self.assertListEqual(layers, [])

    def test_edge_list_with_actors_metadata(self):
        edge_list = "\n".join([
            "0 1",
            "0 2",
            "1 2",
            "# Actors",
            "0 a0",
            "1 a1",
            "2 a2"
        ])

        edges, actors, layers = parse_edge_list(edge_list)

        self.assertListEqual(edges, [
            Edge(0, 0, 1, 0, 1),
            Edge(0, 0, 2, 0, 1),
            Edge(1, 0, 2, 0, 1)
        ])
        self.assertListEqual(actors, [
            Actor(0, "a0"),
            Actor(1, "a1"),
            Actor(2, "a2")
        ])
        self.assertListEqual(layers, [])

    def test_edge_list_with_all_metadata(self):
        edge_list = "\n".join([
            "0 0 1 0 1",
            "0 0 2 0 1",
            "1 0 2 0 1",
            "# Actors",
            "0 a0",
            "1 a1",
            "2 a2",
            "# Layers",
            "0 l0"
        ])

        edges, actors, layers = parse_edge_list(edge_list)

        self.assertListEqual(edges, [
            Edge(0, 0, 1, 0, 1),
            Edge(0, 0, 2, 0, 1),
            Edge(1, 0, 2, 0, 1)
        ])
        self.assertListEqual(actors, [
            Actor(0, "a0"),
            Actor(1, "a1"),
            Actor(2, "a2")
        ])
        self.assertListEqual(layers, [
            Layer(0, "l0"),
        ])
