custDict = {}
maxPossibleMoney = []
sum = 0

n, k = map(int,input().split(' '))

for customer in range(n):
    money, time = map(int,input().split(' '))
    custDict.setdefault(time, []).append(money)

for time in range(k)[::-1]:
    if time in custDict.keys():
        for money in custDict[time]:
            maxPossibleMoney.append(money)
        if maxPossibleMoney:
            sum += max(maxPossibleMoney)
            maxPossibleMoney.remove(max(maxPossibleMoney))
print(sum)