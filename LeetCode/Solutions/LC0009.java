package LeetCode.Solutions;

import java.util.Stack;

/*
 * Problem Statement:https://leetcode.com/problems/palindrome-number/description/
 * Author: Meer Husamuddin, https://github.com/MeerHusam/
 */

class Solution {
    public boolean isPalindrome(int x) {

        if (x < 0)
            return false;

        Stack stack = new Stack();
        String str = Integer.toString(x);
        String rts = "";

        for (int i = 0; i < str.length(); i++) {
            stack.push(str.charAt(i));
        }

        int size = stack.size();
        for (int i = 0; i < size; i++) {

            rts += stack.pop();
        }
        if (str.equals(rts))
            return true;
        else
            return false;
    }

}