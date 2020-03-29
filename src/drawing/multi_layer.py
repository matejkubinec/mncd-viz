from py3plex.visualization.colors import all_color_names, colors_default
from converters.build_network import build_network
from converters.build_communities import build_communities
from converters import edge_list_to_single_layer
from converters import fig_to_png, fig_to_svg, edge_list_to_multi_layer
from parsers import EdgeListParser
from drawing.drawing_constants import edge_color, node_color, figsize, dpi, get_palette, node_size
from matplotlib.figure import Figure
from threading import Lock
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math


class MultiLayerLayouts():

    def __init__(self, lock: Lock):
        self.lock = lock

    def diagonal_layout(self, edge_list, image_format="svg"):
        network, actors, layers = edge_list_to_multi_layer(edge_list)

        parameters_layers = {
            "node_size": 10,
            "alphalevel": 0.1
        }

        if len(layers) > 0:
            labels = [l.name for l in layers]
            parameters_layers["labels"] = labels

        parameters_multiedges = {
            "alphachannel": 0.5
        }

        self.lock.acquire()

        plt.cla()
        fig: Figure = plt.gcf()
        fig.set_dpi(dpi)
        fig.set_size_inches(figsize)
        network.visualize_network(
            style="diagonal",
            parameters_multiedges=parameters_multiedges,
            parameters_layers=parameters_layers
        )

        image_data = None
        if image_format == "svg":
            image_data = fig_to_svg(fig)
        else:
            image_data = fig_to_png(fig)

        self.lock.release()

        return image_data

    def slices(self, edge_list: str, image_format: str = "svg"):
        parser = EdgeListParser()
        edges, actors, layers = parser.parse_edge_list(edge_list)

        fig = self._get_figure(layers)
        axes = self._get_axes(fig, layers)
        palette = self._get_palette(layers)

        if len(layers) > 2 and len(layers) % 2 == 1:
            r = int((len(layers) - 1) / 2)
            c = int(len(layers) % 2)
            axes[r, c].axis("off")
        else:
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

            nx.draw(
                G,
                ax=ax,
                label=l.name,
                node_color=[palette[i]],
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

    def _filter_edges(self, edge, layer):
        return edge.layer_from == layer.index and edge.layer_to == layer.index

    def _get_figure(self, layers):
        return Figure(figsize=(8, 2 * len(layers)), dpi=dpi)

    def _get_axes(self, fig, layers):
        nrows = math.ceil(len(layers) / 2.0)
        return fig.subplots(nrows, 2)

    def _get_palette(self, layers):
        palette = get_palette(len(layers))
        return palette

    def _get_node_size(self, G):
        min_size = node_size
        degrees = sorted(nx.degree(G), key=lambda d: d[0])
        return [deg[1] * min_size for deg in degrees]
