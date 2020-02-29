from py3plex.core import multinet
import networkx as nx


def build_network(edgelist):
    N = multinet.multi_layer_network()

    lines = edgelist.splitlines()
    edges = [line.split(" ") for line in lines]

    N.add_edges(edges, input_type="list")

    return N


def build_network_single_layer(edgelist):
    G = nx.Graph()

    lines = edgelist.splitlines()
    edges = [tuple(line.split(" ")) for line in lines]

    G.add_edges_from(edges)

    return G
