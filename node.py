class Node:
    """
    Classe représentant un nœud du graphe de résolution de problème (GRP).
    """

    def __init__(self, estim_g, estim_h, liste_som, next_nodes):
        """
        :param estim_g: La valeur de g (coût du chemin parcouru) estimant le coût optimal du nœud de départ à celui-ci
        :param estim_h: La valeur de h (calculée selon l'heuristique) estimant le coût optimal de ce nœud à un but
        :param liste_som: Liste des villes déjà parcourues
        :param next_nodes: Liste des successeurs du noeud (normalement vide tant qu'on n'a pas développé le nœud)

        Constructeur d'un nœud du GRP.
        """

        self.estim_g = estim_g
        self.estim_h = estim_h
        self.liste_som = liste_som
        self.next_nodes = next_nodes

    def __lt__(self, other):
        """
        :param other: Un autre nœud du GRP.
        :return: Vrai si f < f(other)

        Fonction utilisée pour comparer un nœud à un autre selon la valeur de f.
        """

        return self.estim_f < other.estim_f

    def __gt__(self, other):
        """
        :param other: Un autre nœud du GRP.
        :return: Vrai si f > f(other)

        Fonction utilisée pour comparer un nœud à un autre selon la valeur de f.
        """

        return self.estim_f > other.estim_f

    @property
    def estim_f(self):
        """
        :return: La valeur de f (fonction d'évaluation) où f = g + h.
        """

        return self.estim_g + self.estim_h

    @property
    def current_city(self):
        """
        :return: La ville dans laquelle le voyageur se trouve, c'est-à-dire la dernière de liste_som.
        """

        if self.length > 0:
            return self.liste_som[self.length - 1]

    @property
    def length(self):
        """
        :return: Le nombre de villes parcourues.
        """

        return len(self.liste_som)
