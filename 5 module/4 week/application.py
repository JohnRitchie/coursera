import helpers
import provided
import matplotlib.pyplot as plt


###################################
# Question 1
computer_network_graph = provided.load_graph(provided.NETWORK_URL)
erdos_renyi_graph = helpers.erdos_renyi(1239, 0.004)
upa_graph = helpers.upa_graph(1239, 3)

computer_network_graph_resile = helpers.compute_resilience(computer_network_graph,
                                                           helpers.random_order(computer_network_graph))
erdos_renyi_graph_resile = helpers.compute_resilience(erdos_renyi_graph, helpers.random_order(erdos_renyi_graph))
upa_graph_resile = helpers.compute_resilience(upa_graph, helpers.random_order(upa_graph))


x_values = range(1240)
plt.plot(x_values, computer_network_graph_resile, '-y', label='Computer Network Graph')
plt.plot(x_values, erdos_renyi_graph_resile, '-g', label='Erdos Renyi Graph, P=0.004')
plt.plot(x_values, upa_graph_resile, '-r', label='UPA Graph, m=3')
plt.grid(which="major", linestyle="--", color="gray", linewidth=0.8)
plt.legend(loc='upper right')
plt.title("Resilience")
plt.ylabel("Size of largest connected component")
plt.xlabel("Number of nodes removed")
plt.show()
###################################
