/*
    Problem Statement: https://leetcode.com/problems/return-length-of-arguments-passed/description/
    Author: Meer Husamuddin

    Time Complexity: O(1)
    Space Complexity: O(1)
*/
/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */