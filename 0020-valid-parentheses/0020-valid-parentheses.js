/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if(s.length === 1){
        return false
    }

    const options = new Map([
        ["(", ")"], 
        ["{", "}"], 
        ["[", "]"]
    ])
    const openings = Array.from(options.keys())
    let q = []
    for(let i=0; i<s.length; i++){
        if(openings.includes(s[i])){
            q.push(s[i])
        } else { // closing
            if(!q.length || options.get(q[q.length-1]) !== s[i]){
                return false
            }
            q.pop()
        }
    }
    return !q.length
};

// base case
// if length is 1 return false
// build dict (:), {:}, [:]
// get list of opening // dict.keys() 
// q = []
// iterate through s, if it's in opening list, push to q,
// if not in opening list, which means closing, pop from q, check if dict(pop) doesn't match, return false
// global return true