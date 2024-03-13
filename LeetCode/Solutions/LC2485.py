"""
    Problem Statement: https://leetcode.com/problems/find-the-pivot-integer/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = n * (n + 1)/2
        sum = [0]
        for a in range(1, n + 1):
            sum.append(sum[a - 1] + a)
        sum2 = 0
        for a in range(len(sum) - 1, -1, -1):
            sum2 += a
            if sum2 == sum[a]:
                return(a)
        return -1