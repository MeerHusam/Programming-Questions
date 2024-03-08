"""
Problem Statement: https://leetcode.com/problems/add-two-numbers/
Author: Meer Husamuddin, https://github.com/MeerHusam/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        iter = dummyHead
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = x + y + carry
            carry = sum // 10
            iter.next = ListNode(sum % 10)
            iter = iter.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummyHead.next