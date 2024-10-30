from typing import List
import networkx as nx

from app.models import Actor, Layer
from app.parsers.edge_list import parse_edge_list


def to_single_layer(
    edge_list: str,
) -> tuple[nx.Graph, List[Actor], List[Layer]]:
    G = nx.Graph()
    edges, actors, layers = parse_edge_list(edge_list)

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
