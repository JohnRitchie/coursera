"""
Provided code for Application portion of Module 1
Imports physics citation graph
"""

import urllib2
import matplotlib.pyplot as plt
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
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


citation_graph = load_graph(CITATION_URL)
distribution = Proj_1.in_degree_distribution(citation_graph)
normalized_distribution = Proj_1.normalized_distribution(distribution)

for key, value in normalized_distribution.items():
    x = key
    y = value
    plt.scatter(x, y)

plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1, 1000)
plt.title('Normalized in-degree distribution of citation \n in high energy physics theory papers\n')
plt.ylabel('Distribution of citation (normalized)')
plt.xlabel('Number of papers')
plt.show()
