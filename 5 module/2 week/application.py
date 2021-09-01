"""
Provided code for Application portion of Module 1
Imports physics citation graph
"""

import urllib2
import networkx as nx
from itertools import combinations
import random
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import distribution
import plot_graph
import dpa_trial

codeskulptor.set_timeout(20)

###################################
# Question 1

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


# citation_graph = load_graph(CITATION_URL)
# disted_graph = distribution.in_degree_distribution(citation_graph)
# normalized_disted_graph = distribution.normalized_distribution(disted_graph)
# plot_graph.make_plot(normalized_disted_graph, 'In degree distribution of citation in scientific articles',
#                      'Number of citation', 'Distribution of citation')

###################################
# Question 2


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


# random_graph = erdos_renyi(27770, 0.0005)
# disted_graph = distribution.in_degree_distribution(random_graph)
# normalized_disted_graph = distribution.normalized_distribution(disted_graph)
# plot_graph.make_plot(normalized_disted_graph, 'In degree distribution for the erdos renyi graph',
#                      'Number of edges (log)', 'Fraction of nodes (log)')
# plot_graph.make_plot(normalized_disted_graph, 'In degree distribution for the erdos renyi graph',
#                      'Number of edges', 'Fraction of nodes', False)

###################################
# Question 4

def make_complete_dpa_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary
    corresponding to a complete directed graph with the specified
    number of nodes.
    """
    graph = {}
    dpa = dpa_trial.DPATrial(num_nodes)

    for node in range(num_nodes):
        graph[node] = dpa.run_trial(num_nodes)

    return graph


def dpa_graph(n, m):

    complete_dpa_graph = make_complete_dpa_graph(m)
    dpa_graph = dpa_trial.DPATrial(m)

    for i in range(m, n):
        complete_dpa_graph[i] = dpa_graph.run_trial(m)

    return complete_dpa_graph


# random_graph = dpa_graph(27770, 12)
# disted_graph = distribution.in_degree_distribution(random_graph)
# normalized_disted_graph = distribution.normalized_distribution(disted_graph)
# plot_graph.make_plot(normalized_disted_graph, 'In degree distribution for the DPA graph',
#                      'Number of edges (log)', 'Fraction of nodes (log)')
# plot_graph.make_plot(normalized_disted_graph, 'In degree distribution for the DPA graph',
#                      'Number of edges', 'Fraction of nodes', False)
