/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    const count = {}
    count[0] = 0
    count[1] = 1

    for(let i=2; i<=n; i++){
        count[i] = count[i-1] + count[i-2]
    }
    return count[n]
};