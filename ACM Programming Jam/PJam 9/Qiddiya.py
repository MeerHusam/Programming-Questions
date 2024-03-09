def floyd_warshall(graph, n):
  dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

  for i in range(n):
    for j in range(n):
      if dist[i][j] == -1:
        dist[i][j] = float('inf')

  for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  return dist

def main():
  n = int(input().strip())
  graph = []
  for _ in range(n):
    row = input().strip().split()
    graph.append(int(x) if x != "-" else -1 for x in row)  
  hub = int(input())  
  dist = floyd_warshall(graph, n)
  for i in range(n):
    if i == hub:
      continue
    if dist[hub][i] == float('inf'):
      print(-1)
    else:
      print(dist[hub][i])

if __name__ == "__main__":
  main()