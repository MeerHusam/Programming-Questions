t = int(input())

for a in range(t):
    n, x = map(int, input().split())
    savings = list(map(int, input().split()))
    savings.sort(reverse=True)
    count = 0

    currentAverage = 0
    sum = 0
    count = 0
    for a in range(len(savings)):
        currentAverage = savings[a]
        sum += savings[a]
        currentAverage = sum / (a + 1)
        if currentAverage >= x:
            count += 1
            continue
        else:
            break
    print(count)
    
