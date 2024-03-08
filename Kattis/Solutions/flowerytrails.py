import heapq
from collections import defaultdict, deque

inf = (1 << 63) - 1

n, m = map(int, input().split())
dist = [inf]  * n
parent = [[] for _ in range(n)]
adj = [[] for _ in range(n)]
vis = [False] * n

mat = defaultdict(lambda: defaultdict(int))

for _ in range(m):
    n1, n2, w = map(int, input().split())
    if n1 == n2:
        continue
    adj[n1].append((w, n2))
    adj[n2].append((w, n1))

    if mat[(n1)][(n2)] == 0 or mat[(n1)][(n2)] > w:
        mat[(n1)][(n2)] = mat[(n2)][(n1)] = w

pq = [(0, 0)]
dist[0] = 0

while pq:
    curr_dist, curr = heapq.heappop(pq)
    if vis[curr]:
        continue
    vis[curr] = True

    for weight, next_node in adj[curr]:
        if dist[curr] + weight < dist[next_node]:
            dist[next_node] = dist[curr] + weight
            parent[next_node] = [(dist[curr] + weight, curr)]
            heapq.heappush(pq, (dist[curr] + weight, next_node))
        elif dist[curr] + weight == dist[next_node]:
            parent[next_node].append((dist[curr] + weight, curr))

vis = [False] * n
q = deque([n - 1])
total = 0

while q:
    curr = q.popleft()
    if vis[curr]:
        continue
    vis[curr] = True
    for dist_curr, prev in parent[curr]:
        total += mat[curr][prev]
        q.append(prev)

print(total * 2)
