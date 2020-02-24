from build_network import build_network
from build_communities import build_communities
from plt_to_str import plt_to_str

from py3plex.visualization.colors import colors_default
from py3plex.visualization.multilayer import hairball_plot

import matplotlib.pyplot as plt


def hairball_communities(edgelist, communities_list):
    network = build_network(edgelist)
    actor_to_community, communities = build_communities(communities_list)

    c_count = len(communities)
    color_mappings = dict((com, col) for col, com in zip(
        colors_default[:c_count], communities))

    colors = [color_mappings[actor_to_community[a]]
              for a, _ in network.get_nodes()]

    hairball_plot(network.core_network,
                  color_list=colors,
                  scale_by_size=True,
                  edge_width=0.5)

    return plt_to_str(plt)
