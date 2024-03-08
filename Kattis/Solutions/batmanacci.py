n,k = map(int, input().split(' '))

# to store the length of each batmanacci string sequence
fib = [0,1,1]
for i in range(n+1):
    fib.append(fib[-1] + fib[-2])
while n > 2:
    if k > fib[n-2]:
        k -= fib[n-2]
        n -= 1
    else:
        n -= 2

if n == 1:
    print("N")

if n == 2:
    print("A")