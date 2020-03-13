from typing import List
from models import ActorToCommunity
from py3plex.core.multinet import multi_layer_network
from converters.build_network import build_network
from converters.build_communities import build_communities
from converters import fig_to_png, fig_to_svg, edge_list_to_multi_layer, convert_community_list
from py3plex.visualization.colors import colors_default
from py3plex.visualization.multilayer import hairball_plot
from drawing.drawing_constants import node_size, get_palette, figsize, dpi
from threading import Lock
import matplotlib.pyplot as plt


class MultiLayerHairball():

    def __init__(self, lock: Lock):
        self.lock = lock

    def hairball_layout(self, edge_list, community_list, image_format):
        network, actors, layers = edge_list_to_multi_layer(edge_list)
        actor_to_community, actors, communities = convert_community_list(
            community_list
        )
        colors = self._get_colors(network, actor_to_community)

        self.lock.acquire()

        plt.cla()
        fig = plt.gcf()
        fig.set_dpi(dpi)
        fig.set_size_inches(figsize)
        hairball_plot(
            network.core_network,
            color_list=colors,
            node_size=node_size,
            scale_by_size=True,
            edge_width=0.5
        )

        image_data = None
        if image_format == "svg":
            image_data = fig_to_svg(fig)
        else:
            image_data = fig_to_png(fig)

        self.lock.release()

        return image_data

    def _get_colors(self, network: multi_layer_network, atc: List[ActorToCommunity]):
        colors_count = len(set(i.community for i in atc)) + 1
        palette = get_palette(colors_count)
        atc_dict = dict((i.actor, i.community) for i in atc)
        colors = []
        for n in [n[0] for n in network.get_nodes()]:
            if n in atc_dict:
                c = int(atc_dict[n])
                colors.append(palette[c])
            else:
                colors.append(palette[-1])
        return colors
