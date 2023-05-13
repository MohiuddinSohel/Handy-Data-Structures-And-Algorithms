def prim(N: int, connections: List[List[int]]) -> int:
    if not connections:
        return -1
    minimumSpanningTree = defaultdict(set)  # track the MST
    adjList = defaultdict(list)
    visited = set()
    heap = [(0, 1, 1)]  # select node 1(with imaginary edge with cost 0) as first
    for c in connections:
        adjList[c[0]].append((c[1], c[2]))
        adjList[c[1]].append((c[0], c[2]))

    minimumCost = 0
    while heap and len(visited) < N:
        cost, u, v = heapq.heappop(heap)
        if v in visited:
            continue

        visited.add(v)
        minimumCost += cost
        minimumSpanningTree[u].add(v)

        for nei, cost in adjList[v]:
            if nei in visited:
                continue
            heapq.heappush(heap, (cost, v, nei))

    if len(visited) < N:
        return -1
    return minimumCost

'''
Space complexity: O(E+V)
V from heap and E from edge tracker for each edge
Time complexity: O(ElogV +VlogV), theoretical
In the worst case, add all E edges to heap
Each edge enters and exits heap at most once, logE
Thus, ElogE ~ ElogV^2 ~ ElogV
'''