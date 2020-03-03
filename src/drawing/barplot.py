from converters.build_communities import build_communities
from drawing.drawing_constants import node_color
from converters.plt_to_str import plt_to_str
from converters.plt_to_png import plt_to_png
from matplotlib import cm
import matplotlib.pyplot as plt


def draw_barplot(X, Y, labels, xlabel, ylabel, image_format):
    fig, ax = plt.subplots()

    plt.cla()

    ax.set_xticklabels([""] + labels)
    ax.set_xlabel(xlabel)

    ax.set_ylabel(ylabel)

    ax.bar(
        X,
        Y,
        align="center",
        color=node_color
    )

    if image_format == "svg":
        return plt_to_str(fig)
    else:
        return plt_to_png(fig)
