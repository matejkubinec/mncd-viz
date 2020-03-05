from py3plex.visualization.colors import all_color_names, colors_default
from converters.build_network import build_network
from converters.build_communities import build_communities
from converters import fig_to_png, fig_to_svg, edge_list_to_multi_layer
import matplotlib.pyplot as plt


def diagonal_layout(edge_list, image_format="svg"):
    network, actors, layers = edge_list_to_multi_layer(edge_list)

    plt.cla()

    parameters_layers = {
        "node_size": 25,
        "scale_by_size": True,
    }

    network.visualize_network(
        style="diagonal",
        parameters_layers=parameters_layers
    )

    if image_format == "svg":
        return fig_to_svg(plt.gcf())
    else:
        return fig_to_png(plt.gcf())
