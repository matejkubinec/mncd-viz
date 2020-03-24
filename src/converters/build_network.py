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
    edges = []

    for line in lines:
        values = line.split(" ")

        if len(values) == 3:
            edges.append(tuple(values))
        elif len(values) == 2:
            edges.append(tuple(values))
        else:
            edges.append(tuple([values[0], values[2]]))

    G.add_edges_from(edges)

    return G


def build_network(edges, actors):
    G = nx.Graph()

    for e in edges:
        G.add_edge(e.actor_from, e.actor_to, weight=e.weight)

    return G
