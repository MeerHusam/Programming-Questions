n = int(input())

weights = []
for _ in range(n):
    weights.append(int(input()))

lis = [1] * n
lds = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if weights[i] < weights[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        if weights[i] > weights[j]:
                    lds[i] = max(lds[i], 1 + lds[j])

maxLength = 0
for a in range(n):
       maxLength = max(maxLength, lis[a] + lds[a] - 1)
print(maxLength)