from matplotlib.figure import Figure
import networkx as nx

from app import constants
from app.models import Layout
from app.network.edge_list import to_single_layer


def draw_network(edge_list: str, layout: Layout) -> Figure:
    G, _, _ = to_single_layer(edge_list)
    node_sizes = _get_node_size(G)
    fig = Figure(figsize=constants.figsize, dpi=constants.dpi)
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        G,
        ax=ax,
        pos=_get_nx_layout(layout)(G),
        edge_color=constants.edge_color,
        node_size=node_sizes,
        node_color=constants.node_color,
        with_labels=True,
        font_size=9,
        font_family="serif",
    )
    return fig


def _get_nx_layout(layout: Layout):
    if layout == Layout.spring:
        return nx.spring_layout
    elif layout == Layout.spiral:
        return nx.spiral_layout
    else:
        return nx.circular_layout


def _get_node_size(G):
    min_size = 25
    degrees = sorted(nx.degree(G), key=lambda d: d[0])
    return [deg[1] * min_size for deg in degrees]
