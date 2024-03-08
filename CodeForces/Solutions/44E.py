k, a, b = map(int, input().split())
text = input()
length = len(text)

if length/k < a or length/k > b:
    print("No solution")
    exit()

s = 0
ans = []

for a in range(k):
    if a == k - 1:
        ans.append(text[s : ])
    else:
        ans.append(text[s : s + length // k])
    s += length // k

for an in ans:
    print(an)