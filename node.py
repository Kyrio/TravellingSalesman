import random


class Node:
    def __init__(self, estim_g, estim_h, liste_som, next_nodes):
        self.estim_g = estim_g
        self.estim_h = estim_h
        self.liste_som = liste_som  # liste des villes
        self.next_nodes = next_nodes  # suite de la liste (successeurs du noeud)

    def __lt__(self, other):
        return self.estim_f < other.estim_f

    def __gt__(self, other):
        return self.estim_f > other.estim_f

    @property
    def estim_f(self):
        return self.estim_g + self.estim_h

    @property
    def current_city(self):
        if self.length > 0:
            return self.liste_som[self.length - 1]

    @property
    def length(self):
        return len(self.liste_som)


class RoadMap:
    # FIXME indices ou valeurs pour décrire les villes ?

    def __init__(self, map_size):
        self.cities = []
        for i in range(map_size):
            self.cities.append(i)

        self.edges = self.make_edges()

    def make_edges(self):
        edges = [[0 for x in range(self.nb_cities)] for y in range(self.nb_cities)]
        for i in range(self.nb_cities):
            edges[i][i] = float('inf')
            for j in range(self.nb_cities):
                if i != j:
                    edges[i][j] = random.randint(1, 10)
                    edges[j][i] = edges[i][j]

        return edges

    def get_distance(self, x, y):
        return self.edges[x][y]

    def edge_list(self, visited):
        e_list = []
        for x in range(len(self.edges)):
            for y in range(x + 1, len(self.edges[x])):
                if self.edges[x][y] != float('inf') and x < len(self.cities) and y < len(self.cities):

                    if x == visited[len(visited)-1] and y not in visited:
                        e_list.append((self.edges[x][y], x, y))

                    elif x == visited[0] and y not in visited:
                        e_list.append((self.edges[x][y], x, y))

                    elif y == visited[len(visited) - 1] and x not in visited:
                        e_list.append((self.edges[x][y], x, y))

                    elif y == visited[0] and x not in visited:
                        e_list.append((self.edges[x][y], x, y))

                    elif x not in visited and y not in visited:
                        e_list.append((self.edges[x][y], x, y))

        return e_list

    @property
    def nb_cities(self):
        return len(self.cities)

    def print(self):
        for i in range(self.nb_cities):
            for j in range(self.nb_cities):
                print(str(self.edges[i][j]) + "\t", end="")
            print()
