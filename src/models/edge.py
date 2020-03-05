from typing import NamedTuple


class Edge(NamedTuple):
    actor_from: int
    layer_from: int
    actor_to: int
    layer_to: int
    weight: int

    def to_list(self):
        return [
            self.actor_from,
            self.layer_from,
            self.actor_to,
            self.layer_to,
            self.weight
        ]
