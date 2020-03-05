from models import Edge, Actor, Layer
from converters import edge_list_to_multi_layer
import unittest


class EdgeListConversionsTests(unittest.TestCase):

    def build_network_single_layer_without_metadata(self):
        edge_list = "\n".join([
            "0 1",
            "0 2",
            "1 2"
        ])

        N, actors, layers = edge_list_to_multi_layer(edge_list)

        self.assertListEqual(N.get_nodes(), [(0, 0), (1, 0), (2, 0)])
        self.assertListEqual(N.get_edges(), [
            ((0, 0), (1, 0)),
            ((0, 0), (2, 0)),
            ((1, 0), (2, 0))
        ])
        self.assertListEqual(actors, [])
        self.assertListEqual(layers, [])

    def test_edge_list_parser_with_actors_metadata(self):
        edge_list = "\n".join([
            "0 1",
            "0 2",
            "1 2",
            "# Actors",
            "0 a0",
            "1 a1",
            "2 a2"
        ])

        N, actors, layers = edge_list_to_multi_layer(edge_list)

        nodes = list(N.get_nodes())
        edges = list(N.get_edges())
        self.assertListEqual(nodes, [(0, 0), (1, 0), (2, 0)])
        self.assertListEqual(edges, [
            ((0, 0), (1, 0)),
            ((0, 0), (2, 0)),
            ((1, 0), (2, 0))
        ])
        self.assertListEqual(actors, [
            Actor(0, "a0"),
            Actor(1, "a1"),
            Actor(2, "a2")
        ])
        self.assertListEqual(layers, [])

    def test_edge_list_parser_with_layers_metadata(self):
        edge_list = "\n".join([
            "0 0 1 0 1",
            "0 0 2 0 1",
            "1 0 2 0 1",
            "# Layers",
            "0 l0"
        ])

        N, actors, layers = edge_list_to_multi_layer(edge_list)

        nodes = list(N.get_nodes())
        edges = list(N.get_edges())
        self.assertListEqual(nodes, [(0, 0), (1, 0), (2, 0)])
        self.assertListEqual(edges, [
            ((0, 0), (1, 0)),
            ((0, 0), (2, 0)),
            ((1, 0), (2, 0))
        ])
        self.assertListEqual(actors, [])
        self.assertListEqual(layers, [
            Layer(0, "l0"),
        ])

    def test_edge_list_parser_with_all_metadata(self):
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

        N, actors, layers = edge_list_to_multi_layer(edge_list)

        nodes = list(N.get_nodes())
        edges = list(N.get_edges())
        self.assertListEqual(nodes, [(0, 0), (1, 0), (2, 0)])
        self.assertListEqual(edges, [
            ((0, 0), (1, 0)),
            ((0, 0), (2, 0)),
            ((1, 0), (2, 0))
        ])
        self.assertListEqual(actors, [
            Actor(0, "a0"),
            Actor(1, "a1"),
            Actor(2, "a2")
        ])
        self.assertListEqual(layers, [
            Layer(0, "l0"),
        ])
