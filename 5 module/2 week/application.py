"""
Provided code for Application portion of Module 1
Imports physics citation graph
"""

import urllib2
import matplotlib.pyplot as plt
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import distribution

codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

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


def make_plot(graph):
    keys = graph.keys()
    values = graph.values()
    plt.plot(keys, values, 'xr')
    plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('In degree distribution of citation in scientific articles')
    plt.xlabel('Number of citation')
    plt.ylabel('Distribution of citation')
    plt.show()


citation_graph = load_graph(CITATION_URL)
distribution = distribution.in_degree_distribution(citation_graph)
normalized_distribution = distribution.normalized_distribution(distribution)
make_plot(normalized_distribution)
