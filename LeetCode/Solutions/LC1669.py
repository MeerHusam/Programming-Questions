"""
    Problem Statement: https://leetcode.com/problems/merge-in-between-linked-lists/description/
    Author: Meer Husamuddin

    Time Complexity: O(N + M)
    Space Complexity: O(1)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        iter = list1
        while a > 1:
            a -= 1
            b -= 1
            iter = iter.next
        iter2 = iter
        while b > 0:
            b -= 1
            iter2 = iter2.next
        iter.next = list2
        while iter.next:
            iter = iter.next
        iter.next = iter2.next
        return list1