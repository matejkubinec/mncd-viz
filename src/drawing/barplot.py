from converters.build_communities import build_communities
from drawing.drawing_constants import node_color
from converters import fig_to_png, fig_to_svg
from matplotlib.figure import Figure
from matplotlib import cm


def draw_barplot(X, Y, labels, xlabel, ylabel, image_format="svg"):
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)

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
        return fig_to_svg(fig)
    else:
        return fig_to_png(fig)
