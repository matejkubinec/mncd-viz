from converters.build_network import build_network
from converters.build_communities import build_communities
from converters.plt_to_str import plt_to_str
from py3plex.visualization.colors import colors_default
from py3plex.visualization.multilayer import hairball_plot
import matplotlib.pyplot as plt


def hairball_layout(edge_list, community_list):
    network = build_network(edge_list)
    actor_to_community, communities = build_communities(community_list)

    c_count = len(communities)
    color_mappings = dict((com, col) for col, com in zip(
        colors_default[:c_count], communities))

    colors = [color_mappings[actor_to_community[a]]
              for a, _ in network.get_nodes()]

    plt.cla()
    hairball_plot(
        network.core_network,
        color_list=colors,
        scale_by_size=True,
        edge_width=0.5
    )
    return plt_to_str(plt)
