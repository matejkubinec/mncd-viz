from converters.build_communities import build_communities
from converters import fig_to_png, fig_to_svg
from matplotlib.colors import Normalize
from matplotlib.cm import Blues
from matplotlib.figure import Figure
import squarify


def draw_treemap(sizes, label, image_format):
    cmap = Blues
    mini = min(sizes)
    maxi = max(sizes)
    norm = Normalize(vmin=mini, vmax=maxi)
    colors = [cmap(norm(value)) for value in sizes]

    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)

    squarify.plot(
        ax=ax,
        sizes=sizes,
        label=label,
        alpha=0.9,
        color=colors
    )

    if image_format == "svg":
        return fig_to_svg(fig)
    else:
        return fig_to_png(fig)
