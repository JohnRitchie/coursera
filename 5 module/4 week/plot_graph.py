"""
Graphs for Module 2
"""

import matplotlib.pyplot as plt


def make_plot(graph, title='', xlabel='', ylabel='', log=True):
    keys = graph.keys()
    values = graph.values()
    plt.plot(keys, values, 'xr')
    plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
    if log:
        plt.xscale('log')
        plt.yscale('log')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
