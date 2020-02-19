import matplotlib.pyplot as plt
from py3plex.visualization.colors import all_color_names, colors_default
from build_network import build_network
from plt_to_str import plt_to_str


def diagonal(edgelist):
    network = build_network(edgelist)

    plt.cla()

    network.visualize_network()

    return plt_to_str(plt)
