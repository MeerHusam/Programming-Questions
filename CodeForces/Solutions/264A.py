s = input()
for a in range(len(s)):
    if s[a] == 'r':
        print(a  +1)

for a in range(len(s), 0 , -1):
    # print(a)
    if s[a - 1] == 'l':
        print(a)