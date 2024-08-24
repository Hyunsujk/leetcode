/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const dict = {}
    for(let i=0; i<strs.length; i++){
        const key = strs[i].split("").sort().join("")
        if(dict[key]){
            dict[key].push(strs[i])
        } else {
            dict[key] = [strs[i]]
        }
    }
    return Object.values(dict)  
};

// iterate through arr
// use set as key, if matches push to array
// return values