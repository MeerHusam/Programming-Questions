def find_heights(n, h0, a, c, q):
    heights = [h0]
    for i in range(1, n):
        hi = (a * heights[i - 1] + c) % q
        heights.append(hi)
    return heights

def noticeable_count(heights):
    i, j = 0, 1
    count = 0
    # Iterate until both i and j do not reach the end
    while(i < len(heights) and j < len(heights) and i != j):
        # if j is larger or equal to i, increase i as all heights to the left of i
        # will not be visible OR if j is at the end, and the height is smaller than i, increase i
        if heights[j] >= heights[i] or (j == len(heights) - 1 and heights[j] < heights[i]):
            i += 1
            j = min(i + 1, len(heights))
        # increase j if j is smaller than i and j is not at the end
        elif heights[j] < heights[i]:
            j += 1
            
        # Count increases in each iteration because no matter what, a height to 
        # the immediate left is visible to the right element
        count += 1

    return count

n, h0, a, c, q = map(int, input().split())
heights = find_heights(n, h0, a, c, q)
print(noticeable_count(heights))