n = int(input())
for a in range(n):
    curr = int(input())
    count = 0
    while(curr > 0):
        if(curr % 2 == 0):
            curr = curr // 2
        elif(curr % 5 == 0):
            curr = (4 * curr) // 5
        elif(curr % 3 == 0):
            curr = (2 * curr) // 3
        elif(curr == 1):
            print(count)
            break;
        else:
            print(-1)
            break;
        count += 1