i = 0      
while True:
    d, r = map(int,input().split())
    if d ==0 and r == 0:
        break
    dString, rString = bin(d), bin(r)
    dString, rString = "".join(dString[2:]), "".join(rString[2:])
    
    while len(dString) < 24:
        dString = "0" + dString
        
    while len(rString) < 24:
        rString = "0" + rString
        
    operations ,countDifference, countDifferenceZeros, countDifferenceOnes = 0, 0, 0, 0
    for a in range(24):
        if dString[a] != rString[a]:
            dString[a] == rString[a]
            countDifference+=1
        if rString[a] != "0":
            countDifferenceZeros +=1 
        else:
            countDifferenceOnes += 1
                
    # understand why this failed earlier for "9328869 7448346" when we had the line
    # countDifferenceZeros > countDifferenceOnes on line 33
    # Update: i was missing <= (the = sign)
    if countDifference > countDifferenceZeros + 1 and countDifferenceZeros <= countDifferenceOnes:
        dString = "000000000000000000000000"
        operations = 1
    elif countDifference >= countDifferenceOnes + 1 and countDifferenceZeros > countDifferenceOnes:
        dString = "111111111111111111111111"
        operations = 1
    for a in range(24):
        if dString[a] != rString[a]:
            dString[a] == rString[a]
            operations+=1
    print(f"{i + 1}.", operations)
    i += 1