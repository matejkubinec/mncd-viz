from py3plex.visualization.colors import all_color_names, colors_default
from converters.build_network import build_network
from converters.build_communities import build_communities
from converters import fig_to_png, fig_to_svg, edge_list_to_multi_layer
from drawing.drawing_constants import node_size, figsize, dpi
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from threading import Lock


class MultiLayerDiagonal():

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
