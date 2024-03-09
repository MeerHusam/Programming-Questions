package LeetCode.Solutions;

/* 
Problem Statement: https://leetcode.com/problems/swap-nodes-in-pairs/description/
Author: Meer Husamuddin, https://github.com/MeerHusam/
*/
// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode next = head.next;
        ListNode prev = head;
        head = next;
        while (next != null) {
            ListNode temp = prev;
            prev.next = next.next;
            next.next = prev;

            prev = prev.next;
            next = (prev == null) ? null : prev.next;
            if (next != null)
                temp.next = next;

            // System.out.println("prev" + prev.val);
            // System.out.println("next" + next.val);
        }
        return head;
    }
}