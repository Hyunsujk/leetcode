/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if(s.length == 0){
        return "";
    }

    function getSubSize(string, left, right){
        while(left >= 0 && right < string.length && string[left] == string[right]){
            left--;
            right++;
        }
        return right - left - 1; // overrun, exclude left, then -1 for included right. 
    }

    let max = 0
    let start = 0
    let end = 0

    for(let i=0; i<s.length; i++){
        const odd = getSubSize(s, i, i)
        const even = getSubSize(s, i, i+1)
        const sub = Math.max(odd, even)

        if(sub > max){
            max = sub
            start = i - Math.floor((sub-1)/2) // because i is part of the left partition
            end = i + Math.floor(sub/2)
        }
    }
    return s.slice(start, end+1)
};

// base case
// if s length is 0 return empty array

// function getSubSize string, left, right
// while left is >=0 && right is < s.length and left == right
// then left--, right ++
// return right - left - 1

// max = 0
// start = 0
// end = 0

// for i from 0 til s.length
// odd = s, i, i
// even = s, i, i+1
// sub = math.max odd, even

// if sub > max
// max = sub
// start = i - floor(sub-1 / 2)
// end = i + floor(sub/2)

// return s.slice(start, end+1)