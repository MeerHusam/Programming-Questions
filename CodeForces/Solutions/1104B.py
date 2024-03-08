from collections import deque

str = deque(input())
stack = deque()
output = 1

for char in str:
    if stack and stack[-1] == char:
        stack.pop()
        output = -output
    else:
        stack.append(char)

if output == -1:
    print("Yes")
else:
    print("No")