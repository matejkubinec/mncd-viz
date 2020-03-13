from converters.build_communities import build_communities
from drawing.drawing_constants import node_color, get_palette
from converters import fig_to_png, fig_to_svg
from matplotlib.figure import Figure
from matplotlib import cm


def draw_barplot(X, Y, labels, xlabel, ylabel, image_format="svg", params={}):
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)

    color = _get_node_color(X, params)

    ax.set_xticklabels([""] + labels)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.bar(
        X,
        Y,
        align="center",
        color=color
    )

    if image_format == "svg":
        return fig_to_svg(fig)
    else:
        return fig_to_png(fig)


def _get_node_color(X, params):

    if params is None or "color_communities" not in params:
        return node_color
    elif params["color_communities"]:
        community_count = len(X)
        palette = get_palette(community_count)
        return [palette[i] for i in range(community_count)]
