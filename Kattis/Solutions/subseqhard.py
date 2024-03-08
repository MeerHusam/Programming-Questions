def count_interesting_subsequences(sequence):
    s = 0
    m = {0: 1}
    res = 0
    for num in sequence:
        s += num
        res += m.get(s - 47, 0)
        m[s] = m.get(s, 0) + 1
    return res

def main():
    t = int(input().strip())  
    
    for _ in range(t):
        input()  
        n = int(input().strip())  
        sequence = list(map(int, input().strip().split()))  
        result = count_interesting_subsequences(sequence)
        print(result)

if __name__ == "__main__":
    main()
