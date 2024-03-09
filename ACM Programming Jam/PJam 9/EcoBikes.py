def main():
    # Assuming inputs are floating point numbers, similar to Java's double
    n, s, c, x, scenario = float(input()), float(input()), float(input()), int(input()), int(input())
    
    if not (5000 <= n + s + c <= 7000 and 0 < n <= 5000 and 0 < s <= 5000 and 0 < c <= 5000 and scenario in [1, 2]):
        print(0)
        return

    for _ in range(7):  # Perform the calculations 7 times
        if scenario == 1:
            newN = (n * 0.10) + (s * 0.30) + (c * 0.25)
            newS = (s * 0.20) + (c * 0.35) + (n * 0.30)
            newC = (c * 0.40) + (s * 0.50) + (n * 0.60)
        elif scenario == 2:
            newN = (n * 0.60) + (s * 0.30) + (c * 0.25)
            newS = (s * 0.20) + (c * 0.35) + (n * 0.30)
            newC = (c * 0.40) + (s * 0.50) + (n * 0.10)
        
        # Update n, s, c for the next iteration
        n, s, c = map(lambda x: float(x) // 1, (newN, newS, newC))  # Floor the results to simulate Java's Math.floor

    count_exceed = sum(val > x for val in [n, s, c])
    
    # Output based on the count of outlets exceeding X
    if count_exceed == 0:
        print(2)
    elif count_exceed == 1:
        print(4)
    elif count_exceed == 2:
        print(3)
    elif count_exceed == 3:
        print(1)
    else:
        print(0)

main()