from node import Node, RoadMap
import math


def build_node(estim_g, estim_h, liste_som, next_nodes):
    return Node(estim_g, estim_h, liste_som, next_nodes)


def compute_h():
    return 0


def develop_node(node, r_map):
    nodes = []
    visited = node.liste_som
    total_cities = r_map.cities
    for i in total_cities:
        if i not in visited:
            movement_cost = r_map.edges[node.current_city][i]

            new_liste_som = node.liste_som + [i]
            new_estim_g = node.estim_g + movement_cost
            new_estim_h = compute_h()

            new_node = build_node(new_estim_g, new_estim_h, new_liste_som, [])

            node.next_nodes.append(new_node)
            nodes.append(new_node)

    return nodes


def grp_size(nb_cities):
    size = 0
    for i in range(1, nb_cities+1):
        size += math.factorial(nb_cities-1)/math.factorial(nb_cities-i)
    size += math.factorial(nb_cities - 1)
    return size
