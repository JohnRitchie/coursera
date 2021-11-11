import matplotlib.pyplot as plt
import random
import time
import alg_cluster
import alg_project3_solution as proj
import alg_project3_viz


def gen_random_clusters(num_clusters):
    """
    creates a list of clusters where each cluster in this list corresponds to one randomly generated point
    in the square with corners +-1, +-1
    """
    cluster_list = []

    for _ in range(num_clusters):
        coords = tuple(random.random() * random.choice([-1, 1]) for x in range(2))
        cluster_list.append(coords)

    return cluster_list


###################################
# Question 1
# num_clusters = range(2, 200)
# time_slow_closest_pair = []
# time_fast_closest_pair = []
#
# for num in num_clusters:
#     random_clusters_nums = gen_random_clusters(num)
#     random_clusters_list = []
#
#     for cluster_nums in random_clusters_nums:
#         random_clusters_list.append(alg_cluster.Cluster(set([]), cluster_nums[0], cluster_nums[1], 0, 0))
#
#     start_time = time.clock()
#     proj.slow_closest_pair(random_clusters_list)
#     end_time = time.clock()
#     time_slow_closest_pair.append(end_time - start_time)
#
#     start_time = time.clock()
#     proj.fast_closest_pair(random_clusters_list)
#     end_time = time.clock()
#     time_fast_closest_pair.append(end_time - start_time)
#
# plt.plot(num_clusters, time_slow_closest_pair, '-y', label='slow_closest_pair')
# plt.plot(num_clusters, time_fast_closest_pair, '-g', label='fast_closest_pair')
# plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
# plt.legend(loc='upper left')
# plt.title("Slow vs fast closest pair")
# plt.ylabel("Time")
# plt.xlabel("Number of clusters")
# plt.show()

###################################
# Question 7
def compute_distortion(cluster_list, cluster_table):
    dist = 0

    for cluster in cluster_list:
        dist += cluster.cluster_error(cluster_table)

    return dist


def make_singleton_list(cluster_table):
    s_list = list()

    for line in cluster_table:
        s_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    return s_list


# data_table = alg_project3_viz.load_data_table(alg_project3_viz.DATA_111_URL)
#
# singleton_list = make_singleton_list(data_table)
# cluster_list_hierarchical = proj.hierarchical_clustering(singleton_list, 9)
# print compute_distortion(cluster_list_hierarchical, data_table)
#
# singleton_list = make_singleton_list(data_table)
# cluster_list_kmeans = proj.kmeans_clustering(singleton_list, 9, 5)
# print compute_distortion(cluster_list_kmeans, data_table)

###################################
# Question 10
data_table = alg_project3_viz.load_data_table(alg_project3_viz.DATA_111_URL)
num_clusters = range(6, 21)
kmeans_distortion_list = []
hierarchical_distortion_list = []

for clusters in num_clusters:
    singleton_list = make_singleton_list(data_table)
    distortion = compute_distortion(proj.kmeans_clustering(singleton_list, clusters, 5), data_table)
    kmeans_distortion_list.append(distortion/(10**10))

    singleton_list = make_singleton_list(data_table)
    distortion = compute_distortion(proj.hierarchical_clustering(singleton_list, clusters), data_table)
    hierarchical_distortion_list.append(distortion/(10**10))

plt.plot(num_clusters, kmeans_distortion_list, '-y', label='kmeans_clustering')
plt.plot(num_clusters, hierarchical_distortion_list, '-g', label='hierarchical_clustering')
plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
plt.legend(loc='upper left')
plt.title("Distortion (111 points)")
plt.ylabel("Distortion / 10**10")
plt.xlabel("num_clusters")
plt.show()
