s = input()
k = 0
flag = True
for a in range(len(s)):
    if s[a] == '(' or s[a] == ')':
        flag = False
    elif flag:
        k += 1
    else:
        k -= 1
if k == 0:
    print("correct")
else:
    print("fix")