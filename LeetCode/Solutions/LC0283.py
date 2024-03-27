"""
    Problem Statement: https://leetcode.com/problems/move-zeroes/

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            while i < len(nums) - 1 and nums[i] != 0:
                i += 1
            if nums[j] != 0 and i < j:
                nums[i], nums[j] = nums[j], nums[i]        