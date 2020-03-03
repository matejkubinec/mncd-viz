from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO


def plt_to_png(plt):
    image_data = BytesIO()
    FigureCanvas(plt).print_png(image_data)
    return image_data.getvalue()
