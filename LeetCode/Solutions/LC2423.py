"""
    Problem Statement: https://leetcode.com/problems/remove-letter-to-equalize-frequency/
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(M) where M is the number of unique words
"""
from typing import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Check if all the values are same
        def check():
            values_freq = Counter(count.values())
            # Eg: "aabbb", after removing one "b", the only frequency is 2
            if len(values_freq) == 1:
                return True
            elif len(values_freq) == 2:
                for val in values_freq:
                    # Eg: "aabbc", after removing c, the freq of 2 is two and for 0 its once
                    # The resulting string is "aabb", hence its valid
                    if val == 0:
                        return True
                # Eg: "aabbbb" after removing one a, the frequency is 1 one time and b 4 times
                return False
            # Eg: "aabbbc"
            else:
                return False

        count = Counter(word)
        for idx in count.keys():
            count[idx] -= 1
            if check():
                return True
            count[idx] += 1 
        
        return False