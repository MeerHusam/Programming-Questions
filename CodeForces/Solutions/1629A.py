t = int(input())

for a in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c =[[0, 0]] * n
    for i in range(n):
        c[i] = [a[i], b[i]]
        # if(a[i] <= k):
        #     k+= b[i]
        #     print(b[i])
    c.sort()
    for i in range(n):
        # print(c[i][0])
        if(c[i][0] <= k):
            k+= c[i][1]
            # print(b[i])
    # print(c[i])
    print(k)