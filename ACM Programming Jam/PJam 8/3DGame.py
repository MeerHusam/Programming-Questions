def main():
    num = input()
    if num.isdigit():
        num = int(num)
        if num < 2:
            print("0")
            return
    else:
        print("0")
        return

    l = []
    for a in range(num):
        l.append(int(input()))
    l.sort()
    
    if l [0] < 0:
        print("0")
        return

    size = len(l)
    prices = []

    for b in range(num):
        price = l[b] * (num - b)
        prices.append(price)

    prices.sort()
    print(prices[num-1])

main()