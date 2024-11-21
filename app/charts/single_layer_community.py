from matplotlib.figure import Figure
from app.network.edge_list import to_single_layer
from app.parsers.communities import parse_community_list
from app.models import Layout
from app.utils import layout_utils, node_utils
from app import constants
import networkx as nx


def draw_communities(edge_list: str, community_list: str, layout: Layout) -> Figure:
    graph, _, _ = to_single_layer(edge_list)
    atc, _, _ = parse_community_list(community_list)
    fig = Figure(figsize=constants.figsize, dpi=constants.dpi)
    node_colors = node_utils.get_node_colors(graph, atc)
    node_sizes = node_utils.get_node_sizes(graph)
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        graph,
        ax=ax,
        pos=layout_utils.get_nx_layout(layout)(graph),
        edge_color=constants.edge_color,
        node_size=node_sizes,
        node_color=node_colors,
        with_labels=True,
        font_size=9,
        font_family="serif",
    )
    return fig
