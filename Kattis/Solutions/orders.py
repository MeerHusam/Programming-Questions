from collections import Counter
from functools import lru_cache
import sys

sys.setrecursionlimit(10_000_000)

IMPOSSIBLE = "Impossible"
AMBIGUOUS = "Ambiguous"

def solve(menu):
    menu_count = Counter(menu)
    menu_duplicates = {item for item, count in menu_count.items() if count > 1}
    menu_set = set(menu_count.keys())

    @lru_cache(maxsize=None)
    def find_combination(order):
        if order < 0:
            return IMPOSSIBLE
        if order == 0:
            return Counter()

        if order in menu_set:
            if order in menu_duplicates:
                return AMBIGUOUS
            return Counter({order: 1})

        solutions = []

        for item in menu_set:
            solution = find_combination(order - item)
            if solution == IMPOSSIBLE:
                continue
            if solution == AMBIGUOUS:
                return AMBIGUOUS
            new_solution = solution.copy()
            new_solution.update({item: 1})
            solutions.append(new_solution)

        if not solutions:
            return IMPOSSIBLE

        # If more than one distinct solution exists, it's ambiguous
        for i in range(len(solutions) - 1):
            if solutions[i] != solutions[i+1]:
                return AMBIGUOUS

        return solutions[0]

    return find_combination

def main():
    _ = input()
    menu = list(map(int, input().split()))
    _ = input()
    orders = list(map(int, input().split()))

    menu_index = {value: index for index, value in enumerate(menu, start=1)}
    find_solution = solve(menu)

    for order in orders:
        result = find_solution(order)
        if result in [IMPOSSIBLE, AMBIGUOUS]:
            print(result)
        else:
            output_order = [menu_index[item] for item, count in result.items() for _ in range(count)]
            print(' '.join(map(str, sorted(output_order))))

if __name__ == '__main__':
    main()