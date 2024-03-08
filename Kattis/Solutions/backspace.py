str = input()
stack = []
finalString = ""
for a in range(len(str)):
    if str[a] == "<":
        stack.pop()
    else:
        stack.append(str[a])
print("".join(stack))