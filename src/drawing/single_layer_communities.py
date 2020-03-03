from networkx.readwrite.edgelist import read_edgelist
from converters.build_communities import build_communities
from converters.build_network import build_network_single_layer
from converters.plt_to_str import plt_to_str
from converters.plt_to_png import plt_to_png
from drawing.drawing_constants import edge_color, node_color
import networkx as nx
import matplotlib.pyplot as plt


def spring_layout_communities(edge_list, community_list, image_format):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)

    fig, ax = plt.subplots()

    nx.draw(
        G,
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=_get_node_color(ATC)
    )

    if image_format == "svg":
        return plt_to_str(fig)
    else:
        return plt_to_png(fig)


def circular_layout_communities(edge_list, community_list, image_format):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)
    fig, ax = plt.subplots()
    node_count = G.number_of_nodes()
    nx.draw(
        G,
        pos=nx.circular_layout(G),
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=_get_node_color(ATC)[:node_count]
    )

    if image_format == "svg":
        return plt_to_str(fig)
    else:
        return plt_to_png(fig)


def spiral_layout_communities(edge_list, community_list, image_format):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)
    fig, ax = plt.subplots()
    nx.draw(
        G,
        pos=nx.spiral_layout(G),
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=_get_node_color(ATC)
    )

    if image_format == "svg":
        return plt_to_str(fig)
    else:
        return plt_to_png(fig)


def _get_node_size(G):
    return [deg[1] * 25 for deg in sorted(nx.degree(G), key=lambda d: d[0])]


def _get_node_color(ATC):
    return [int(ATC[key]) for key in ATC]
