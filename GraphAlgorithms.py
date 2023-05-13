class Algorithms:

    def dijkstra(self, times, N, K):
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


    def bellman_Ford(self, times, N, K):
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
    
    def prim(self, N: int, connections: List[List[int]]) -> int:
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

    '''
    Space complexity: O(E+V)
    E from edgelist and V from disjoint set
    Time complexity: O (ElogE + ElogV)
    ElogE from sorting and V from disjoint set operation 

    '''

    def targansAlgorithm(self, adjList, current, parent, visited, currentDisCoveryTime, lowestDisCovryTime, result):
        visited.add(current)
        lowestDisCovryTime[current] = currentDisCoveryTime

        for node in adjList[current]:
            if parent == node:
                continue
            if node not in visited:
                self.dfs(adjList, node, current, visited, currentDisCoveryTime + 1, lowestDisCovryTime, result)

            lowestDisCovryTime[current] = min(lowestDisCovryTime[current], lowestDisCovryTime[node])

            if currentDisCoveryTime < lowestDisCovryTime[node]:
                result.append([current, node])
        return result



if __name__ == "__main__":
    algorithm = Algorithms()
    