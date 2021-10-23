"""
Helpers for the Application 2
"""

from collections import deque
import random
import networkx as nx
from itertools import combinations
import upa_trial

GRAPH = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1}, 5: {2}, 6: set([])}


def bfs_visited(ugraph, start_node):
    """returns the set consisting of all nodes that are visited by a breadth-first search that starts at start_node"""
    assert start_node in ugraph, 'Start node not in graph!'

    queue = deque()
    visited = {start_node}
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


# print bfs_visited(GRAPH, 5)


def cc_visited(ugraph):
    """returns a list of sets, where each set consists of all the nodes (and nothing else) in a connected component"""
    remain_node = set(ugraph.keys())
    component_list = []

    while remain_node:
        node = random.choice(tuple(remain_node))
        visited = bfs_visited(ugraph, node)
        component_list.append(visited)
        remain_node = remain_node - visited

    return component_list


# print cc_visited(GRAPH)


def largest_cc_size(ugraph):
    """returns the size (an integer) of the largest connected component in ugraph"""
    try:
        return max([len(item) for item in cc_visited(ugraph)])
    except ValueError:
        return 0


# print largest_cc_size(GRAPH)

def compute_resilience(ugraph, attack_order):
    """
    returns a list whose k + 1k+1th entry is the size of the largest connected component
    in the graph after the removal of the first k nodes in attack_order
    """
    resilience = [largest_cc_size(ugraph)]

    for item in attack_order:
        ugraph.pop(item)
        for node in ugraph:
            ugraph[node].discard(item)
        resilience.append(largest_cc_size(ugraph))

    return resilience


# print compute_resilience(GRAPH, [1, 4, 5])

def make_complete_ugraph(num_nodes):
    ugraph = {}
    nodes = range(num_nodes)

    for node in nodes:
        ugraph[node] = set(nodes)
        ugraph[node].remove(node)

    return ugraph


def erdos_renyi(n, p):
    vertex = set([v for v in range(n)])
    edge = set()
    for combination in combinations(vertex, 2):
        a = random.random()
        if a < p:
            edge.add(combination)

    graph = nx.Graph()
    graph.add_nodes_from(vertex)
    graph.add_edges_from(edge)

    return graph


def upa_graph(n, m):
    complete_ugraph = make_complete_ugraph(m)
    upa = upa_trial.UPATrial(m)

    for i in range(m, n):
        complete_ugraph[i] = upa.run_trial(m)

    for key, values in complete_ugraph.items():
        for value in values:
            complete_ugraph[value].add(key)

    return complete_ugraph


def random_order(graph):
    nodes = graph.keys()
    random.shuffle(nodes)
    return nodes
