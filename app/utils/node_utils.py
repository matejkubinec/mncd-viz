from networkx import Graph, degree

from app import constants
from app.theme.palette import get_palette
from app.models import ActorToCommunity


def get_node_sizes(graph: Graph) -> list[int]:
    min_size = 25
    degrees = sorted(degree(graph), key=lambda d: d[0])
    return [deg[1] * min_size for deg in degrees]


def get_node_colors(graph, atc: list[ActorToCommunity]):
    act_dict = dict((pair.actor, pair.community) for pair in atc)
    colors_count = len(set(i.community for i in atc)) + 1
    palette = get_palette(colors_count)
    colors = list()
    for n in graph.nodes():
        if n in act_dict:
            c = int(act_dict[n])
            colors.append(palette[c])
        else:
            colors.append(constants.black)
    return colors
