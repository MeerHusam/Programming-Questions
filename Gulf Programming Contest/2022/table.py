def main():
    k = int(input())
    for a in range(k):
        calc(a)
  
def calc(a):
    h, s, n = map(int, input().split())
    heights = list(map(int , input().split()))
    
    heights = sorted(heights)
    # Add 0 at the start
    heights.insert(0, 0)
    # Add the height of the table at the end
    heights.append(h)
    
    running_difference = []
    for i in range(len(heights) - 2):
        running_difference.append(heights[i + 2] - heights[i])
        
    for index,diff in enumerate(running_difference):
        if diff > s:
            print(f"{a + 1}. {heights[index + 1]}")
            return
    print(f"{a + 1}. Not possible")
    
main()