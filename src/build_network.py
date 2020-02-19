from py3plex.core import multinet


def build_network(edgelist):
    N = multinet.multi_layer_network()

    lines = edgelist.splitlines()
    edges = [line.split(" ") for line in lines]

    N.add_edges(edges, input_type="list")

    return N
