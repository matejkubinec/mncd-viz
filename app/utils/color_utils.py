from app.theme.palette import get_palette
from app.models import ActorToCommunity, Community
from app import constants
import networkx as nx


def get_layer_colors(
    act: list[ActorToCommunity],
    communities: list[Community],
    nodes: nx.reportviews.NodeView,
):
    palette = get_palette(len(communities))
    act_dict = dict((ac.actor, ac.community) for ac in act)
    return [palette[act_dict[n]] if n in act_dict else constants.black for n in nodes]
