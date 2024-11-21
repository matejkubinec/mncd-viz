from io import StringIO, BytesIO
from app import constants


def to_png(fig) -> bytes:
    image_data = BytesIO()
    fig.savefig(image_data, format="png", dpi=constants.dpi, transparent=True)
    image_data.seek(0)
    del fig
    return image_data.getvalue()


def to_svg(fig) -> str:
    image_data = StringIO()
    fig.savefig(image_data, format="svg", dpi=constants.dpi, transparent=True)
    image_data.seek(0)
    del fig
    return image_data.read()
