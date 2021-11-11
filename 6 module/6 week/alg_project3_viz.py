"""
Example code for creating and visualizing
cluster of county-based cancer risk data
"""

import math
import urllib2
import time

import alg_cluster
import alg_project3_solution
import alg_clusters_matplotlib

###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"
DATA_SIZE = DATA_111_URL
CLUSTERING_NAME = "sequential_clustering"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering

    Note that method may return num_clusters or num_clusters + 1 final clusters
    """

    cluster_list = []
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters) / num_clusters

    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
                math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)

    return cluster_list


#####################################################################
# Code to load cancer data, compute a clustering and
# visualize the results


def run_example():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters
    """
    data_table = load_data_table(DATA_SIZE)
    singleton_list = []

    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    start_time = time.clock()

    if CLUSTERING_NAME == "sequential_clustering":
        cluster_list = sequential_clustering(singleton_list, 15)
    elif CLUSTERING_NAME == "hierarchical_clustering":
        cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, 9)
    elif CLUSTERING_NAME == "kmeans_clustering":
        cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, 15, 5)

    end_time = time.clock()
    print end_time - start_time

    print "Displaying", len(cluster_list), CLUSTERING_NAME
    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)


if __name__ == "__main__":
    run_example()
