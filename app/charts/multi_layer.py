from app.parsers.edges import parse_edge_list
from app.theme.palette import get_palette
from app.utils import multi_layer_utils, graph_utils, node_utils
from app import constants
from matplotlib.figure import Figure
import networkx as nx


def draw_slices(edge_list: str):
    edges, _, layers = parse_edge_list(edge_list)
    fig = Figure(figsize=constants.figsize, dpi=constants.dpi)
    axes = multi_layer_utils.get_axes(fig, layers)
    palette = get_palette(len(layers))

    if len(layers) > 2 and len(layers) % 2 == 1:
        r = int((len(layers) - 1) / 2)
        c = int(len(layers) % 2)
        axes[r, c].axis("off")
    elif len(layers) == 1:
        axes[1].axis("off")

    for i, l in enumerate(layers):
        layer_edges = filter(lambda e: multi_layer_utils.filter_edges(e, l), edges)
        r = int(i / 2)
        c = int(i % 2)

        ax = None
        if len(layers) > 2:
            ax = axes[r, c]
        else:
            ax = axes[c]

        ax.set_title(l.name)

        graph = graph_utils.build_graph(layer_edges)
        node_size = node_utils.get_node_sizes(graph)

        nx.draw(
            graph,
            ax=ax,
            label=l.name,
            node_color=[palette[i]],
            node_size=node_size,
            font_size=9,
            font_family="serif",
            with_labels=True,
        )

    return fig
