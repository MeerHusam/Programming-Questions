"""
Problem Statement: https://leetcode.com/problems/3sum/description/
Author: Meer Husamuddin, https://github.com/MeerHusam/
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for k in range(len(nums) - 1):
            n3 = nums[k]
            if k > 0 and n3 == nums[k - 1]:
                continue
            i,j = k + 1, len(nums) - 1
            while(i < j):
                n1 = nums[i]
                n2 = nums[j]
                if (n1 + n2) == -n3 and (i != k and j != k):
                    a = (n1, n2, n3)
                    result = tuple(sorted(a))
                    output.add(result)
                    i += 1  
                    j -= 1
                elif (n1 + n2 > -n3):
                    j -= 1
                else:
                    i += 1  
        return output
