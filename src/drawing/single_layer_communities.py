from networkx.readwrite.edgelist import read_edgelist
from converters.build_communities import build_communities
from converters.build_network import build_network_single_layer
from converters.plt_to_str import plt_to_str
from drawing.drawing_constants import edge_color, node_color
import networkx as nx
import matplotlib.pyplot as plt


def spring_layout_communities(edge_list, community_list):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)
    plt.cla()
    nx.draw(
        G,
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=_get_node_color(ATC)
    )
    return plt_to_str(plt)


def circular_layout_communities(edge_list, community_list):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)
    plt.cla()
    node_count = G.number_of_nodes()
    nx.draw(
        G,
        pos=nx.circular_layout(G),
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=_get_node_color(ATC)[:node_count]
    )
    return plt_to_str(plt)


def spiral_layout_communities(edge_list, community_list):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)
    plt.cla()
    nx.draw(
        G,
        pos=nx.spiral_layout(G),
        edge_color=edge_color,
        node_size=_get_node_size(G),
        node_color=_get_node_color(ATC)
    )
    return plt_to_str(plt)


def _get_node_size(G):
    return [deg[1] * 25 for deg in sorted(nx.degree(G), key=lambda d: d[0])]


def _get_node_color(ATC):
    return [int(ATC[key]) for key in ATC]
