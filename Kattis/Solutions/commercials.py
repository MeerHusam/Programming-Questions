n, price = input().split(" ")
n = int(n)
price = int(price)
currentMax, totalMax = 0, 0
nums = input().split(" ")

for num in nums:
    currentMax = max(int(num) - price, currentMax + int(num) - price );
    totalMax = max(currentMax, totalMax)
print(totalMax)