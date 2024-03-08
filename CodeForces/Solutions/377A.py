def perform_dfs(n, m, k, arr):
    def valid(x, y):
        return 0 <= x < n and 0 <= y < m

    if k == 0: 
        for row in arr:
            print(''.join(row))
        return

    x, y = -1, -1 
    to_visit = -k 

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                to_visit += 1
                x, y = i, j

    stack = [(x, y)] 
    while to_visit > 0 and stack:
        i, j = stack.pop()
        arr[i][j] = '?' 

        to_visit -= 1
    
        if i > 0 and arr[i - 1][j] == '.':
            stack.append((i - 1, j))
            arr[i - 1][j] = '@'
    
        if i < n - 1 and arr[i + 1][j] == '.':
            stack.append((i + 1, j))
            arr[i + 1][j] = '@'
    
        if j > 0 and arr[i][j - 1] == '.':
            stack.append((i, j - 1))
            arr[i][j - 1] = '@'
    
        if j < m - 1 and arr[i][j + 1] == '.':
            stack.append((i, j + 1))
            arr[i][j + 1] = '@'

    for row in arr:
        for element in row:
            if element == '?':
                print('.', end="")
            elif element == '.' or element == '@':
                print('X', end="")
            else:
                print(element, end="")
        print("")


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    maze = [list(input()) for _ in range(n)] 

    perform_dfs(n, m, k, maze)
