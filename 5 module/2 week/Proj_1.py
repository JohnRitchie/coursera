"""
 compute information about the distribution of the in-degrees for nodes in the graphs
"""
EX_GRAPH0 = {0: {1, 2}, 1: set([]), 2: set([])}
EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1},
             5: {2}, 6: set([])}
EX_GRAPH2 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3, 7}, 3: {7}, 4: {1},
             5: {2}, 6: set([]), 7: {3}, 8: {1, 2}, 9: {0, 3, 4, 5, 6, 7}}


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


def in_degree_distribution(digraph):
    """
    computes the unnormalized distribution of the in-degrees of the graph
    """
    distribution = {}
    indegrees = compute_in_degrees(digraph).values()

    for degree in indegrees:
        if degree not in distribution.keys():
            distribution[degree] = 1
        else:
            distribution[degree] += 1

    return distribution


def normalized_distribution(digraph):
    total = sum(digraph.values())
    distribution = {}
    for node in digraph:
        distribution[node] = (float(digraph[node])) / float(total)

    return distribution
