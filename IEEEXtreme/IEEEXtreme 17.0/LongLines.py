def find_heights(n, h0, a, c, q):
    heights = [h0]
    for i in range(1, n):
        hi = (a * heights[i - 1] + c) % q
        heights.append(hi)
    return heights

def noticeable_count(heights):
    i = 0
    j = 1
    count = 0
    while(i < len(heights) and j < len(heights) and i != j):
        if heights[j] >= heights[i]:
            count += 1
            i += 1
            j = i
        else:
            count += 1
        
        
        if j == len(heights) - 1 and heights[j] < heights[i]:
            i += 1
            j = i
        if j != len(heights) - 1:
            j += 1
        # print(i, j, count)
    return count

n, h0, a, c, q = map(int, input().split())
heights = find_heights(n, h0, a, c, q)
print(noticeable_count(heights))