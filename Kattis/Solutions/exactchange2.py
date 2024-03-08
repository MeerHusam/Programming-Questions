def calculate_min_payment():
    results = []
    num_cases = int(input())

    for _ in range(num_cases):
        price = int(input())
        num_denominations = int(input())
        dp = [float('inf')] * 10001
        dp[0] = 0

        for _ in range(num_denominations):
            coin = int(input())
            for amt in range(10000 - coin, -1, -1):
                dp[amt + coin] = min(dp[amt + coin], dp[amt] + 1)

        for amt in range(price, 10001):
            if dp[amt] < float('inf') / 2:
                results.append(f"{amt} {dp[amt]}")
                break

    return results


if __name__ == "__main__":
    output = calculate_min_payment()
    for line in output:
        print(line)
