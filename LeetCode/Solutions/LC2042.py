"""
    Problem Statement: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        values = s.split()
        prevalue = -1
        for val in values:
            if val.isdigit():
                if int(val) <= prevalue:
                    return False
                prevalue = int(val)
        return True