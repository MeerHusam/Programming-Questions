n = int(input())
nums = list(map(int, input().split()))
    
countNeg, count1, count2, ansp = 0, 0, 0, 0
    
for num in nums:
    if countNeg % 2 == 0:
        count1 += 1
    else:
        count2 += 1
    if num < 0:
        countNeg += 1
    
    if countNeg % 2 != 0:
        ansp += count2
    else:
        ansp += count1
    
ansn = (n*(n+1))//2 - ansp
print(ansn, ansp)