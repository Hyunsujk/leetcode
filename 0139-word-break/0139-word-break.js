/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const cache = new Array(s.length+1).fill(false)
    cache[s.length] = true

    for(let i=s.length-1; i>=0; i--){
        for(const word of wordDict){
            if(i+word.length <= s.length // <= because i and the first char of word overlap
            && word == s.substring(i, i+word.length)){
                cache[i] = cache[i+word.length]
            }
            if(cache[i]){
                break;
            }
        }
    }

    return cache[0]
};

// cache is array s.length + 1 // +1 for the base case
// start from the end
// for the word in word,
// if start + word.length is less than s and dict matches substring start, word.length
// then cache[start] is cache[start+word.length]
// and break
// return cache[0] 