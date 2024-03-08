n = int(input())
names_set = set()
names_count = {}
while n > 0:
    str = input()
    if str not in names_set:
        names_count[str] = 0
        names_set.add(str)
        print("OK")
    else:
        names_count[str] += 1
        new_name = f"{str}{names_count[str]}"
        names_set.add(new_name)
        print(new_name)
    n -= 1
