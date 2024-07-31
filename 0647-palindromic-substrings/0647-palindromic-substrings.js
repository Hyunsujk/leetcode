/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let count = 0
    for(let i=0; i<s.length; i++){
        // odd
        let lPt = i
        let rPt = i
        while(lPt >= 0 && rPt < s.length && s[lPt] == s[rPt]){
            count++
            lPt--
            rPt++
        }
        // even
        let lPte = i
        let rPte = i+1
        while(lPte >= 0 && rPte < s.length && s[lPte] == s[rPte]){
            count ++
            lPte--
            rPte++
        }
    }
    return count
};

// pointer is center
// if left and right pointer equals count++
// left --, right ++

// for odd, left = right
// for even, right = left+1