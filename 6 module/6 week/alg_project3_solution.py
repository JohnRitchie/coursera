"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2)


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    dist, idx1, idx2 = float('inf'), -1, -1

    for cluster in cluster_list:
        for other_cluster in cluster_list:
            if cluster != other_cluster:
                dist, idx1, idx2 = min((dist, idx1, idx2), pair_distance(cluster_list, cluster_list.index(cluster),
                                                                         cluster_list.index(other_cluster)))

    return dist, idx1, idx2


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    len_cluster_list = len(cluster_list)

    if len_cluster_list <= 3:
        return slow_closest_pair(cluster_list)
    else:
        mid = len_cluster_list / 2
        left_cluster_list = cluster_list[:mid]
        right_cluster_list = cluster_list[mid:]
        left_dist, left_idx1, left_idx2 = fast_closest_pair(left_cluster_list)
        right_dist, right_idx1, right_idx2 = fast_closest_pair(right_cluster_list)
        dist, idx1, idx2 = min((left_dist, left_idx1, left_idx2), (right_dist, right_idx1 + mid, right_idx2 + mid))
        mid = 0.5 * (cluster_list[mid].horiz_center() + cluster_list[mid - 1].horiz_center())
        dist, idx1, idx2 = min((dist, idx1, idx2), closest_pair_strip(cluster_list, mid, dist))

    return dist, idx1, idx2


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """
    strip_list = [cluster for cluster in cluster_list if abs(cluster.horiz_center() - horiz_center) < half_width]
    strip_list.sort(key=lambda cluster: cluster.vert_center())
    len_strip_list = len(strip_list)
    dist, idx1, idx2 = float('inf'), -1, -1

    if len(cluster_list):
        for idx_cluster in range(len_strip_list - 1):
            for idx_other_cluster in range(idx_cluster + 1, min(idx_cluster + 3, len_strip_list)):
                dist, idx1, idx2 = min((dist, idx1, idx2),
                                       pair_distance(cluster_list, cluster_list.index(strip_list[idx_cluster]),
                                                     cluster_list.index(strip_list[idx_other_cluster])))

    return dist, idx1, idx2


# c0 = alg_cluster.Cluster([], 1, 1, 0, 0)
# c1 = alg_cluster.Cluster([], 5, 18, 0, 0)
# c2 = alg_cluster.Cluster([], 3, 3, 0, 0)
# c3 = alg_cluster.Cluster([], 7, 20, 0, 0)
# c4 = alg_cluster.Cluster([], 4, 4, 0, 0)
# c_list = [c0, c1, c2, c3, c4]
# c_list.sort(key=lambda cluster: cluster.horiz_center())
# print slow_closest_pair(c_list)
# print fast_closest_pair(c_list)
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    return []


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations

    return []
