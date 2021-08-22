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

    list_nodes = range(num_nodes)

    for node in range(num_nodes):
        tmp_list = list_nodes[:]
        tmp_list.remove(node)
        complete_graph[node] = set(tmp_list)

    return complete_graph


print make_complete_graph(5)
draw_di_graph(make_complete_graph(5))


def compute_in_degrees(digraph):
    """
    :param digraph:
    :return:
    """
    return


def in_degree_distribution(digraph):
    """
    :param digraph:
    :return:
    """
    return
