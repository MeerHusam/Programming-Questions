size = int(input())
balloons = list(map(int, input().split()))
arr = [0] * (size + 1)
res = 0
for h in balloons:
    if arr[h] > 0:
        arr[h] -= 1
    else:
        res+=1
    arr[h - 1] += 1
print(res)
