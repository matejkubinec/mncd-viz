from io import StringIO, BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def fig_to_png(fig):
    image_data = BytesIO()
    fig.savefig(image_data, format="png")
    image_data.seek(0)
    return image_data.getvalue()


def fig_to_svg(fig):
    image_data = StringIO()
    fig.savefig(image_data, format="svg")
    image_data.seek(0)
    return image_data.read()
