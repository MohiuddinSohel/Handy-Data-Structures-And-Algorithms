def bellman_Ford(times, N, K):
    adjList = defaultdict(list)
    parent = {}
    distance = {}
    for t in times:
        adjList[t[0]].append((t[1], t[2]))

        distance[t[0]] = float(inf)
        distance[t[1]] = float(inf)

        parent[t[0]] = None
        parent[t[1]] = None

    distance[K] = 0
    for _ in size(distance) - 1:  # loop for V-1 time
        for u in adjList.keys():  # update distance for all edges
            for v, cost in adjList[u]:
                if cost + distance[u] < distance[v]:
                    distance[v] = cost + distance[u]
                    parent[v] = u

    # Detect negative weight cycle, run for all edge on more time and if weight continue to decrease negative cycle

    for u in adjList.keys():
        for v, cost in adjList[u]:
            if cost + distance[u] < distance[v]:
                return True  # negative weight cycle

'''
 to find shortest path  from a vertex to all other vertex. Greedy. Can all be used for all source shortest path with O(VE)~O(V^3).
'''