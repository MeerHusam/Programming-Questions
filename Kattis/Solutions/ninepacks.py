def min_packs(hotdogs, buns):
    MAX = 100000

    opt_h = [float('inf')] * (MAX + 1)
    opt_b = [float('inf')] * (MAX + 1)

    opt_h[0] = 0
    opt_b[0] = 0

    for h in hotdogs:
        for k in range(MAX, h - 1, -1):
            if opt_h[k - h] != float('inf'):
                opt_h[k] = min(opt_h[k], opt_h[k - h] + 1)


    for b in buns:
        for k in range(MAX, b - 1, -1):
            if opt_b[k - b] != float('inf'):
                opt_b[k] = min(opt_b[k], opt_b[k - b] + 1)


    answer = min(opt_h[k] + opt_b[k] for k in range(1, MAX + 1))

    if answer == float('inf'):
        return "impossible"
    return answer

def parse_input():
    H, *hotdogs = map(int, input().split())
    B, *buns = map(int, input().split())
    return hotdogs, buns

def main():
    hotdogs, buns = parse_input()
    result = min_packs(hotdogs, buns)
    print(result)

if __name__ == "__main__":
    main()