import heapq

def prims(n, edges, start):
    graph = [[] for _ in range(n + 1)]

    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * (n + 1)
    pq = [(0, start)]
    total = 0
    count = 0

    while pq and count < n:
        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        total += weight
        count += 1

        for w, v in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    return total


# Input
n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

start = int(input())

print(prims(n, edges, start))