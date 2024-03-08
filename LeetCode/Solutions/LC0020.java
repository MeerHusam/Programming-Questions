/*
 * Problem Statement:https://leetcode.com/problems/valid-parentheses/description/
 * Author: Meer Husamuddin, https://github.com/MeerHusam/
 */
package LeetCode.Solutions;

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        if (s.length() % 2 != 0)
            return false;
        for (char c : s.toCharArray()) {
            if (c == '(')
                st.push(')');
            else if (c == '[')
                st.push(']');
            else if (c == '{')
                st.push('}');
            else {
                if (st.isEmpty() || c != st.peek())
                    return false;
                st.pop();
            }
        }
        return st.isEmpty();
    }
}
