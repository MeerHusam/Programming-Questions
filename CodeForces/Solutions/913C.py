n,l = map(int, input().split())
costs = list(map(int, input().split()))

for a in range(1,n):
    costs[a] = min(costs[a], 2 * costs[a -1])
# print(costs)

ans = float('inf') 
sum = 0

for i in range(n - 1, -1, -1):
    bit = l // (1 << i) 
    sum += bit * costs[i] 
    l -= bit << i 
    ans = min(ans, sum + (l > 0) * costs[i]) 

print(ans)