k = int(input())
for a in range(k):
    d, s, p, r = map(int, input().split())
    
    sum = d - p
    sum = 1 if sum <=0 else sum
    sum += r
    sum = d if sum >= d else sum
    
    print(f"{a+1}.", sum)