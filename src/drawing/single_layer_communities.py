from typing import List
from models import ActorToCommunity
from networkx.readwrite.edgelist import read_edgelist
from converters import fig_to_png, fig_to_svg, convert_community_list, edge_list_to_single_layer
from drawing.drawing_constants import edge_color, node_color, get_palette, figsize, dpi, black
from matplotlib.figure import Figure
import networkx as nx


def spring_layout_communities(edge_list, community_list, image_format="svg"):
    G, g_actors, layers = edge_list_to_single_layer(edge_list)
    actor_to_community, actors, communities = convert_community_list(
        community_list
    )
    node_colors = _get_node_color(G, actor_to_community)
    node_sizes = _get_node_size(G)
    fig = _get_figure()
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        G,
        ax=ax,
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_colors,
        with_labels=True,
        font_size=9,
        font_family="serif"
    )
    return _get_image(fig, image_format)


def circular_layout_communities(edge_list, community_list, image_format="svg"):
    G, g_actors, layers = edge_list_to_single_layer(edge_list)
    actor_to_community, actors, communities = convert_community_list(
        community_list
    )
    node_colors = _get_node_color(G, actor_to_community)
    node_sizes = _get_node_size(G)
    fig = _get_figure()
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        G,
        ax=ax,
        pos=nx.circular_layout(G),
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_colors,
        with_labels=True,
        font_size=9,
        font_family="serif"
    )
    return _get_image(fig, image_format)


def spiral_layout_communities(edge_list, community_list, image_format="svg"):
    G, g_actors, layers = edge_list_to_single_layer(edge_list)
    actor_to_community, actors, communities = convert_community_list(
        community_list
    )
    node_colors = _get_node_color(G, actor_to_community)
    node_sizes = _get_node_size(G)
    fig = _get_figure()
    ax = fig.add_subplot(1, 1, 1)
    nx.draw(
        G,
        ax=ax,
        pos=nx.spiral_layout(G),
        edge_color=edge_color,
        node_size=node_sizes,
        node_color=node_colors,
        with_labels=True,
        font_size=9,
        font_family="serif"
    )
    return _get_image(fig, image_format)


def _get_figure():
    return Figure(figsize=figsize, dpi=dpi)


def _get_image(fig, image_format):
    if image_format == "svg":
        return fig_to_svg(fig)
    else:
        return fig_to_png(fig)


def _get_node_size(G):
    min_size = 25
    degrees = sorted(nx.degree(G), key=lambda d: d[0])
    return [deg[1] * min_size for deg in degrees]


def _get_node_color(G, atc: List[ActorToCommunity]):
    act_dict = dict((pair.actor, pair.community) for pair in atc)
    colors_count = len(set(i.community for i in atc)) + 1
    palette = get_palette(colors_count)
    colors = list()
    for n in G.nodes():
        if n in act_dict:
            c = int(act_dict[n])
            colors.append(palette[c])
        else:
            colors.append(black)
    return colors
