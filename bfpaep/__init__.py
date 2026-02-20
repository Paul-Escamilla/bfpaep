import itertools
import networkx as nx

def is_hamiltonian_cycle(graph, cycle):
    """Cheks if cycle is a hamiltonian cycle in a graph.
    graph is a netwokx graph, and cycle is a list of verices"""
    n = len(set(cycle))
    if n != graph.order():
        return False
    for i in range(n-1):
        if not graph.has_edge(cycle[i], cycle[i+1]):
            return False
    if not graph.has_edge(cycle[n-1], cycle[0]):
        return False
    return True

def is_hamiltonian(graph):
    """cheks if a graph is hamiltonian.
    graph is a networkx graph"""
    if not nx.is_connected(graph):
        return False
    vertices = list(graph.nodes())
    if len(vertices) < 3:
        return False
    perms = itertools.permutations(vertices)
    for perm in perms:
        if is_hamiltonian_cycle(graph, perm):
            return perm
    return False

def is_proper_coloring(graph, coloring):
    for edge in graph.edges():
        if coloring[edge[0]] == coloring[edge[1]]:
            return False            
    return True

def is_3_colorable(graph):
    n = graph.order()
    colorings = itertools.product([0, 1, 2], repeat = n)
    for coloring in colorings:
        if is_proper_coloring(graph, coloring):
            return coloring
    return False