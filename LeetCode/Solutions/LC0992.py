"""
    Problem Statement: https://leetcode.com/problems/subarrays-with-k-different-integers/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        set = defaultdict(int)
        l_far = l_near = num_distinct = output = 0
        for r in range(len(nums)):
            if nums[r] not in set or set[nums[r]] == 0:
                num_distinct += 1
            
            set[nums[r]] += 1
            
            while num_distinct > k:
                set[nums[l_near]] -= 1
                if set[nums[l_near]] == 0:
                    num_distinct -= 1
                l_near += 1
                l_far = l_near

            while set[nums[l_near]] > 1:
                set[nums[l_near]] -= 1
                l_near += 1

            if num_distinct == k:
                output += l_near - l_far + 1
                
        return output