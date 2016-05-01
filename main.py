from salesman.roadmap import RoadMap
from salesman.tsp import a_star, grp_size


def calc(roadmap):
    print("Quelle heuristique faut-il utiliser ?",
          "0 : heuristique nulle",
          "1 : minimum local",
          "2 : somme des coûts minimums",
          "3 : arbre couvrant de poids minimum", sep="\n")

    code = int(input())
    start = int(input("\nDe quelle ville (de 0 à {}) faut-il partir ? ".format(n - 1)))

    print("Exécution de l'algorithme A*... ", end="")
    goal, count = a_star(roadmap, start, code)

    print("\nNombre de nœuds développés : {}".format(count),
          "Chemin obtenu à l'issue de l'algorithme : {}".format(goal.liste_som),
          "Longueur totale du circuit : {}".format(goal.estim_g), sep="\n", end="\n\n")


n = int(input("Combien de villes doit contenir la carte ? "))
print("Création d'une carte routière de {} villes...".format(n), end="\n\n")

road_map = RoadMap(n)
print("Les villes sont numérotées de 0 à {}. Affichage de la matrice des distances :".format(n - 1))
road_map.print()

size = int(grp_size(n))
print("\nDans cette situation, la taille totale du GRP est de {} nœuds.".format(size), end="\n\n")

restart = "o"
while restart == "o":
    calc(road_map)
    restart = input("Recommencer avec une autre heuristique ou une autre ville de départ ? [o/n] ")

print("Sortie du programme.")
