# Code has some discrepency because difference in C++ and Python 
# floating point arithmetic
tCount = int(input())

for a in range(tCount):
    weightEarth, body, weightBody = input().split()
    weightEarth = int(weightEarth)
    weightBody = float(weightBody)
    print(f"Earth {weightEarth*10}N {body} {round(weightBody*weightEarth, 1)}N")