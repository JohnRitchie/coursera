# import matplotlib.pyplot as plt
import random
# import alg_cluster
# import alg_project3_solution


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


print gen_random_clusters(5)
