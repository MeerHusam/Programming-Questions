n = int(input())

laptops = [None] * n
for i in range(n):
    laptops[i] = list(map(int, input().split()))

laptops = sorted(laptops)
flag = True
for i in range(n-1):
    if laptops[i][1] > laptops[i+1][1]:
        flag = False
        break
    else:
        flag = True
if(flag):
    print('Poor Alex')
else:
    print('Happy Alex')
