from typing import List
from app import constants
from matplotlib.colors import Normalize
from matplotlib.cm import Blues
from matplotlib.figure import Figure
import squarify


def draw_barplot(
    labels: List[str], x: List[int], xlabel: str, y: List[int], ylabel: str
) -> Figure:
    fig = Figure(figsize=constants.figsize, dpi=constants.dpi)
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.bar(x, y, align="center", tick_label=labels)

    return fig


def draw_treemap(label: List[str], sizes: List[int]) -> Figure:
    norm = Normalize(vmin=min(sizes), vmax=max(sizes))
    colors = [Blues(norm(value)) for value in sizes]
    fig = Figure(figsize=constants.figsize, dpi=constants.dpi)
    ax = fig.add_subplot(1, 1, 1)

    squarify.plot(ax=ax, sizes=sizes, label=label, alpha=0.9, color=colors)

    return fig
