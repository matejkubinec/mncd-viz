
from typing import List
from models import Actor, Layer
from parsers import EdgeListParser
from py3plex.core import multinet
import networkx as nx


def edge_list_to_multi_layer(edge_list: str) -> (multinet.multi_layer_network, List[Actor], List[Layer]):
    N = multinet.multi_layer_network()
    parser = EdgeListParser()

    edges, actors, layers = parser.parse_edge_list(edge_list)
    edges_to_add = [e.to_list() for e in edges]

    N.add_edges(edges_to_add, input_type="list")

    return N, actors, layers


def edge_list_to_single_layer(edge_list: str) -> (nx.Graph, List[Actor], List[Layer]):
    G = nx.Graph()
    parser = EdgeListParser()

    edges, actors, layers = parser.parse_edge_list(edge_list)

    edges_to_add = list()
    for edge in edges:
        f = edge.actor_from
        t = edge.actor_to

        edges_to_add.append((f, t))

    G.add_edges_from(edges_to_add)

    if len(actors) > 0 and len(actors) != len(G.nodes()):
        actors_set = set(a.index for a in actors)
        nodes_set = set(G.nodes())

        nodes_to_add = actors_set.difference(nodes_set)
        G.add_nodes_from(nodes_to_add)

    return G, actors, layers
