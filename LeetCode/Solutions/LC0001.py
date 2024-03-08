"""
Problem Statement: https://leetcode.com/problems/two-sum/description/
Author: Meer Husamuddin, https://github.com/MeerHusam/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        