from math import sqrt

def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def find_parent(idx, parents):
    if parents[idx] == idx:
        return idx
    parents[idx] = find_parent(parents[idx], parents)
    return parents[idx]

def main():
    t = int(input())
    for _ in range(t):
        s, p = map(int, input().split())
        if s >= p:
            print("0.00")
            continue
        
        outposts = [tuple(map(int, input().split())) for _ in range(p)]
        edges = [(i, j, dist(outposts[i], outposts[j])) for i in range(p) for j in range(i+1, p)]
        edges.sort(key=lambda x: x[2])

        parents = [i for i in range(p)]
        weights = []

        for a, b, w in edges:
            parent_a = find_parent(a, parents)
            parent_b = find_parent(b, parents)
            
            if parent_a != parent_b:
                parents[parent_a] = parent_b
                weights.append(w)

        weights.sort(reverse=True)
        print(f"{weights[s - 1]:.2f}")

if __name__ == "__main__":
    main()
