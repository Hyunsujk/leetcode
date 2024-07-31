/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let count = 0
    for(let i=0; i<s.length; i++){
        // odd
        count += countPalin(s, i, i)
        // even
        count += countPalin(s, i, i+1)
    }
    return count
};

function countPalin(s, lPt, rPt){
    let count = 0
    while(lPt >= 0 && rPt < s.length && s[lPt] == s[rPt]){
        count ++
        lPt--
        rPt++
    }
    return count
}

// pointer is center
// if left and right pointer equals count++
// left --, right ++

// for odd, left = right
// for even, right = left+1