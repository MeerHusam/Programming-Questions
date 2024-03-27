"""
    Problem Statement: https://leetcode.com/problems/subarray-product-less-than-k/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        i = ans = 0
        product = 1
        for j in range(len(nums)):
            product *= nums[j]
            while product >= k and i <= j:
                product /= nums[i]
                i += 1
            ans += j - i + 1
        return ans