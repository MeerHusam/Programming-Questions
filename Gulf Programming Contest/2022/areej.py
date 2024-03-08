def main():
    while True:
        pCount, nCount = map(int, input().split())
        if pCount == 0:
            print()
            break
        for a in range(pCount):
            vCount = int(input())
            dict = {}
            curr_max = 0
            max_index = ""
            for b in range(vCount):
                vote = input()
                if vote not in dict:
                    dict[vote] = 1
                else:
                    dict[vote] += 1
                    if dict[vote] > curr_max:
                        max_index = vote
                        curr_max = dict[vote]
            print(max_index)
        print()
    
main()