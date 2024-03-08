def main():
    n = int(input())
    values = list(map(int, input().split()))
    assert len(values) == n

    z = [0] * (n + 1)
    y = [0] * (n + 1)

    for i in range(1, n + 1):
        z[i] = z[i - 1] + values[i - 1]

    sorted_values = sorted(values)
    for i in range(1, n + 1):
        y[i] = y[i - 1] + sorted_values[i - 1]

    m = int(input())
    for _ in range(m):
        opt, l, r = map(int, input().split())
        if opt == 1:
            print(z[r] - z[l - 1])
        else:
            print(y[r] - y[l - 1])

if __name__ == "__main__":
    main()
