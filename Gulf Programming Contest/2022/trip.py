def check(a):
    n = int(input())
    curr_set = set()
    cities = list(map(int, input().split()))
    cities.remove(cities[0])
    for city in cities:
        curr_set.add(city)
    flag = False
    for b in range(n - 1):
        new_set = set()
        cities = list(map(int, input().split()))
        cities.remove(cities[0])
        for city in cities:
            if city in curr_set:
                new_set.add(city)
        if len(new_set) == 0:
            flag = True
        else:
            curr_set = new_set
            new_set = set()
    
    if flag:
        print(f"{a+1}. No Trip")
        return
    print(f"{a+1}. ", end="")
    sorted_curr_set = sorted(curr_set)
    print(','.join(map(str, sorted_curr_set)))

k = int(input())
for a in range(k):
    check(a)