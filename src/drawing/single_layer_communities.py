from networkx.readwrite.edgelist import read_edgelist
from converters.build_communities import build_communities
from converters.build_network import build_network_single_layer
from converters import fig_to_png
from drawing.drawing_constants import edge_color, node_color
import networkx as nx
import matplotlib.pyplot as plt


def spring_layout_communities(edge_list, community_list, image_format="svg"):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)
    node_colors = _get_node_color(G, ATC)
    node_sizes = _get_node_size(G)
    fig, ax = plt.subplots()
    nx.draw(
        G,
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_colors
    )
    return _get_image(fig, image_format)


def circular_layout_communities(edge_list, community_list, image_format="svg"):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)
    node_colors = _get_node_color(G, ATC)
    node_sizes = _get_node_size(G)
    fig, ax = plt.subplots()
    nx.draw(
        G,
        pos=nx.circular_layout(G),
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_colors
    )
    return _get_image(fig, image_format)


def spiral_layout_communities(edge_list, community_list, image_format="svg"):
    G = build_network_single_layer(edge_list)
    ATC, C = build_communities(community_list)
    node_colors = _get_node_color(G, ATC)
    node_sizes = _get_node_size(G)
    fig, ax = plt.subplots()
    nx.draw(
        G,
        pos=nx.spiral_layout(G),
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_colors
    )
    return _get_image(fig, image_format)


def _get_image(fig, image_format):
    if image_format == "svg":
        return fig_to_svg(fig)
    else:
        return fig_to_png(fig)


def _get_node_size(G):
    min_size = 25
    degrees = sorted(nx.degree(G), key=lambda d: d[0])
    return [deg[1] * min_size for deg in degrees]


def _get_node_color(G, ATC):
    colors = list()
    for n in G.nodes():
        c = int(ATC[n])
        colors.append(c)
    return colors
