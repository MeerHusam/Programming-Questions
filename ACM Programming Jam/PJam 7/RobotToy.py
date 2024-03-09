from collections import deque

def main():
    
    N = int(input().strip())
    matrix = []
    start = end = None

    for i in range(N):
        row = list(input().strip())
        matrix.append(row)
        for j, val in enumerate(row):
            if val == 'X':
                start = (i, j)
            elif val == 'Y':
                end = (i, j)

    min_moves = bfs(matrix, start, end, N)
    
    print(min_moves + 1)
    
def bfs(matrix, start, end, N):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] # E, S, W, N
    queue = deque([(start, 0)]) # (position, moves)
    visited = set([start])

    while queue:
        (x, y), moves = queue.popleft()

        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < N:
                if (nx, ny) == end:
                    # Check if it's possible to stop at 'Y'
                    next_x, next_y = nx + dx, ny + dy
                    if not (0 <= next_x < N and 0 <= next_y < N) or matrix[next_x][next_y] == '#':
                        print(visited)
                        return moves
                    
                nx += dx
                ny += dy

                if not (0 <= nx < N and 0 <= ny < N) or matrix[nx][ny] == '#':
                    if (nx - dx, ny - dy) not in visited:
                        visited.add((nx - dx, ny - dy))
                        queue.append(((nx - dx, ny - dy), moves + 1))
                    break
    return 
main()