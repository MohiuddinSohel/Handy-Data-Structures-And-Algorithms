def kruskal(N: int, connections: List[List[int]]) -> int:
    rank = {i: 0 for i in range(N + 1)}
    parent = {i: i for i in range(N + 1)}

    minimumSpanningTree = defaultdict(set)  # track the MST
    minimumCost = 0
    connections.sort(key=lambda x: x[2])

    for edge in connections:
        if union(parent, rank, edge[0], edge[1]):
            minimumCost += edge[2]
            minimumSpanningTree[edge[0]].add(edge[1])

    root = find(parent, N)  # track one mst or multiple mst
    return minimumCost if all(root == find(parent, x) for x in range(1, N)) else -1

if __name__ == "__main__":
    kruskal(N, connections)

'''
Space complexity: O(E+V)
E from edgelist and V from disjoint set
Time complexity: O (ElogE + ElogV)
ElogE from sorting and V from disjoint set operation 

'''