import sys

def main():
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        capacity, n = map(int, line.split())
        items = []
        for _ in range(n):
            value, weight = map(int, sys.stdin.readline().split())
            items.append((value, weight))
        selected_item_indexes = knapsack(items, capacity)
        print_result(selected_item_indexes)

def knapsack(items, capacity):
    n = len(items)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(1, capacity + 1):
            if weight <= w:
                table[i][w] = max(table[i - 1][w], table[i - 1][w - weight] + value)
            else:
                table[i][w] = table[i - 1][w]

    chosen_items = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
    
            chosen_items.append(i - 1)
    
            w -= items[i - 1][1]

    return chosen_items

def print_result(selected_item_indexes):
    print(len(selected_item_indexes))
    for index in sorted(selected_item_indexes):
        print(index, end=' ')
    print()

if __name__ == "__main__":
    main()
