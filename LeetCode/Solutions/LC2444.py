"""
    Problem Statement: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
class Solution:
        def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
            minIdx = maxIdx = badIdx = -1
            ans = 0
            for i, a in enumerate(nums):
                # Update the index of the "bad" element
                if not minK <= a <= maxK:
                    minIdx = maxIdx = badIdx = i
                # Update the index of the minimum element
                if a == minK: minIdx = i
                # Update the index of the maximum element
                if a == maxK: maxIdx = i
                # We take the min of minIdx and maxIdx because this is the index from where
                # the subarrays will start. We substract the badIdx because all elements on the left of badIdx
                # are invalid because badIdx is not in the range.
                # Eg: [7, 5, 1] Initially all indices are -1. But by the end, the indices are
                # badIdx = 0, minIdx = 2 and maxIdx = 1. Because the smaller index is 1, the subarrays will start from index 1.
                # Hence, the sum is 1 - 0 = 1. The subarray is [5,1]
                # Let's consider [7, 5, 1, 1] In this case, first the ans will be 1, then in the next iteration it becommes 1+1=2
                # The twp subarrays are [5,1] and [5,1,1]
                ans += min(minIdx, maxIdx) - badIdx
            return ans