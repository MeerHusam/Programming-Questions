size = int(input())
sequence = list(map(int, input().split()))
lowest = min(sequence)
gap = 0
recent = size + size
for idx, value in enumerate(sequence + sequence):
    if value == lowest:
        if idx - recent > gap:
            gap = idx - recent
        recent = idx
print(lowest * size + gap - 1)
