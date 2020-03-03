from py3plex.visualization.colors import all_color_names, colors_default
from converters.build_network import build_network
from converters.build_communities import build_communities
from converters.plt_to_str import plt_to_str
from converters.plt_to_png import plt_to_png
import matplotlib.pyplot as plt


def diagonal_layout(edge_list, image_format):
    network = build_network(edge_list)

    fig, ax = plt.subplots()

    network.visualize_network(
        fig=fig,
        parameters_multiedges={"alphachannel": 0.5},
    )

    if image_format == "svg":
        return plt_to_str(fig)
    else:
        return plt_to_png(fig)
