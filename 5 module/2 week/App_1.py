"""
Provided code for Application portion of Module 1
Imports physics citation graph
"""

import urllib2
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import simpleplot
from simple_draw_graph import draw_di_graph
import Proj_1

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
    graph_lines = graph_lines[: 20]  #TODO

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


citation_graph = load_graph(CITATION_URL)
# draw_di_graph(citation_graph)
distribution = Proj_1.in_degree_distribution(citation_graph)
normalized_distribution = Proj_1.normalized_distribution(distribution)
# print normalized_distribution
# simpleplot.plot_lines('Todo1', 1000, 400, 'Todo2', 'Todo3', [normalized_distribution])
