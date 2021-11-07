import matplotlib.pyplot as plt
import random
import time
import alg_cluster
import alg_project3_solution as proj


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
num_clusters = range(2, 200)
time_slow_closest_pair = []
time_fast_closest_pair = []

for num in num_clusters:
    random_clusters_nums = gen_random_clusters(num)
    random_clusters_list = []

    for cluster_nums in random_clusters_nums:
        random_clusters_list.append(alg_cluster.Cluster(set([]), cluster_nums[0], cluster_nums[1], 0, 0))

    start_time = time.clock()
    proj.slow_closest_pair(random_clusters_list)
    end_time = time.clock()
    time_slow_closest_pair.append(end_time - start_time)

    start_time = time.clock()
    proj.fast_closest_pair(random_clusters_list)
    end_time = time.clock()
    time_fast_closest_pair.append(end_time - start_time)

plt.plot(num_clusters, time_slow_closest_pair, '-y', label='slow_closest_pair')
plt.plot(num_clusters, time_fast_closest_pair, '-g', label='fast_closest_pair')
plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
plt.legend(loc='upper left')
plt.title("Slow vs fast closest pair")
plt.ylabel("Time")
plt.xlabel("Number of clusters")
plt.show()
