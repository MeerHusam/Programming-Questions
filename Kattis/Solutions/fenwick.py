import sys

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def query(self, index):
        sum_ = 0
        while index > 0:
            sum_ += self.tree[index]
            index -= index & -index
        return sum_
    
    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

def read_input():
    N, Q = map(int, sys.stdin.readline().split())
    fenwick_tree = FenwickTree(N)
    output = []
    
    for _ in range(Q):
        operation = sys.stdin.readline().split()
        if operation[0] == '+':
            idx, delta = int(operation[1]) + 1, int(operation[2])
            fenwick_tree.update(idx, delta)  
        else:  # operation[0] == '?'
            idx = int(operation[1])
            output.append(str(fenwick_tree.query(idx)))
    
    print("\n".join(output))

read_input()
