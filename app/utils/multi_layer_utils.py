import math


def get_axes(fig, layers):
    nrows = math.ceil(len(layers) / 2.0)
    return fig.subplots(nrows, 2)


def filter_edges(edge, layer):
    return edge.layer_from == layer.index and edge.layer_to == layer.index
