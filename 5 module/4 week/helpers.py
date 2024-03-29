"""
Helpers for the Application 2
"""

from collections import deque
import random
import upa_trial
import provided

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

def make_complete_ugraph(n):
    ugraph = {}
    nodes = range(n)

    for node in nodes:
        ugraph[node] = set(nodes)
        ugraph[node].remove(node)

    return ugraph


def erdos_renyi(n, p):
    ugraph = {}

    for key in range(n):
        ugraph[key] = set([])

    for row in range(n):
        for col in range(row):
            rand = random.random()
            if rand < p:
                 ugraph[row] = ugraph[row].union([col])
                 ugraph[col] = ugraph[col].union([row])
    return ugraph


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


def fast_targeted_order(ugraph):
    new_graph = provided.copy_graph(ugraph)
    degree_sets = {}

    for k in range(len(new_graph)):
        degree_sets[k] = set()

    for key, value in new_graph.items():
        degree = len(value)
        degree_sets[degree].add(key)

    order = []

    for i in range((len(new_graph) - 1), -1, -1):
        while degree_sets[i]:
            node = degree_sets[i].pop()

            for neighbor in new_graph[node]:
                if neighbor in new_graph:
                    degree = len(new_graph[neighbor])
                    if degree and neighbor in degree_sets[degree]:
                        degree_sets[degree].remove(neighbor)
                        degree_sets[degree - 1].add(neighbor)

            order.append(node)
            del new_graph[node]

    return order


# print fast_targeted_order(GRAPH)
