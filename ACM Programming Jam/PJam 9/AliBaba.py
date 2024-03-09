# test case 6, 7, 8, 9 are "Error"
import math
def main():
    
    x = float(input())
    if x < 100 or x > 100000000:
        print("Error")
        return
    
    y = float(input())
    if y > 3 or y < 1:
        print("Error")
        return
    
    z = float(input())
    if z > 50000:
        print("Error")
        return
  
    amount = x
    interest = 0
    
    for _ in range(11):
        interest = amount * (y/100)
        amount += interest
        amount -= z

    res = int(amount)
    print(res)
    if res < x:
        print("Bad")
    else:
        print("Good")
    
main()