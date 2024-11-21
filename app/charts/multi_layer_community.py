from matplotlib.figure import Figure
from app import constants, models
from app.parsers.communities import parse_community_list
from app.parsers.edges import parse_edge_list
from app.utils import color_utils, graph_utils, node_utils
import networkx as nx
import math


def draw_slices_with_communities(edge_list: str, community_list: str):
    edges, _, layers = parse_edge_list(edge_list)
    act, _, communities = parse_community_list(community_list)

    fig = Figure(figsize=constants.figsize, dpi=constants.dpi)
    axes = _get_axes(fig, layers)

    if len(layers) > 2 and len(layers) % 2 == 1:
        r = int((len(layers) - 1) / 2)
        c = int(len(layers) % 2)
        axes[r, c].axis("off")
    elif len(layers) == 1:
        axes[1].axis("off")

    for i, l in enumerate(layers):
        layer_edges = filter(lambda e: _filter_edges(e, l), edges)
        r = int(i / 2)
        c = int(i % 2)

        ax = axes[r, c] if len(layers) > 2 else axes[c]
        ax.set_title(l.name)

        graph = graph_utils.build_graph(layer_edges)
        node_size = node_utils.get_node_sizes(graph)
        node_color = color_utils.get_layer_colors(act, communities, graph.nodes())

        nx.draw(
            graph,
            ax=ax,
            label=l.name,
            node_color=node_color,
            node_size=node_size,
            font_size=9,
            font_family="serif",
            with_labels=True,
        )

    return fig


def _get_axes(fig: Figure, layers: list[models.Layer]):
    nrows = math.ceil(len(layers) / 2.0)
    return fig.subplots(nrows, 2)


def _filter_edges(edge: models.Edge, layer: models.Layer):
    return edge.layer_from == layer.index and edge.layer_to == layer.index
