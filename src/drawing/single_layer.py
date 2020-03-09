from networkx.readwrite.edgelist import read_edgelist
from converters import fig_to_png, fig_to_svg, edge_list_to_single_layer
from drawing.drawing_constants import edge_color, node_color
from matplotlib.figure import Figure
import networkx as nx


def spring_layout(edge_list, image_format):
    G, actors, layers = edge_list_to_single_layer(edge_list)
    node_sizes = _get_node_size(G)
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        G,
        ax=ax,
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_color,
        with_labels=True,
        font_size=9,
        font_family="serif"
    )
    return _get_image(fig, image_format)


def circular_layout(edge_list, image_format):
    G, actors, layers = edge_list_to_single_layer(edge_list)
    node_sizes = _get_node_size(G)
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        G,
        ax=ax,
        pos=nx.circular_layout(G),
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_color,
        with_labels=True,
        font_size=9,
        font_family="serif"
    )
    return _get_image(fig, image_format)


def spiral_layout(edge_list, image_format):
    G, actors, layers = edge_list_to_single_layer(edge_list)
    node_sizes = _get_node_size(G)
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        G,
        ax=ax,
        pos=nx.spiral_layout(G),
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_color,
        with_labels=True,
        font_size=9,
        font_family="serif"
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
