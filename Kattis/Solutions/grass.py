from typing import List, Tuple
from math import sqrt


def solve(seg: List[Tuple[float, float]], m: int, eps: float = 1e-9) -> int:
    res = 0
    y = 0.0
    seg = [(start, -end) for start, end in seg]
    i = 0
    while i < len(seg):
        if y + eps >= m:
            return res
        if seg[i][1] + eps <= y:
            i += 1
            continue
        if seg[i][0] - eps > y:
            return -1
        j = i
        u = i
        while j < len(seg) and seg[j][0] - eps <= y:
            if seg[j][1] > seg[u][1]:
                u = j
            j += 1
        y = seg[u][1]
        i = u + 1
        res += 1
    if y + eps >= m:
        return res
    return -1


def main():
    while True:
        try:
            n, m, w = map(int, input().split())
        except EOFError:
            break
        
        seg = []
        for _ in range(n):
            p, r = map(int, input().split())
            if 2.0 * r < w:
                continue
            d = sqrt(r ** 2 - (w / 2.0) ** 2)
            seg.append((p - d, -p - d))
        
        seg.sort()
        print(solve(seg, m))


if __name__ == "__main__":
    main()
