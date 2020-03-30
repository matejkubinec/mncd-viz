from typing import List
from models import ActorToCommunity
from py3plex.core.multinet import multi_layer_network
from converters.build_network import build_network
from converters.build_communities import build_communities
from converters import fig_to_png, fig_to_svg, edge_list_to_multi_layer, convert_community_list
from py3plex.visualization.colors import colors_default
from py3plex.visualization.multilayer import hairball_plot
from drawing.drawing_constants import node_size, get_palette, figsize, dpi
from parsers import EdgeListParser, CommunityListParser
from matplotlib.figure import Figure
from threading import Lock
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math


class MultiLayerCommunitiesLayouts():

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

    def slices(self, edge_list: str, community_list: str, image_format: str = "svg"):
        parser = EdgeListParser()
        edges, actors, layers = parser.parse_edge_list(edge_list)

        parser = CommunityListParser()
        act, actors, communities = parser.parse_community_list(community_list)

        fig = self._get_figure(layers)
        axes = self._get_axes(fig, layers)
        palette = self._get_palette(communities)

        if len(layers) > 2 and len(layers) % 2 == 1:
            r = int((len(layers) - 1) / 2)
            c = int(len(layers) % 2)
            axes[r, c].axis("off")
        elif len(layers) == 1:
            axes[1].axis("off")

        for i, l in enumerate(layers):
            layer_edges = filter(lambda e: self._filter_edges(e, l), edges)
            r = int(i / 2)
            c = int(i % 2)

            ax = None
            if len(layers) > 2:
                ax = axes[r, c]
            else:
                ax = axes[c]

            ax.set_title(l.name)

            G = build_network(layer_edges, actors)
            node_size = self._get_node_size(G)
            node_color = self._layer_colors(palette, act, G.nodes())

            nx.draw(
                G,
                ax=ax,
                label=l.name,
                node_color=node_color,
                node_size=node_size,
                font_size=9,
                font_family="serif",
                with_labels=True
            )

        image_data = None
        if image_format == "svg":
            image_data = fig_to_svg(fig)
        else:
            image_data = fig_to_png(fig)
        return image_data

    def _layer_colors(self, palette, act, nodes):
        act_dict = dict((ac.actor, ac.community) for ac in act)
        return [palette[act_dict[n]] for n in nodes]

    def _filter_edges(self, edge, layer):
        return edge.layer_from == layer.index and edge.layer_to == layer.index

    def _get_figure(self, layers):
        return Figure(figsize=(8, 2 * len(layers)), dpi=dpi)

    def _get_axes(self, fig, layers):
        nrows = math.ceil(len(layers) / 2.0)
        return fig.subplots(nrows, 2)

    def _get_palette(self, communities):
        palette = get_palette(len(communities))
        return palette

    def _get_node_size(self, G):
        min_size = node_size
        degrees = sorted(nx.degree(G), key=lambda d: d[0])
        return [deg[1] * min_size for deg in degrees]
