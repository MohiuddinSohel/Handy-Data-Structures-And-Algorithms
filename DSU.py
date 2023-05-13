class DSU:
    def __init__(self):
        self.parent = defaultdict()
        self.rank = defaultdict()

    def find(self, x, parent): # path compression
        while x in parent.keys() and x != parent[x]:
            if parent[x] in parent.keys():
                parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(self, x, y, parent, rank): # union by rank
        xP = find(x, parent)
        yP = find(y, parent)
        if xP == yP:
            return True
        if rank[xP] < rank[yP]:
            xP, yP = yP, xP
        parent[yP] = xP
        if rank[xP] == rank[yP]:
            rank[xP] += 1
        return False

if __name__ == "__main__":
    dsu = DSU()
    for x, y in edges:
        dsu.parent[x], dsu.parent[y], dsu.rank[x], dsu.rank[y] = x, y, 0, 0

    removal = None
    for x, y in edges:
        if unionFind(x, y, parent, rank):
            return [x, y]
    return removal

'''
684. Redundant Connection
'''