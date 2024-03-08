def main():
    n = int(input())
    for a in range(n):
        setNum = set()
        size = int(input())
        str = input()
        if(checkString(size,str, setNum)):
            print("YES")
        else:
            print("NO")
            
def checkString(size, str, setNum):
    if (len(str) != size):
        return False
    if size == 1:
        return True
    for b in range(size):
        if str[b] not in setNum:
            setNum.add(str[b])
        elif str[b] in setNum and str[b -1] == str[b]:
            continue
        else:
            return False
    return True

main()