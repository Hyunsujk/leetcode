/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const cleaned = s.replace(/[^a-z0-9]/gi,"").toLowerCase()
    
    let l = 0
    let r = cleaned.length-1
    
    while(l<r){
        if(cleaned.charAt(l) !== cleaned.charAt(r)){
            return false
        }
        l++
        r--
    }
    return true
};