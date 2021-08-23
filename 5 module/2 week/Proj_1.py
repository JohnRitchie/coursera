"""
TODO:
"""
from simple_draw_graph import draw_graph, draw_di_graph

EX_GRAPH0 = {0: {1, 2}, 1: {}, 2: {}}
EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1},
             5: {2}, 6: {}}
EX_GRAPH2 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3, 7}, 3: {7}, 4: {1},
             5: {2}, 6: {}, 7: {3}, 8: {1, 2}, 9: {0, 3, 4, 5, 6, 7}}


def make_complete_graph(num_nodes):
    """
    make a dictionary
    corresponding to a complete directed graph
    with the specified number of nodes
    """
    complete_graph = {}

    for node in range(num_nodes):
        complete_graph[node] = {i for i in range(num_nodes) if i != node}

    return complete_graph


# print make_complete_graph(5)
# draw_di_graph(make_complete_graph(5))


def compute_in_degrees(digraph):
    """
    computes the in-degrees for the nodes in the graph
    """
    nodes = []
    in_degrees = {}

    for node in digraph:
        nodes.extend(list(digraph[node]))

    for node in digraph:
        in_degrees[node] = nodes.count(node)

    return in_degrees


print compute_in_degrees(make_complete_graph(5))


def in_degree_distribution(digraph):
    """
    :param digraph:
    :return:
    """
    return
