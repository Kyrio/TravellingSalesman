class Forest:
    """
    Classe utilisée dans la méthode des ensembles disjoints (union-find) pour l'algorithme de Kruskal.
    Elle est construite à partir d'une liste de sommets, et représente ces sommets sous forme d'arbres.
    Elle possède des méthodes pour trouver la racine d'un arbre (find) ou attacher deux arbres par la racine (union).
    """

    def __init__(self, vertices):
        """
        :param vertices: Liste de sommets (villes dans notre exemple) représentés par un indice.

        Constructeur de la forêt : à chaque sommet est associé un parent (lui-même à l'initialisation)
        et un rang (0 à l'initialisation car chaque arbre ne possède qu'un sommet).
        """

        self.parents = {}
        self.ranks = {}
        for v in vertices:
            self.parents[v] = v
            self.ranks[v] = 0

    def find(self, x):
        """
        :param x: Un sommet de la forêt (représenté par son indice).
        :return: Racine de l'arbre sur lequel se trouve le sommet.

        Cette méthode remonte les parents du sommet reçu en paramètre pour trouver la racine de l'arbre
        sur lequel il se trouve. Elle permet notamment de vérifier que deux sommets se trouvent sur le
        même arbre.
        """

        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        """
        :param x: Un sommet de la forêt (représenté par son indice).
        :param y: Un second sommet de la forêt (représenté par son indice).

        Cette méthode recherche, pour chacun des sommets reçus, la racine de l'arbre correspondant.
        Si ces racines sont identiques, alors les sommets sont sur le même arbre et aucun changement n'est nécessaire.
        Si elles sont différentes, alors la racine du plus petit arbre est attachée à celle de l'arbre le plus grand.
        """

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.ranks[root_x] > self.ranks[root_y]:
            self.parents[root_y] = root_x
        elif self.ranks[root_x] < self.ranks[root_y]:
            self.parents[root_x] = root_y
        else:
            self.parents[root_y] = root_x
            self.ranks[root_x] += 1
