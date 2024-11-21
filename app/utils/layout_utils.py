from app.models import Layout
from networkx import spring_layout, spiral_layout, circular_layout


def get_nx_layout(layout: Layout):
    if layout == Layout.spring:
        return spring_layout
    elif layout == Layout.spiral:
        return spiral_layout
    else:
        return circular_layout
