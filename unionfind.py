class Forest:
    # FIXME probleme d'indices (refaire une classe pour chaque union ?)
    def __init__(self, vertices):
        self.parents = vertices.copy()
        self.ranks = [0 for i in range(len(vertices))]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
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
