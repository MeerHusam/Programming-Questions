"""
Problem Statement: https://leetcode.com/problems/reverse-integer/description/
Author: Meer Husamuddin, https://github.com/MeerHusam/
"""
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1 
        INT_MIN = -2**31    
        
        rev = 0
        negative = x < 0
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > INT_MAX//10 or (rev == INT_MAX // 10 and pop > 7):
                return 0
            if rev < INT_MIN//10 or (rev == INT_MIN // 10 and pop < -8):
                return 0
            
            rev = rev * 10 + pop
        
        if negative:
            rev = -rev
        
        return rev

