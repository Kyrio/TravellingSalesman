from node import Node, RoadMap
from unionfind import Forest
import math
import heapq


def build_start_node(road_map, start_city, heuristic_code):
    if heuristic_code == 0:
        return Node(0, h_zero(), [start_city], [])

    elif heuristic_code == 1:
        return Node(0, h_local_min(road_map, start_city, [start_city]), [start_city], [])

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
        estim_h = h_local_min(road_map, new_city, liste_som)

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


# FIXME heuristique nulle plus efficace lol
def h_local_min(road_map, current_city, visited):
    cities = road_map.cities
    distances = []
    for i in cities:
        if i not in visited:
            distances.append(road_map.edges[current_city][i])
    if len(distances) == 0:
        return road_map.edges[current_city][visited[0]]

    return min(distances)


def h_edges_min(road_map, visited):
    sum_distance = 0
    cities = road_map.cities
    for i in cities:
        if i not in visited:
            sum_distance += min(road_map.edges[i])
    return sum_distance


# def make_set(x):
#     x.parent = x
#     x.rank = 0
#
#
# def find(x):
#     if x.parent != x:
#         x.parent = find(x.parent)
#     return x.parent
#
#
# def union(x, y):
#     root_x = find(x)
#     root_y = find(y)
#
#     if root_x == root_y:
#         return
#
#     if root_x.rank > root_y.rank:
#         root_y.parent = root_x
#     elif root_x.rank < root_y.rank:
#         root_x.parent = root_y
#     else:
#         root_y.parent = root_x
#         root_x.rank += 1
#

# TODO Algo de Kruskal sur les villes non visitées (composante connexe ?)
def h_kruskal(road_map, visited):
    edge_list = road_map.edge_list(visited)
    cities = road_map.cities
    forest = Forest(cities)

    tree_weight = 0

    edge_list.sort()
    for weight, u, v in edge_list:
        if forest.find(u) != forest.find(v):
            tree_weight += weight
            forest.union(u, v)

    return tree_weight


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
