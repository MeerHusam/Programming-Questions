def dfs(matrix, a, p, visited):
    visited.add(a)
    for j in range(p):
        if matrix[a][j] and j not in visited:
            dfs(matrix, j, p, visited)

def check_dfs(matrix, p):
    for a in range(p):
        for b in range(a + 1, p):
            if matrix[a][b]:
                # Temporarily remove the connection
                matrix[a][b], matrix[b][a] = False, False

                visited = set()
                dfs(matrix, 0, p, visited)  # Start DFS from node 0

                # Restore the connection
                matrix[a][b], matrix[b][a] = True, True

                if len(visited) != p:
                    return "Yes"
    return "No"

def main():
    while True:
        p, c = map(int, input().split())
        if p == 0 and c == 0:
            break

        adj_matrix = [[False for _ in range(p)] for _ in range(p)]
        for _ in range(c):
            a, b = map(int, input().split())
            adj_matrix[a][b] = True
            adj_matrix[b][a] = True
        
        print(check_dfs(adj_matrix, p))

main()
