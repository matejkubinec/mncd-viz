from io import StringIO, BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from drawing.drawing_constants import dpi


def fig_to_png(fig):
    image_data = BytesIO()
    fig.savefig(image_data, format="png", dpi=dpi)
    image_data.seek(0)
    del fig
    return image_data.getvalue()


def fig_to_svg(fig):
    image_data = StringIO()
    fig.savefig(image_data, format="svg", dpi=dpi)
    image_data.seek(0)
    del fig
    return image_data.read()
