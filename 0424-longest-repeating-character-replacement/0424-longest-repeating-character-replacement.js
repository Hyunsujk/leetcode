/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let count = {}
    let maxFreq = 0
    let maxLength = 0
    let l = 0

    for(let r=0; r<s.length; r++){
        count[s[r]] = (count[s[r]] || 0) + 1
        maxFreq = Math.max(maxFreq, count[s[r]])

        while((r-l+1) - maxFreq > k){
            count[s[l]]--
            l++
        }
        maxLength = Math.max(r-l+1, maxLength)
    }
    return maxLength
};

// l is 0
// r is moving
// count of r char ++
// if length - maxFreq is > k, decrement the l count and move l
// maxLength is max between length and maxLength
// return maxLength