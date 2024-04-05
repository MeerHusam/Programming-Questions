"""
    Problem Statement: https://leetcode.com/problems/make-the-string-great/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(N)
"""
class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack:
                temp = stack.pop()
                if (temp.isupper() and s[i] != temp.lower()) or (temp.islower() and s[i] != temp.upper()):
                    stack.append(temp)
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return "".join(stack)