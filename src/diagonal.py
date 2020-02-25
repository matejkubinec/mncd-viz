from build_network import build_network
from build_communities import build_communities
from plt_to_str import plt_to_str

from py3plex.visualization.colors import all_color_names, colors_default

import matplotlib.pyplot as plt


def diagonal(edgelist):
    network = build_network(edgelist)

    plt.cla()

    network.visualize_network(parameters_multiedges={"alphachannel": 0.5})

    return plt_to_str(plt)
