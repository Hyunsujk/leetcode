/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    let carry;
    while((a & b) != 0){ // has things to carry
        carry = (a & b) << 1 // get carry
        a = a ^ b
        b = carry
    }
    // no more carry
    return a ^ b
};

// ^ add but ignore carry
// & return 1 if both are 1
// << 1 move left by 1 position