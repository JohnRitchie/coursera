from collections import deque
import random


GRAPH = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1}, 5: {2}, 6: set([])}


def bfs_visited(ugraph, start_node):
    assert start_node in ugraph, 'Start node not in graph!'

    queue = deque()
    visited = {start_node}
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


# print bfs_visited(GRAPH, 5)


def cc_visited(ugraph):
    remain_node = set(ugraph.keys())
    component_list = []

    while remain_node:
        node = random.choice(tuple(remain_node))
        visited = bfs_visited(ugraph, node)
        component_list.append(visited)
        remain_node = remain_node - visited

    return component_list


# print cc_visited(GRAPH)


def largest_cc_size(ugraph):
    return max([len(item) for item in cc_visited(ugraph)])


# print largest_cc_size(GRAPH)
