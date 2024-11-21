from app.models import Edge
import networkx as nx


def build_graph(edges: list[Edge]):
    graph = nx.Graph()

    for e in edges:
        graph.add_edge(e.actor_from, e.actor_to, weight=e.weight)

    return graph
