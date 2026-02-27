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

from typing import Sequence
def sum_of_values(value_list, keys):
    """
    Calculates the sum of values from a list based on a binary key sequence.

    Args:
        value_list (list): A list of numerical values.
        keys (Sequence): A sequence of 0s and 1s, where 1 indicates inclusion of
        the corresponding value from value_list.

    Returns:
        int or float: The sum of the selected values.
    """
    sum = 0
    n = len(value_list)
    for i in range(n):
        sum += value_list[i]*keys[i]
    return sum

def knapsack_bf(value_list, weiht_list, value_goal, weigth_goal):
    """
    Solves the knapsack problem using a brute-force approach.
    It tries to find a subset of objects that meets a minimum value goal
    and stays within a maximum weight goal.

    Args:
        value_list (list): A list of values for each object.
        weiht_list (list): A list of weights for each object.
        value_goal (int or float): The minimum total value required.
        weigth_goal (int or float): The maximum total weight allowed.

    Returns:
        tuple or bool: A tuple representing the binary selection (0 for not
        included, 1 for included)
                       of objects if a valid subset is found, otherwise False.
    """
    n = len(value_list)
    sequences = itertools.product([0, 1], repeat=n)
    for sequence in sequences:
        if sum_of_values(value_list, sequence) >= value_goal:
            if sum_of_values(weiht_list, sequence) <= weigth_goal:
                return sequence
    return False