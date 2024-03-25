"""
    Problem Statement: https://leetcode.com/problems/reverse-linked-list
    Author: Meer Husamuddin

    Time Complexity: O(N)
    Space Complexity: O(1)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev