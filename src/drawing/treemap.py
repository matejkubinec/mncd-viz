from converters.build_communities import build_communities
from converters.plt_to_str import plt_to_str
from converters.plt_to_png import plt_to_png
from matplotlib.colors import Normalize
from matplotlib.cm import Blues
import matplotlib.pyplot as plt
import squarify


def draw_treemap(sizes, label, image_format):
    cmap = Blues
    mini = min(sizes)
    maxi = max(sizes)
    norm = Normalize(vmin=mini, vmax=maxi)
    colors = [cmap(norm(value)) for value in sizes]

    fig, ax = plt.subplots()

    squarify.plot(
        ax=ax,
        sizes=sizes,
        label=label,
        alpha=0.9,
        color=colors
    )

    if image_format == "svg":
        return plt_to_str(fig)
    else:
        return plt_to_png(fig)
