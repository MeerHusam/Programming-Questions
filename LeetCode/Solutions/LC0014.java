/*
 * Problem Statement:https://leetcode.com/problems/longest-common-prefix/description/
 * Author: Meer Husamuddin, https://github.com/MeerHusam/
 */
package LeetCode.Solutions;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        String str = strs[0];
        for (int i = 1; i < strs.length; i++) {
            if (str.length() > strs[i].length())
                str = str.substring(0, strs[i].length());
            for (int j = 0; j < str.length() && j < strs[i].length(); j++)
                if (strs[i].charAt(j) != str.charAt(j))
                    str = str.substring(0, j);
        }
        return str;
    }
}
