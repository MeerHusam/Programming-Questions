"""
    Problem Statement: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
# This qn is very similar to https://leetcode.com/problems/subarray-product-less-than-k/ 
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        i = ans = product = 0
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            product = (sum) * (j - i + 1)
            while product >= k and i <= j:
                sum -= nums[i]
                i += 1
                product = sum * (j - i + 1)                
            ans += j - i + 1
        return ans