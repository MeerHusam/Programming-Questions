n = int(input())
arr = list(map(int, input().split()))
f = [[0] * n for _ in range(n)]
 
for length in range(1, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if i == j:
            f[i][j] = 1
        else:
            if arr[i] == arr[j]:
                f[i][j] = f[i + 1][j - 1] if i + 1 <= j - 1 else 1
            else:
                f[i][j] = min(f[i + 1][j], f[i][j - 1]) + 1
            for k in range(i, j):
                f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j])
 
print(f[0][n - 1])