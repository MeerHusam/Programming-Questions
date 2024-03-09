"""
    Passes 35% of test cases. Will update with complete code later
"""


import sys
sys.setrecursionlimit(10000)

MOD = 998244353

def modular_pow(base, exponent):
    result = 1
    base %= MOD
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % MOD
        exponent >>= 1
        base = (base * base) % MOD
    return result

def modular_inverse(x):
    return modular_pow(x, MOD - 2)

def compute_factorials(limit):
    factorials = [1]
    inverse_factorials = [1]
    inverse = [0] * (limit + 1)
    inverse[1] = 1
    for i in range(2, limit + 1):
        inverse[i] = MOD - (MOD // i) * inverse[MOD % i] % MOD
    for i in range(1, limit + 1):
        factorials.append((factorials[-1] * i) % MOD)
        inverse_factorials.append((inverse_factorials[-1] * inverse[i]) % MOD)
    return factorials, inverse_factorials


def lucas_theorem(n, r, factorials, inverse_factorials):
    result = 1
    while n > 0 or r > 0:
        ni, ri = n % MOD, r % MOD
        if ri > ni:
            return 0
        result = (result * (factorials[ni] * (inverse_factorials[ri] * inverse_factorials[ni - ri] % MOD)) % MOD) % MOD
        n //= MOD
        r //= MOD
    return result
    
    
def main():
    k, n = map(int, input().split())
    factorials, inverse_factorials = compute_factorials(100000)

    results = []
    for t in range(2**k):
        sum_ = 0
        i = t
        while i <= n:
            sum_ += lucas_theorem(n, i, factorials, inverse_factorials)
            sum_ %= MOD
            i += 2**k
        results.append(sum_)

    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()
