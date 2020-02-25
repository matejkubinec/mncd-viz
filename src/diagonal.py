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


def diagonal_communities(edgelist, community_list):
    network = build_network(edgelist)
    actor_to_community, communities = build_communities(community_list)

    c_count = len(communities)
    color_mappings = dict((com, col) for col, com in zip(
        colors_default[:c_count], communities))

    colors = [color_mappings[actor_to_community[a]]
              for a, _ in network.get_nodes()]
    plt.cla()

    network.visualize_network(parameters_multiedges={"alphachannel": 0.5})

    return plt_to_str(plt)
