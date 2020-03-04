from typing import NamedTuple


class Edge(NamedTuple):
    actor_from: int
    layer_from: int
    actor_to: int
    layer_to: int
    weight: int
