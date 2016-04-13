import random


class Node:
    def __init__(self, estim_g, estim_h, liste_som, next_nodes):
        self.estim_g = estim_g
        self.estim_h = estim_h
        self.liste_som = liste_som  # liste des villes
        self.next_nodes = next_nodes  # suite de la liste (successeur du noeud)

    @property
    def estim_f(self):
        return self.estim_g + self.estim_h

    @property
    def current_city(self):
        if self.longueur > 0:
            return self.liste_som[self.longueur - 1]

    @property
    def longueur(self):
        return len(self.liste_som)


class RoadMap:
    def __init__(self, map_size):
        self.cities = []
        for i in range(map_size):
            self.cities.append(i)

        self.edges = self.make_edges()

    def make_edges(self):
        edges = [[0 for x in range(self.nb_cities)] for y in range(self.nb_cities)]
        for i in range(self.nb_cities):
            edges[i][i] = -1
            for j in range(self.nb_cities):
                if i != j:
                    edges[i][j] = random.randint(1, 100)
                    edges[j][i] = edges[i][j]

        return edges

    @property
    def nb_cities(self):
        return len(self.cities)
