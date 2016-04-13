from node import Node, RoadMap
import math
import heapq


def build_node(road_map, old_node, new_city, next_nodes):
    movement_cost = road_map.edges[old_node.current_city][new_city]
    liste_som = old_node.liste_som + [new_city]
    estim_g = old_node.estim_g + movement_cost
    estim_h = h_local_min(road_map, new_city)

    node = Node(estim_g, estim_h, liste_som, next_nodes)

    if len(liste_som) == road_map.nb_cities:
        leaf = build_node(road_map, node, node.liste_som[0], [])
        node.next_nodes.append(leaf)

    return node


def h_zero():
    return 0


def h_kruskal(road_map, visited):
    cities = road_map.cities

    n = len(cities) - len(visited)


def h_local_min(road_map, current_city):
    distances = road_map.edges[current_city]
    return min(distances)


def h_edges_min(road_map, visited):
    sum_distance = 0
    cities = road_map.cities
    for i in cities:
        if i not in visited:
            sum_distance += min(road_map.edges[i])
    return sum_distance


def develop_node(road_map, node):
    if len(node.next_nodes) > 0:
        return []

    nodes = []
    visited = node.liste_som
    total_cities = road_map.cities
    for i in total_cities:
        if i not in visited:
            new_node = build_node(road_map, node, i, [])
            node.next_nodes.append(new_node)
            nodes.append(new_node)
    return nodes


def grp_size(nb_cities):
    size = 0
    for i in range(1, nb_cities + 1):
        size += math.factorial(nb_cities - 1) / math.factorial(nb_cities - i)
    size += math.factorial(nb_cities - 1)
    return size


# FIXME so hard
def a_star(road_map, start_city):
    open_heap = []

    start_node = Node(0, h_local_min(road_map, start_city), [start_city], [])
    heapq.heappush(open_heap, (start_node.estim_f, start_node))

    while len(open_heap) > 0:
        n = heapq.heappop(open_heap)[1]
        if n.length == road_map.nb_cities + 1:
            print('Succès !')
            return open_heap
        else:
            heirs = develop_node(road_map, n)
            for heir in heirs:
                print(open_heap, (heir.estim_f, heir))
                heapq.heappush(open_heap, (heir.estim_f, heir))

    print('Echec !')
