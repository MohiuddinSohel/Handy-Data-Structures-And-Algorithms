def dijkstra(times, N, K):
    adjList = defaultdict(list)
    parent = {}
    distance = {}
    Visited = set()
    heap = [(0, K, -1)]
    for t in times:
        adjList[t[0]].append((t[1], t[2]))

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, cost in adjList[u]:
            if v not in visited and d + cost < distance[v]:
                parent[v] = u
                distance[v] = d + cost
                heapq.heappush(heap, (d + cost, v))

'''
Time complexity: ElogE= 2ElogV~ given that E= v^2
'''