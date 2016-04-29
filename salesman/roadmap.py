import random


class RoadMap:
    """
    Classe représentant une carte routière (liste des villes et distances entre elles).
    Dans ce modèle, pour tout couple de villes, il existe une route les reliant.
    """

    def __init__(self, map_size):
        """
        :param map_size: Nombre n de villes.

        Constructeur de la carte routière. Pour la taille n choisie, il génère une carte où les
        villes sont désignées par un indice de 0 à n-1, et une matrice de distances choisies aléatoirement.
        On se place dans le cas général où la cohérence géométrique n'est pas assurée.
        """

        self.cities = []
        for i in range(map_size):
            self.cities.append(i)

        self.edges = self.make_edges()

    def make_edges(self):
        """
        :return: Matrice des distances (tableau à deux dimensions).

        Fonction chargée de créer la matrice des distances entre les villes.
        M(i, j), i et j allant de 0 à n - 1, représente la distance entre la ville 0 et la ville 1.
        La matrice est symétrique et pour tout i, M(i, i) = +inf.
        """

        edges = [[0 for x in range(self.nb_cities)] for y in range(self.nb_cities)]
        for i in range(self.nb_cities):
            edges[i][i] = float('inf')
            for j in range(self.nb_cities):
                if i != j:
                    edges[i][j] = random.randint(1, 10)
                    edges[j][i] = edges[i][j]

        return edges

    def edge_list(self, visited):
        """
        :param visited: Liste des villes déjà visitées.
        :return: Liste des arêtes sous la forme (distance, ville_source, ville_destination)

        Fonction permettant d'obtenir les arêtes reliant entre elles les villes restant à visiter.
        Utilisée dans l'heuristique de Kruskal afin d'obtenir un arbre couvrant de poids minimum
        sur la carte privée des villes visitées.
        """

        e_list = []
        for x in range(len(self.edges)):
            for y in range(x + 1, len(self.edges[x])):
                if self.edges[x][y] != float('inf') and x < len(self.cities) and y < len(self.cities):

                    if x == visited[len(visited) - 1] and y not in visited:
                        e_list.append((self.edges[x][y], x, y))

                    elif y == visited[len(visited) - 1] and x not in visited:
                        e_list.append((self.edges[x][y], x, y))

                    elif x == visited[0] and y not in visited:
                        e_list.append((self.edges[x][y], x, y))

                    elif y == visited[0] and x not in visited:
                        e_list.append((self.edges[x][y], x, y))

                    elif x not in visited and y not in visited:
                        e_list.append((self.edges[x][y], x, y))

        return e_list

    @property
    def nb_cities(self):
        """
        :return: Nombre de villes dans la carte.
        """

        return len(self.cities)

    def print(self):
        """
        :return: Affichage de la matrice des distances sous une forme lisible.
        """

        for i in range(self.nb_cities):
            for j in range(self.nb_cities):
                print(str(self.edges[i][j]) + "\t", end="")
            print()
