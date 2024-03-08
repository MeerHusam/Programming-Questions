from collections import defaultdict

n = int(input())
nums = input()

pos = defaultdict(int)
neg = defaultdict(int)
zeroes = 0

for num in nums.split(" "):
    if int(num) > 0:
        pos[int(num)] += 1
    elif int(num) < 0:
        neg[int(num)] += 1
    else:
        zeroes += 1

# Since 0 can be matches with any other zero, num matches can be calculates with the combinations formula
matches = zeroes * (zeroes - 1) // 2

# Now for postitive and negative numbers, multiply the occurrences of a positive number with it's negative number
for key in pos:
    matches += neg[-key] * pos[key]
print(matches)
