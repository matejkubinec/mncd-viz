from matplotlib.figure import Figure
import networkx as nx

from app import constants
from app.models import Layout
from app.network.edge_list import to_single_layer
from app.utils import layout_utils, node_utils


def draw_network(edge_list: str, layout: Layout) -> Figure:
    graph, _, _ = to_single_layer(edge_list)
    node_sizes = node_utils.get_node_sizes(graph)
    fig = Figure(figsize=constants.figsize, dpi=constants.dpi)
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        graph,
        ax=ax,
        pos=layout_utils.get_nx_layout(layout)(graph),
        edge_color=constants.edge_color,
        node_size=node_sizes,
        node_color=constants.node_color,
        with_labels=True,
        font_size=9,
        font_family="serif",
    )
    return fig
