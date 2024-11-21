from matplotlib.colors import Colormap
import matplotlib.pyplot as plt


def get_palette(colors_count, cmap: Colormap | str = "gist_rainbow") -> list[Colormap]:
    cm = plt.get_cmap(cmap)
    return [cm(1.0 * i / colors_count) for i in range(colors_count)]
