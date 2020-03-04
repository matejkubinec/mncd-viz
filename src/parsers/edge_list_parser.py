from models import Actor, Edge, Layer
from typing import List


class EdgeListParser():

    def parse_edge_list(self, edge_list: str) -> (List[Edge], List[Actor], List[Layer]):
        lines = edge_list.split("\n")
        edges: List[Edge] = []
        actors: List[Actor] = []
        layers: List[Layer] = []

        reading = "edges"
        for line in lines:

            if line.startswith("# Actors"):
                reading = "actors"
                continue
            elif line.startswith("# Layers"):
                reading = "layers"
                continue
            elif line == "":
                break

            if reading == "edges":
                splitted = line.split(" ")

                if len(splitted) == 2:
                    f, t = [int(v) for v in splitted]
                    edges.append(Edge(f, 0, t, 0, 1))

                elif len(splitted) == 5:
                    f, lf, t, lt, w = [int(v) for v in splitted]
                    edges.append(Edge(f, lf, t, lt, w))

            if reading == "actors":
                splitted = line.split(" ")

                if len(splitted) == 2:
                    (a, n) = splitted
                    actors.append(Actor(int(a), n))

            if reading == "layers":
                splitted = line.split(" ")

                if len(splitted) == 2:
                    (l, n) = splitted
                    layers.append(Layer(int(l), n))

        return edges, actors, layers
