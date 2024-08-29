/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let rob1 = 0
    let rob2 = 0

    // rob1, rob2, num
    for(const num of nums){
        const curr = Math.max(num + rob1, rob2)
        rob1 = rob2
        rob2 = curr
    }
    return rob2
};