from node import Node, RoadMap
import math


def build_node(road_map, old_node, new_city, next_nodes):
    movement_cost = road_map.edges[old_node.current_city][new_city]
    liste_som = old_node.liste_som + [new_city]
    estim_g = old_node.estim_g + movement_cost
    estim_h = h_local_min(road_map, new_city)
    return Node(estim_g, estim_h, liste_som, next_nodes)


def h_zero():
    return 0


def h_kruskal():
    return 0


def h_local_min(road_map, current_city):
    distances = road_map.edges[current_city]
    return min(distances)


def h_edges_min(road_map, node):
    visited = node.liste_som
    sum_distance = 0
    cities = road_map.cities
    for i in cities:
        if i not in visited:
            sum_distance += min(road_map.edges[i])
    return sum_distance


def develop_node(road_map, node):
    nodes = []
    visited = node.liste_som
    total_cities = road_map.cities
    for i in total_cities:
        if i not in visited:
            new_node = build_node(road_map, node, i, [])
            node.next_nodes.append(new_node)
            nodes.append(new_node)
        # TODO création des feuilles -> if len(new_node.liste_som) == len(total_cities):
            # TODO  build_node(....) (build feuille)

    return nodes


def grp_size(nb_cities):
    size = 0
    for i in range(1, nb_cities + 1):
        size += math.factorial(nb_cities - 1) / math.factorial(nb_cities - i)
    size += math.factorial(nb_cities - 1)
    return size
