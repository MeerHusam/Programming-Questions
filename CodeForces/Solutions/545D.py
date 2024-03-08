n = int(input())
people = list(map(int, input().split()))
people.sort()
# print(people)
count = 0
time = 0
for a in people:
    if a >= time:
        count+=1
        time += a
print(count)