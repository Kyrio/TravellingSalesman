import heapq
import math
from node import Node
from unionfind import Forest


def build_start_node(road_map, start_city, heuristic_code):
    """
    :param road_map: Carte routière correspondante.
    :param start_city: Ville de départ du voyageur.
    :param heuristic_code: Code désignant l'heuristique à calculer pour ce nœud.
    :return: Le nœud de départ (objet Node).

    Construit le premier noeud du graphe de résolution de problème (GRP).
    """

    if heuristic_code == 0:
        return Node(0, h_zero(), [start_city], [])

    elif heuristic_code == 1:
        return Node(0, h_local_min(road_map, start_city, [start_city]), [start_city], [])

    elif heuristic_code == 2:
        return Node(0, h_edges_min(road_map, [start_city]), [start_city], [])

    elif heuristic_code == 3:
        return Node(0, h_kruskal(road_map, [start_city]), [start_city], [])


def build_node(road_map, old_node, new_city, heuristic_code):
    """
    :param road_map: Carte routière correspondante.
    :param old_node: Prédécesseur du nœud à construire dans le GRP.
    :param new_city: Ville à ajouter à la liste de villes visitées.
    :param heuristic_code: Code désignant l'heuristique à calculer pour ce nœud.
    :return: Le nœud en question (objet Node).

    Construit un nœud du GRP à partir de son prédécesseur. Voir build_start_node pour le nœud de départ.
    """

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

    node = Node(estim_g, estim_h, liste_som, [])

    # Traite le cas de la fin du GRP : lorsque toutes les villes ont été visitées,
    # on crée le dernier nœud qui prend en compte le coût de retour à la ville de départ.
    if len(liste_som) == road_map.nb_cities:
        leaf = build_node(road_map, node, node.liste_som[0], heuristic_code)
        node.next_nodes.append(leaf)

    return node


def h_zero():
    """
    :return: Zéro (heuristique nulle)
    """
    return 0


def h_local_min(road_map, current_city, visited):
    """
    :param road_map: Carte routière correspondante.
    :param current_city: Dernière ville visitée (ville courante).
    :param visited: Liste des villes visitées.
    :return: Valeur de l'heuristique du minimum local dans le cas courant.

    Heuristique du minimum local : distance de la ville courante à la ville (non visitée) la plus proche.
    """

    cities = road_map.cities
    distances = []
    for i in cities:
        if i not in visited:
            distances.append(road_map.edges[current_city][i])
    if len(distances) == 0:
        return 0
    return min(distances)


def h_edges_min(road_map, visited):
    """
    :param road_map: Carte routière correspondante.
    :param visited: Liste des villes visitées.
    :return: Valeur de cette heuristique dans le cas courant.

    Cette heuristique s'obtient en faisant la somme du coût minimum issu de chaque ville non visitée.
    Un coût minimum issu d'une ville est la plus petite distance la séparant d'une autre ville de la carte.
    """

    sum_distance = 0
    cities = road_map.cities
    for i in cities:
        if i not in visited:
            sum_distance += min(road_map.edges[i])
    return sum_distance


def h_kruskal(road_map, visited):
    """
    :param road_map: Carte routière correspondante.
    :param visited: Liste des villes visitées.
    :return: Valeur de l'heuristique : poids de l'arbre de poids minimum.

    Heuristique de l'arbre de poids minimum. En utilisant l'algorithme de Kruskal (à l'aide d'ensembles disjoints),
    on obtient l'arbre de poids minium couvrant le graphe partiel où les arêtes inutiles (reliant des villes visitées
    auparavant) ont été retirées.
    """

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
    """
    :param road_map: Carte routière correspondante.
    :param node: Nœud à développer.
    :param heuristic_code: Code désignant l'heuristique à calculer pour ce nœud.

    Développe un nœud en construisant ses successeurs et en les ajoutant à sa liste de successeurs.
    """

    if len(node.next_nodes) > 0:
        return

    visited = node.liste_som
    total_cities = road_map.cities
    for i in total_cities:
        if i not in visited:
            new_node = build_node(road_map, node, i, heuristic_code)
            node.next_nodes.append(new_node)


def grp_size(nb_cities):
    """
    :param nb_cities: Nombre de villes dans l'exemple voulu.
    :return: Taille du GRP dans cet exemple.

    Calcule la taille du GRP en fonction du nombre de villes à visiter.
    """

    size = 0
    for i in range(1, nb_cities + 1):
        size += math.factorial(nb_cities - 1) / math.factorial(nb_cities - i)
    size += math.factorial(nb_cities - 1)
    return size


def a_star(road_map, start_city, heuristic_code):
    """
    :param road_map: Carte routière à utiliser.
    :param start_city: Ville de départ du voyageur.
    :param heuristic_code: Code désignant l'heuristique à calculer pour tous les nœuds du GRP.
    :return: Duplet contenant le nœud but (chemin optimal) en cas de succès, ainsi que le nombre de nœuds développés.

    Algorithme A*. Cette fonction est indépendante et appelle toutes les méthodes nécessaires au calcul
    du chemin optimal pour le voyageur de commerce sur une carte routière donnée.
    Elle retourne le dernier nœud retiré de la file OUVERT et le nombre de nœuds développés, et affiche "Succès !"
    si c'est un nœud but, ou "Échec !" si OUVERT est vide (échec de l'algorithme).
    """

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

    print('Échec !')
    return n, count
