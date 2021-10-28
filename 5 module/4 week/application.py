import helpers
import provided
import matplotlib.pyplot as plt
import time


###################################
# Question 1
NUMBER_OF_NODES = 1239

computer_network_graph = provided.load_graph(provided.NETWORK_URL)
erdos_renyi_graph = helpers.erdos_renyi(NUMBER_OF_NODES, 0.004)
upa_graph = helpers.upa_graph(NUMBER_OF_NODES, 3)
#
# computer_network_graph_resile = helpers.compute_resilience(computer_network_graph,
#                                                            helpers.random_order(computer_network_graph))
# erdos_renyi_graph_resile = helpers.compute_resilience(erdos_renyi_graph, helpers.random_order(erdos_renyi_graph))
# upa_graph_resile = helpers.compute_resilience(upa_graph, helpers.random_order(upa_graph))
#
# xvals = range(NUMBER_OF_NODES + 1)
# plt.plot(xvals, computer_network_graph_resile, '-y', label='Computer Network Graph')
# plt.plot(xvals, erdos_renyi_graph_resile, '-g', label='Erdos Renyi Graph, p=0.004')
# plt.plot(xvals, upa_graph_resile, '-r', label='UPA Graph, m=3')
# plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
# plt.legend(loc='upper right')
# plt.title("Resilience plot of three graphs")
# plt.ylabel("Size of largest connected component")
# plt.xlabel("Number of nodes removed")
# plt.show()

###################################
# Question 3
# n = range(10, 1000, 10)
# time_targeted_order = []
# time_fast_targeted_order = []
#
# for step in n:
#     upa_graph = helpers.upa_graph(step, 5)
#
#     start_time = time.clock()
#     provided.targeted_order(upa_graph)
#     end_time = time.clock()
#     time_targeted_order.append(end_time - start_time)
#
#     start_time = time.clock()
#     helpers.fast_targeted_order(upa_graph)
#     end_time = time.clock()
#     time_fast_targeted_order.append(end_time - start_time)
#
# plt.plot(n, time_targeted_order, '-y', label='targeted_order')
# plt.plot(n, time_fast_targeted_order, '-g', label='fast_targeted_order')
# plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
# plt.legend(loc='upper left')
# plt.title("Simple vs fast targeted order")
# plt.ylabel("Time")
# plt.xlabel("Number of nodes")
# plt.show()

###################################
# Question 4
computer_network_graph_resile = helpers.compute_resilience(computer_network_graph,
                                                           helpers.fast_targeted_order(computer_network_graph))
erdos_renyi_graph_resile = helpers.compute_resilience(erdos_renyi_graph, helpers.fast_targeted_order(erdos_renyi_graph))
upa_graph_resile = helpers.compute_resilience(upa_graph, helpers.fast_targeted_order(upa_graph))

xvals = range(NUMBER_OF_NODES + 1)
plt.plot(xvals, computer_network_graph_resile, '-y', label='Computer Network Graph')
plt.plot(xvals, erdos_renyi_graph_resile, '-g', label='Erdos Renyi Graph, p=0.004')
plt.plot(xvals, upa_graph_resile, '-r', label='UPA Graph, m=3')
plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
plt.legend(loc='upper right')
plt.title("Resilience plot of three graphs from fast_targeted_order")
plt.ylabel("Size of largest connected component")
plt.xlabel("Number of nodes removed")
plt.show()
