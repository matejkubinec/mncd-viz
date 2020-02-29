from py3plex.visualization.colors import all_color_names, colors_default
from converters.build_network import build_network
from converters.build_communities import build_communities
from converters.plt_to_str import plt_to_str
import matplotlib.pyplot as plt


def diagonal_layout(edge_list):
    network = build_network(edge_list)

    plt.cla()

    network.visualize_network(
        parameters_multiedges={"alphachannel": 0.5}
    )

    return plt_to_str(plt)
