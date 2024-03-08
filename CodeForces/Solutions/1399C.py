t = int(input())

for a in range(t):
    n = int(input())
    k = list(map(int,input().split( )))
    k.sort()
    sums = [0] * (k[n - 1] * 2 + 1)
    # print("sums", sums)
    currentMax = 0
    for a in range(k[0], len(sums)):
        currentSum = a
        i, j = 0, n - 1
        while(i < j):
            if k[i] + k[j] == currentSum:
                sums[a] += 1
                i+=1
                j-=1
            elif k[i] + k[j] < currentSum:
                i +=1
            else:
                j -=1
        if sums[a] > currentMax:
            currentMax = sums[a]
    print(currentMax)
        