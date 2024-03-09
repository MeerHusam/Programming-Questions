from collections import Counter
t = int(input())

for _ in range(t):
    sentence = input()
    char_occurrence = Counter(sentence)
    sorted_by_occurrence = sorted(char_occurrence.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_by_occurrence:
        if 'a' <= char <= 'g':
            print(char.upper())
            break