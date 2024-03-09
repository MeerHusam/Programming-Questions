"""
    Passes 75% of all test cases
"""
from collections import deque

def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def distribute_water(elevation, i, j, n, m):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([(i, j)])
    visited = set()

    while queue:
        x, y = queue.popleft()
        lower_cells = []
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n, m) and elevation[x][y] > elevation[nx][ny]:
                lower_cells.append((nx, ny))
        
        if lower_cells:
            split_water = water[x][y] / len(lower_cells)
            for nx, ny in lower_cells:
                water[nx][ny] += split_water
                if (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
            water[x][y] = 0

def main():
    n, m = map(int, input().split())
    elevation = [list(map(int, input().split())) for _ in range(n)]
    global water
    water = [[1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            distribute_water(elevation, i, j, n, m)

    print(max(max(row) for row in water))  

main()
