def compute(N, t, e, chromes):
    
    # Finding the sum of the initial values
    for a in range(len(chromes)):
            chromes[a].append(eval(chromes[a]))
            
    for _ in range(e):
        # Sorting based on the sum
        chromes = sorted(chromes, key=lambda x: x[-1])

        highest_values = chromes[-2:]
        
        # Get the child with the highest value
        child = children(highest_values)
        
        # In the sorted list, if the childs sum is higher than
        # the sum of the lowest val, replace it
        if(child[-1] > chromes[0][-1]):
            chromes[0] = child
        
        # Sort again
        chromes = sorted(chromes, key=lambda x: x[-1])
        
    return chromes[-1][-1]

# To evaluate the strength of each chromosome
def eval(chromes):
    sum = 0
    for a in chromes:
        sum += a
    return sum

# To generate the children
def children(chromes):
    C1, C2 = chromes[0], chromes[1]
    
    cross_point = len(C1) // 2  
    C4 = C1[:cross_point] + C2[cross_point:] 
    C5 = C2[:cross_point] + C1[cross_point:] 
    
    C4[-1] = eval(C4[: len(C4) - 1])
    C5[-1] = eval(C5[: len(C5) - 1])

    if (C5[-1] > C4[-1] ):
        temp = C5[-2]
        C5[-2] = C5[0]
        C5[0] = temp
        return C5
    else:
        temp = C4[-2]
        C4[-2] = C4[0]
        C4[0] = temp
        return C4
    
def main():
    N, t, e = map(int, input().split())
    
    if N >= 1000 or N <= 0:
        print(-1)
        return
    chromes = []
    
    try:
        while True:
            input_list = list(map(int, input().split()))
            
            for val in input_list:
                if val < 0 or val > 50:
                    print(-1)
                    return
            chromes.append(input_list)
    except EOFError:
            pass
    
    print(compute(N, t, e, chromes))
    
main()