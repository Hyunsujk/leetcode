/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const brackets = new Map([
        ["(", ")"],
        ["{", "}"],
        ["[", "]"]
    ])
    const openings = Array.from(brackets.keys())
    let q = []
    for(let i=0; i<s.length; i++){
        if(openings.includes(s[i])){ // if opening bracket
            q.push(s[i])
        } else { // if closing bracket
            if(!q.length || brackets.get(q[q.length-1]) != s[i]){ // if no opening left or not matching
                return false
            }
            q.pop()
        }
    }
    return !q.length // if length is not 0 extra openings    
};

// opening left
// opening and closing are matching
// closing left