/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let map = {}
    let left = 0

    return s.split('').reduce((max, val, idx) => {
        const lastSeenIdx = map[val]

        const alreadyIncluded = left <= lastSeenIdx

        left = alreadyIncluded ? lastSeenIdx + 1 : left

        map[val] = idx

        const currentWindowSize = idx - left + 1

        return Math.max(max, currentWindowSize)
    }, 0)
    
};

// sliding window
// map is {}
// left is 0
// s.split().reduce(max/acc, val/cur, idx)
// get last seen index from map
// if left is less than or equal to last seen index, the character is already included in the window
// if included in the window, left is last seen index + 1 : left
// update the value index in map
// current window size is idx - left + 1
// return max between current window size and max