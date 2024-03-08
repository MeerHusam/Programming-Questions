n = int(input())
str = input()
array = str.split("W")
length = len(array)
a = 0
for i in range(length):
    if array[a] == "":
        del array[a]
        length -= 1
    else:
        a += 1

print(len(array))
for a in range(len(array)):
    print(len(array[a]), end=" ")
print()