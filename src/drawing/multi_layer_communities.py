from converters.build_network import build_network
from converters.build_communities import build_communities
from converters import fig_to_png, fig_to_svg, edge_list_to_multi_layer, convert_community_list
from py3plex.visualization.colors import colors_default
from py3plex.visualization.multilayer import hairball_plot
import matplotlib.pyplot as plt


def hairball_layout(edge_list, community_list, image_format):
    network, actors, layers = edge_list_to_multi_layer(edge_list)
    actor_to_community, actors, communities = convert_community_list(
        community_list
    )

    c_count = len(communities)
    color_mappings = dict((com, col) for col, com in zip(
        colors_default[:c_count], communities))

    colors = []
    for a, _ in network.get_nodes():

        if a in actor_to_community:
            colors.append(color_mappings[actor_to_community[a]])
        else:
            colors.append("black")

    fig, ax = plt.subplots()

    hairball_plot(
        network.core_network,
        color_list=colors,
        node_size=25,
        scale_by_size=True,
        edge_width=0.5
    )

    if image_format == "svg":
        return fig_to_svg(fig)
    else:
        return fig_to_png(fig)
