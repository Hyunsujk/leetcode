/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    const steps = [0, 1, 2]
    
    for(let i = 3; i <= n; i++){
        steps[i % 3] = steps[(i-1) % 3] + steps[(i-2) % 3]
    }
    return steps[n % 3]
};

//base case
// n is 0, return 0
// n is 1, return 1
// n is 2, return 2