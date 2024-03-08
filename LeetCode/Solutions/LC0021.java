/*
 * Problem Statement:https://leetcode.com/problems/merge-two-sorted-lists/description/
 * Author: Meer Husamuddin, https://github.com/MeerHusam/
 */

package LeetCode.Solutions;

//  Definition for singly-linked list.
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode iter = head;
        while (l1 != null && l2 != null) {
            if (l1.val > l2.val) {
                iter.next = l2;
                l2 = l2.next;
            } else {
                iter.next = l1;
                l1 = l1.next;
            }
            iter = iter.next;
        }

        if (l1 == null)
            iter.next = l2;
        else
            iter.next = l1;

        return head.next;
    }
}