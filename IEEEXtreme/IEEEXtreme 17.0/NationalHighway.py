"""
    Passes 55% of all test cases. Will update later with complete code
"""

def find(city, parents):
    if parents[city] != city:
        parents[city] = find(parents[city], parents)
    return parents[city]

def union(city1, city2, parents, ranks):
    root1, root2 = find(city1, parents), find(city2, parents)
    if root1 != root2:
        if ranks[root1] > ranks[root2]:
            parents[root2] = root1
        else:
            parents[root1] = root2
            if ranks[root1] == ranks[root2]:
                ranks[root2] += 1

def solve(n, edges):
    edges.sort(key=lambda x: x[0])
    parents = {city: city for city in set(city for edge in edges for city in edge[1:])}
    ranks = {city: 0 for city in parents}
    totalCost = 0
    mst_edges = []
    for cost, city1, city2 in edges:
        if find(city1, parents) != find(city2, parents):
            union(city1, city2, parents, ranks)
            mst_edges.append((cost, city1, city2))
            totalCost += cost

    # Look for alternative edges
    for cost, city1, city2 in edges:
        if ((cost, city1, city2) not in mst_edges and
            find(city1, parents) != find(city2, parents)):
            totalCost += cost

    # Check connectivity
    root = find(next(iter(parents)), parents)
    if all(find(city, parents) == root for city in parents):
        return totalCost
    return -1

n = int(input())
edges = []
for _ in range(n):
    edge_input = input().split()
    cost = int(edge_input[2])
    city1, city2 = edge_input[0], edge_input[1]
    edges.append((cost, city1, city2))

print(solve(n, edges))