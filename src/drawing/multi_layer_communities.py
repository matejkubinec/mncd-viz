from typing import List
from models import ActorToCommunity
from py3plex.core.multinet import multi_layer_network
from converters.build_network import build_network
from converters.build_communities import build_communities
from converters import fig_to_png, fig_to_svg, edge_list_to_multi_layer, convert_community_list
from py3plex.visualization.colors import colors_default
from py3plex.visualization.multilayer import hairball_plot
from drawing.drawing_constants import node_size
import matplotlib.pyplot as plt


def hairball_layout(edge_list, community_list, image_format):
    network, actors, layers = edge_list_to_multi_layer(edge_list)
    actor_to_community, actors, communities = convert_community_list(
        community_list
    )

    colors = _get_colors(network, actor_to_community)
    fig, ax = plt.subplots()

    hairball_plot(
        network.core_network,
        color_list=colors,
        node_size=node_size,
        scale_by_size=True,
        edge_width=0.5
    )

    if image_format == "svg":
        return fig_to_svg(fig)
    else:
        return fig_to_png(fig)


def _get_colors(network: multi_layer_network, atc: List[ActorToCommunity]):
    atc_dict = dict((i.actor, i.community) for i in atc)
    colors = []
    for n in [n[0] for n in network.get_nodes()]:
        if n in atc_dict:
            colors.append(atc_dict[n])
        else:
            colors.append("black")
    return colors
