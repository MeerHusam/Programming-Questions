def main():
    num = int(input())
    
    skil = sorted(list(map(int, input().split())))
    people = sorted(list(map(int, input().split())))    
    
    # Test case 4
    if min(people) < 0 or min(skil) < 0:
        print(-1)
        return
    count = 0
    for a in range(len(people)):
        count += abs(int(skil[a]) - int(people[a]))
    print(count)
main()