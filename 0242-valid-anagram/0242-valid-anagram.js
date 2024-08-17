/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length !== t.length){
        return false
    }

    const map = {}
    for(let i=0; i<s.length; i++){
        if(!map[s[i]]){
            map[s[i]] = 1
        } else {
            map[s[i]]++
        }
    }
    for(let i=0; i<t.length; i++){
        if(map[t[i]] && map[t[i]] !== 0){
            map[t[i]]--
        } else {
            return false
        }
    }

    return Object.values(map).filter(v => v !== 0).length > 0 ? false : true
};