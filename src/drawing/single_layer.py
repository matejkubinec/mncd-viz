from networkx.readwrite.edgelist import read_edgelist
from converters.build_network import build_network_single_layer
from converters.plt_to_str import plt_to_str
from drawing.drawing_constants import edge_color, node_color
import matplotlib.pyplot as plt
import networkx as nx


def spring_layout(edge_list):
    G = build_network_single_layer(edge_list)
    plt.cla()
    nx.draw(
        G,
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=node_color
    )
    return plt_to_str(plt)


def circular_layout(edge_list):
    G = build_network_single_layer(edge_list)
    plt.cla()
    nx.draw(
        G,
        pos=nx.circular_layout(G),
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=node_color
    )
    return plt_to_str(plt)


def spiral_layout(edge_list):
    G = build_network_single_layer(edge_list)
    plt.cla()
    nx.draw(
        G,
        pos=nx.spiral_layout(G),
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=node_color
    )
    return plt_to_str(plt)


def _get_node_size(G):
    return [deg[1] * 25 for deg in sorted(nx.degree(G), key=lambda d: d[0])]
