"""
    Fails the test case, but passes the rest
"""

t = int(input())
for _ in range(t):
    r,c,a,b = map(int, input().split())
    if r > c:
        print("YES")
    else:
        print("NO")