import matplotlib.pyplot as plt


def get_palette(colors_count):
    cm = plt.get_cmap("gist_rainbow")
    return [cm(1.*i/colors_count) for i in range(colors_count)]


edge_color = "#c4c4c4"
node_color = "#02aff9"
black = (0.0, 0.0, 0.0, 1.0)
node_size = 10

figsize = (8, 8)
dpi = 200
