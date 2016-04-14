from node import Node, RoadMap
import math
import heapq


def build_start_node(road_map, start_city, heuristic_code):
    if heuristic_code == 0:
        return Node(0, h_zero(), [start_city], [])

    elif heuristic_code == 1:
        return Node(0, h_local_min(road_map, start_city), [start_city], [])

    elif heuristic_code == 2:
        return Node(0, h_edges_min(road_map, [start_city]), [start_city], [])

    elif heuristic_code == 3:
        return Node(0, h_kruskal(road_map, [start_city]), [start_city], [])


def build_node(road_map, old_node, new_city, next_nodes, heuristic_code):
    movement_cost = road_map.edges[old_node.current_city][new_city]
    liste_som = old_node.liste_som + [new_city]
    estim_g = old_node.estim_g + movement_cost

    estim_h = h_zero()
    if heuristic_code == 1:
        estim_h = h_local_min(road_map, new_city)

    elif heuristic_code == 2:
        estim_h = h_edges_min(road_map, liste_som)

    elif heuristic_code == 3:
        estim_h = h_kruskal(road_map, liste_som)

    node = Node(estim_g, estim_h, liste_som, next_nodes)

    if len(liste_som) == road_map.nb_cities:
        leaf = build_node(road_map, node, node.liste_som[0], [], heuristic_code)
        node.next_nodes.append(leaf)

    return node


def h_zero():
    return 0


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


# TODO Algo de Kruskal sur les villes non visitées (composante connexe ?)
def h_kruskal(road_map, visited):
    cities = road_map.cities

    n = len(cities) - len(visited)
    return 0


def develop_node(road_map, node, heuristic_code):
    if len(node.next_nodes) > 0:
        return

    visited = node.liste_som
    total_cities = road_map.cities
    for i in total_cities:
        if i not in visited:
            new_node = build_node(road_map, node, i, [], heuristic_code)
            node.next_nodes.append(new_node)


def grp_size(nb_cities):
    size = 0
    for i in range(1, nb_cities + 1):
        size += math.factorial(nb_cities - 1) / math.factorial(nb_cities - i)
    size += math.factorial(nb_cities - 1)
    return size


def a_star(road_map, start_city, heuristic_code):
    open_heap = []
    count = 0
    start_node = build_start_node(road_map, start_city, heuristic_code)
    heapq.heappush(open_heap, start_node)
    n = None

    while len(open_heap) > 0:
        n = heapq.heappop(open_heap)

        if n.length == road_map.nb_cities + 1:
            print('Succès !')
            return n, count
        else:
            develop_node(road_map, n, heuristic_code)
            for heir in n.next_nodes:
                count += 1
                heapq.heappush(open_heap, heir)

    print('Echec !')
    return n, count
