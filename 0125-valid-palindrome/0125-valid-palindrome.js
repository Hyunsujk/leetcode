/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const removed = s.replace(/[^a-z0-9]/gi, '').toLowerCase()
    return removed === removed.split("").reverse().join("")
};