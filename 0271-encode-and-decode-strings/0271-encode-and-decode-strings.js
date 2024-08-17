/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
var encode = function(strs) {
    const res = []
    for(const str of strs){
        res.push(str.length + "#" + str)
    }
    return res.join("")    
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
var decode = function(s) {
    const res = []
    let i = 0
    while(i < s.length){
        let j = i
        while(s[j] != "#"){ // get length number
            j++
        } // j is #
        const length = Number(s.slice(i, j))
        const word = s.slice(j+1, j+1+length)
        res.push(word)
        i = j+1+length //now i is beginning of the next word
    }

    return res
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */

 // str length # str