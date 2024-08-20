/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const cleaned = s.replace(/[^a-z0-9]/gi, "").toLowerCase()
    return cleaned === cleaned.split("").reverse().join("")
};