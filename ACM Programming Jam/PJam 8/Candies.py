from itertools import combinations

def main():
    # read input prices and budget
    prices = list(input().split())
    for i in range(len(prices)):
        if prices[i].isdigit():
            prices[i] = int(prices[i])
        else:
            print("0")
            return
    budget = int(input())

    # find all combinations of prices that add up to budget
    valid_combinations = []
    for i in range(1, len(prices)+1):
        for comb in combinations(prices, i):
            abc = list(comb)
            abc.sort()
            if sum(abc) == budget:
                valid_combinations.append(abc)


    # print valid combinations in ascending order
    for comb in sorted(valid_combinations):
            print(*sorted(comb))
    if len(valid_combinations) == 0:
        print("0")
            
main()