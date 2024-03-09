import heapq

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight
    
    def __lt__(self, other):
        return self.weight < other.weight

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]
    
    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append(Edge(source, destination, weight))
        self.adjacency_list[destination].append(Edge(destination, source, weight))  # For undirected graph
    
    def dijkstra_get_min_distances(self, start_vertex, end_vertex):
        visited = [False] * self.vertices
        distances = [float('inf')] * self.vertices
        distances[start_vertex] = 0

        pq = []
        heapq.heappush(pq, Edge(start_vertex, start_vertex, 0))
        
        while pq:
            edge = heapq.heappop(pq)
            vertex = edge.destination
            
            if visited[vertex]:
                continue
            visited[vertex] = True
            
            for e in self.adjacency_list[vertex]:
                if not visited[e.destination]:
                    new_dist = distances[vertex] + e.weight
                    if new_dist < distances[e.destination]:
                        distances[e.destination] = new_dist
                        heapq.heappush(pq, Edge(vertex, e.destination, new_dist))
        
        return distances

def main():
    N, M, S, D, T = map(int, input().split())
    S -= 1
    D -= 1

    graph = Graph(N)

    for _ in range(M):
        u, v, c, p = map(int, input().split())
        u -= 1
        v -= 1
        if c >= T:
            graph.add_edge(u, v, p)
    
    distances = graph.dijkstra_get_min_distances(S, D)
    print(distances[D] if distances[D] != float('inf') else -1)

if __name__ == "__main__":
    main()