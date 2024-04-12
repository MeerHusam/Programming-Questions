"""
    Problem Statement: https://leetcode.com/problems/trapping-rain-water/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0   

        maxl, maxr = 0, len(height) - 1
        maxl_value, maxr_value = height[maxl], height[maxr]
        total_amount = 0

        while maxl < maxr:
            if maxl_value > maxr_value:
                maxr -= 1
                maxr_value = max(maxr_value, height[maxr])
                total_amount += maxr_value - height[maxr]
            else:
                maxl += 1
                maxl_value = max(maxl_value, height[maxl])
                total_amount += maxl_value - height[maxl]
        return total_amount