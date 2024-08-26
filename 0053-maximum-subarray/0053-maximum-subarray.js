/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSub = nums[0]
    let currSub = 0

    for(const n of nums){
        if(currSub < 0){
            currSub = 0
        }
        currSub = currSub + n
        maxSub = Math.max(currSub, maxSub)
    }
    return maxSub
};