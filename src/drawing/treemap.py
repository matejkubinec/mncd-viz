from converters.build_communities import build_communities
from converters.plt_to_str import plt_to_str
from matplotlib.colors import Normalize
from matplotlib.cm import Blues
import matplotlib.pyplot as plt
import squarify


def draw_treemap(sizes, label):
    cmap = Blues
    mini=min(sizes)
    maxi=max(sizes)
    norm = Normalize(vmin=mini, vmax=maxi)
    colors = [cmap(norm(value)) for value in sizes]

    plt.cla()
    squarify.plot(
        sizes=sizes,
        label=label,
        alpha=0.9,
        color=colors
    )
    plt.axis("off")

    return plt_to_str(plt)
