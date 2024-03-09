def main():
    m, n = map(int, input().split())
    matrix = []
    visited = set()
    for _ in range (m):
        matrix.append(list(map(int, input().split())))
    
    i, j, sum = 0, 0, matrix[0][0]
    visited.add((0,0))

    while i != m - 1 or j != n - 1:
        
        neighbours = get_neighbours(matrix, i, j, visited)
        if neighbours == []:
            print(0, sum)
            return
        max = get_max(matrix, neighbours)
        
        if max not in visited:
            i, j = max[0], max[1]
            sum += matrix[i][j] 
            visited.add(max)
        else:
            print(-1)
            return    
    
    print(1, sum)

def get_neighbours(matrix, row, col, visited):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    neighbors = []

    if row - 1 >= 0 and (row - 1, col) not in visited:
        neighbors.append((row - 1, col))
    if row + 1 < rows and (row + 1, col) not in visited:
        neighbors.append((row + 1, col))
    if col - 1 >= 0 and (row, col - 1) not in visited:
        neighbors.append((row, col - 1))
    if col + 1 < cols and (row, col + 1) not in visited:
        neighbors.append((row, col + 1))

    return neighbors

def get_max(matrix, neighbours):
    current_max , index = 0, (0, 0)
    for neighbour in neighbours:
        i, j = neighbour
        if matrix[i][j] > current_max:
            current_max = matrix[i][j]
            index = (i, j)
    return index
    
main()