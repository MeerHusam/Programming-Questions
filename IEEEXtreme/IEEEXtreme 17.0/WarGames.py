t = int(input())

cards = ["2", "3", "4", "5", '6', "7", "8", "9", "T", "J", "Q", "K", "A"]
for _ in range(t):
    p1 = list(input().split(' '))
    p2 = list(input().split(' '))

    max_turns = 51 * 51
    turn_count = 0

    while len(p1) > 0 and len(p2) > 0:
        if turn_count > max_turns:
            print("draw")
            break
        turn_count += 1
        index1 = cards.index(p1[0])
        index2 = cards.index(p2[0])
        
        if index1 > index2:
            p1.append(p2.pop(0))
            p1.pop(0)
        elif index1 < index2:
            p2.append(p1.pop(0))
            p2.pop(0)
        else:
            p1.append(p1.pop(0))
            p2.append(p2.pop(0))
    else:
        if len(p1) == 0:
            print("player 2")
        else:
            print("player 1")