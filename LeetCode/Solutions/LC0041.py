"""
    Problem Statement: https://leetcode.com/problems/first-missing-positive/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        one_exists = False
        # First change all the negative values and the values greater than
        # len(nums) to 1 as the missing value should be between 1 and len(nums) + 1
        for index, a in enumerate(nums):
            # If 1 doesnt exist in the original array, 1 is the required value
            if a == 1:
                one_exists = True
            if a > len(nums) or a <= 0:
                nums[index] = 1
        
        if not one_exists:
            return 1
        
        # Change the value of nums[a - 1] to -nums[a -1] indicating that the value
        # a exists in the array. If nums[a] isn't negative we know that a 
        # is the smallest required positive
        # Eg: [1, 2, 2]. After changing the values: [-1, -2, 2]. The value at index
        # 2 is positive hence the required value is 2 + 1 = 3
        for a in nums:
            if a <= len(nums):
                nums[abs(a) - 1] = -abs(nums[abs(a) - 1])

        # The first index with positive value is the required index
        for index, a in enumerate(nums):
            if a > 0:
                return index + 1
        # If all values are negative, the requried val is len(nums) + 1
        return len(nums) + 1