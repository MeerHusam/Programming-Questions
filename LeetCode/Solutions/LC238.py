"""
    Problem Statement: https://leetcode.com/problems/product-of-array-except-self/description/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        length = len(nums)
        for a in range(length - 1):
            output.append(output[a] * nums[a])
        right = 1
        for a in range(length - 1, -1, -1):
            output[a] = output[a] * right
            right *= nums[a]
        return output