from converters.build_communities import build_communities
from drawing.drawing_constants import node_color, get_palette, figsize, dpi
from converters import fig_to_png, fig_to_svg
from matplotlib.figure import Figure
from matplotlib import cm


def draw_barplot(X, Y, labels, xlabel, ylabel, image_format="svg", params={}):
    fig = _get_figure()
    ax = fig.add_subplot(1, 1, 1)

    color = _get_node_color(X, params)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.bar(
        X,
        Y,
        align="center",
        tick_label=labels,
        color=color
    )

    if image_format == "svg":
        return fig_to_svg(fig)
    else:
        return fig_to_png(fig)


def _get_figure():
    return Figure(figsize=figsize, dpi=dpi)


def _get_node_color(X, params):

    if params is None or "color_communities" not in params:
        return node_color
    elif params["color_communities"]:
        community_count = len(X)
        palette = get_palette(community_count + 1)
        return [palette[i] for i in range(community_count)]
