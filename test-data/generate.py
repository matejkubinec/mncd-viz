from networkx.readwrite.edgelist import write_edgelist
from networkx.generators.classic import complete_graph, cycle_graph
from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import math

print('Starting generation...')

N = [3, 4, 5, 10, 20]

for n in N:
    G = complete_graph(n)
    filename = f'complete-{n}.edgelist'
    write_edgelist(G, filename, data=False)

    G = cycle_graph(n)
    filename = f'circulant-{n}.edgelist'
    write_edgelist(G, filename, data=False)

    G = erdos_renyi_graph(n, 0.4)
    filename = f'erdos_renyi-{n}.edgelist'
    write_edgelist(G, filename, data=False)

print('Generation complete!')